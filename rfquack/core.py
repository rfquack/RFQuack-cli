# -*- coding: utf-8 -*-

"""
This is a Python implementation of a RFQuack client.

RFQuack is a versatile RF-analysis tool that allows you to sniff, analyze, and
transmit data over the air.

Copyright (C) 2019 Trend Micro Incorporated

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import sys
import logging

from rfquack import rfquack_pb2
from rfquack import topics

logger = logging.getLogger('rfquack.core')


class RFQuack(object):
    """
    The RFQuack object connects to a given transport and abstracts the
    invocation of commands to the RFQuack dongle by means of function calls.
    """

    def __init__(self, transport, shell):
        self._mode = 'IDLE'
        self._ready = False
        self._transport = transport
        self._shell = shell

        self.data = {}

        self._init()

    def _init(self):
        """
        - reset packet modifications
        - put the tool in sending mode
        """
        self._transport.init(on_message_callback=self._recv)

    def _recv(self, *args, **kwargs):
        cmd = kwargs.get('cmd')
        msg = kwargs.get('msg')

        if cmd in self.data:
            self.data[cmd].append(msg)
        else:
            self.data[cmd] = [msg]

        out = ''

        # suppress output for certain data
        if not isinstance(msg, rfquack_pb2.Packet):
            out = str(msg)

        # type-specific output
        if isinstance(msg, rfquack_pb2.Register):
            fmt = '0x{addr:02X} = 0b{value:08b} (0x{value:02X}, {value})'
            out = fmt.format(
                    **dict(addr=msg.address, value=msg.value))

        if out:
            sys.stdout.write('\n')
            sys.stdout.write(out)
            sys.stdout.write('\n')

    def exit(self):
        self._transport.end()

    def ready(self):
        return self._transport.ready()

    def verbose(self):
        self._transport.verbose()

    def debug(self):
        self._transport.debug()

    def quiet(self):
        self._transport.quiet()

    def _make_payload(self, klass, **fields):
        if not self.ready():
            return

        obj = klass()
        fieldNames = [x.camelcase_name for x in klass.DESCRIPTOR.fields]

        for name, value in fields.items():
            if name not in fieldNames:
                logger.warning(
                        'Skipping {} as it does not belong to: {}'.format(
                            name, fieldNames))
                continue
            try:
                setattr(obj, name, value)
                logger.info('{} = {}'.format(name, value))
            except TypeError as e:
                logger.error('Wrong type for {}: {}'.format(name, e))
            except Exception as e:
                logger.error('Cannot set field {}: {}'.format(name, e))

        payload = obj.SerializeToString()

        logger.debug("Payload = {}".format(payload))

        return payload

    def set_modem_config(self, **fields):
        klass = rfquack_pb2.ModemConfig
        payload = self._make_payload(klass, **fields)
        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_SET,
                    topics.TOPIC_MODULE_DRIVER,
                    topics.TOPIC_MODEM_CONFIG)),
                payload=payload)

    def set_mode(self, mode, repeat=0):
        if not self.ready():
            return

        logger.debug('Setting mode to {}'.format(mode))

        try:
            rfquack_pb2.Mode.Value(mode)
        except ValueError:
            logger.warning(
                'No such mode "{}": '
                'please select any of {}'.
                format(mode, rfquack_pb2.Mode.keys()))
            return

        status = rfquack_pb2.Status()
        status.mode = rfquack_pb2.Mode.Value(mode)
        status.tx_repeat_default = repeat

        payload = status.SerializeToString()
        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_SET,
                    topics.TOPIC_MODULE_DRIVER,
                    topics.TOPIC_STATUS,
                )),
                payload=payload)

        self._mode = mode

    def reset(self):
        if not self.ready():
            return

        logger.debug('Resetting the radio')

        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_UNSET,
                    topics.TOPIC_MODULE_DRIVER,
                    topics.TOPIC_MODEM_CONFIG)),
                payload=b'')

        self._mode = 'IDLE'  # don't send the idle command, just pretend

    def rx(self):
        self.set_mode('RX')

    def tx(self):
        self.set_mode('TX')

    def idle(self):
        self.set_mode('IDLE')

    def repeat(self, repeat=0):
        self.set_mode('REPEAT', repeat)

    def get_status(self):
        if not self.ready():
            return

        logger.debug('Getting status')

        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_UNSET,
                    topics.TOPIC_MODULE_DRIVER,
                    topics.TOPIC_MODEM_CONFIG)),
                payload=b'')

    def set_register(self, addr, value):
        if not self.ready():
            return

        logger.debug('Setting value of register 0x{:02X} = 0b{:08b}'.format(
            addr, value))

        register = rfquack_pb2.Register()
        register.address = addr
        register.value = value

        payload = register.SerializeToString()
        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_SET,
                    topics.TOPIC_MODULE_DRIVER,
                    topics.TOPIC_REGISTER)),
                payload=payload)

    def get_register(self, addr):
        if not self.ready():
            return

        logger.debug('Getting value of register 0x{:02X}'.format(addr))

        register = rfquack_pb2.Register()
        register.address = addr

        payload = register.SerializeToString()
        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_GET,
                    topics.TOPIC_MODULE_DRIVER,
                    topics.TOPIC_REGISTER)),
                payload=payload)

    def set_packet(self, data, repeat=1, delayMs=None):
        if not self.ready():
            return

        packet = rfquack_pb2.Packet()
        packet.data = data

        if isinstance(delayMs, int):
            packet.delayMs = delayMs

        try:
            packet.repeat = int(repeat)
        except Exception as e:
            logger.warning('Cannot set repeat of packet: {}'.format(e))

        payload = packet.SerializeToString()
        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_SET,
                    topics.TOPIC_MODULE_DRIVER,
                    topics.TOPIC_PACKET)),
                payload=payload)

    send = set_packet

    def reset_packet_modifications(self):
        """
        Reset any packet modification.
        """
        if not self.ready():
            return

        logger.debug('Resetting packet modifications')

        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_UNSET,
                    topics.TOPIC_MODULE_PACKET_MODIFICATION,
                    topics.TOPIC_RULES
                )),
                payload=b'')

    def get_packet_modifications(self):
        """
        Get list of packet modifications
        """
        if not self.ready():
            return

        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_GET,
                    topics.TOPIC_MODULE_PACKET_MODIFICATION,
                    topics.TOPIC_RULES
                )),
                payload=b'')

    def add_packet_modification(self, **fields):
        klass = rfquack_pb2.PacketModification
        payload = self._make_payload(klass, **fields)
        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_SET,
                    topics.TOPIC_MODULE_PACKET_MODIFICATION,
                    topics.TOPIC_RULES
                )),
                payload=payload)

    def reset_packet_filters(self):
        """
        Reset any packet filter.
        """
        if not self.ready():
            return

        logger.debug('Resetting packet filters')

        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_UNSET,
                    topics.TOPIC_MODULE_PACKET_FILTER,
                    topics.TOPIC_RULES
                )),
                payload=b'')

    def get_packet_filters(self):
        """
        Get list of packet filters
        """
        if not self.ready():
            return

        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_GET,
                    topics.TOPIC_MODULE_PACKET_FILTER,
                    topics.TOPIC_RULES
                )),
                payload=b'')

    def add_packet_filter(self, **fields):
        klass = rfquack_pb2.PacketFilter
        payload = self._make_payload(klass, **fields)
        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_SET,
                    topics.TOPIC_MODULE_PACKET_FILTER,
                    topics.TOPIC_RULES
                )),
                payload=payload)

    def set_packet_format(self, **fields):
        klass = rfquack_pb2.PacketFormat
        payload = self._make_payload(klass, **fields)
        self._transport._send(
                command=topics.TOPIC_SEP.join((
                    topics.TOPIC_SET,
                    topics.TOPIC_PACKET_FORMAT)),
                payload=payload)
