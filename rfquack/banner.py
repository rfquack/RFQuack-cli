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

BANNER = """

                   ,-.
               ,--' ~.).
             ,'         `.
            ; (((__   __)))      welcome to rfquack!
            ;  ( (#) ( (#)
            |   \_/___\_/|              the versatile
           ,"  ,-'    `__".             rf-hacking tool that quacks!
          (   ( ._   ____`.)--._        _
           `._ `-.`-' \(`-'  _  `-. _,-' `-/`.
            ,')   `.`._))  ,' `.   `.  ,','  ;   ~~~
          .'  .     `--'  /     ).   `.      ;
         ;     `-        /     '  )         ;           ~~~~
         \                       ')       ,'    ~~  ~
          \                     ,'       ;           ~~
           \               `~~~'       ,'               ~~~  ~~    ~~~~~
            `.                      _,'             ~~~
        hjw   `.                ,--'
        ~~~~~~~~`-._________,--'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ------------------------------------------------------------------------

        > q.set_modem_config(               # set modem configuration
            modemconfigchoiceindex=0,       # see radiohal documentation
            txpower=14,                     # tx output power in db
            syncwords=b'\\x43\\x42',        # sync words
            carrierfreq=433)                # and of course, carrier frequency

        > q.set_packet('\\x0d\\xa2', 13)    # transmit '0xd 0xa2' 13 times

        > q.set_modem_config(               # set modem configuration
            modemconfigchoiceindex=0,       # see radiohal documentation
            txpower=14,                     # tx output power in db
            syncwords='',                   # disable sync-word matching
            carrierfreq=433)                # and of course, carrier frequency

                                            # example: with rfm69
                                            # -------------------
        > q.set_register(                   #  truly promiscuous mode:
            0x2e,                           #  1) set register 0x2e
            0b01000000                      #     to 0b01000000
            )                               #
        > q.set_register(                   #
            0x37,                           #  2) set register 0x37
            0b01000000                      #     to 0b11000000
            )

        > q.add_packet_filter(              # ignore packets
            pattern="^ab[cd]"               # not matching this regex
        )

        > q.add_packet_modification(        # modify packets as follows:
            pattern="[ke]$",                #  if they end with 'k' or 'e'
            position=3,                     #  at position = 3 in the payload
            content=b'\\x29',               #  and position = indexof(0x29)
            operation=2                     #  content[position] |= 0x25
            operand=b'\\x25'
        )

        > q.repeat(10)                      # stay in rx and
                                            # modify each matching packet
                                            # transmit the result 10 times

        > q.reset_packet_modifications()
                                        # clear all packet modifications

        help:
        > q.set_mode?                # tab is your friend

        exit:   just type ctrl-d a couple of times!
"""
