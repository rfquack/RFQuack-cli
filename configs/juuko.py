#  # Address Config = Address check, no broadcast 
#  # Bit Rate = 11.52 
#  # Carrier Frequency = 434.177490 
#  # Deviation = 2.395630 
#  # Device Address = a2 
#  # Manchester Enable = false 
#  # Modulation Format = 4-FSK 
#  # PA Ramping = true 
#  # Packet Bit Length = 0 
#  # Packet Length = 24 
#  # Packet Length Mode = Variable 
#  # Performance Mode = High Performance 
#  # RX Filter BW = 11.764706 
#  # Symbol rate = 5.76 
#  # TX Power = 0 
#  # Whitening = false 
#  
#  registers = [
#          (0x00, 0x58),  # IOCFG3
#          #(0x01, 0x46),  # IOCFG2 - this is Juuko default, but we loose the IRQs
#          (0x01, 0x54),  # IOCFG2
#          (0x02, 0x46),  # IOCFG1
#          (0x2F16, 0x40),  # FS_CAL1
#          (0x2F01, 0x22),  # FREQOFF_CFG
#          (0x08, 0x0B),  # SYNC_CFG1
#          (0x0A, 0x3A),  # DEVIATION_M
#          (0x0B, 0x22),  # MODCFG_DEV_E
#          (0x0C, 0x1C),  # DCFILT_CFG
#          (0x2F0D, 0x8B),  # FREQ1
#          (0x2F0E, 0x5C),  # FREQ0
#          (0x10, 0xC6),  # IQIC
#          (0x11, 0x11),  # CHAN_BW
#          (0x2F12, 0x00),  # FS_DIG1
#          (0x13, 0x05),  # MDMCFG0
#          (0x14, 0x67),  # SYMBOL_RATE2
#          (0x15, 0x97),  # SYMBOL_RATE1
#          (0x16, 0xCC),  # SYMBOL_RATE0
#          (0x17, 0x20),  # AGC_REF
#          (0x18, 0x19),  # AGC_CS_THR
#          (0x2F19, 0x03),  # FS_DIVTWO
#          (0x2F1B, 0x33),  # FS_DSM0
#          (0x1C, 0xA9),  # AGC_CFG1
#          (0x1D, 0xCF),  # AGC_CFG0
#          (0x1E, 0x00),  # FIFO_CFG
#          (0x1F, 0xA2),  # DEV_ADDR
#          (0x20, 0x03),  # SETTLING_CFG
#          (0x21, 0x14),  # FS_CFG
#          (0x2F22, 0xAC),  # FS_SPARE
#          (0x2F23, 0x13),  # FS_VCO4
#          (0x2F25, 0x4A),  # FS_VCO2
#          (0x26, 0x00),  # PKT_CFG2
#          (0x2F27, 0xB4),  # FS_VCO0
#          (0x28, 0x20),  # PKT_CFG0
#          (0x2B, 0x7F),  # PA_CFG2
#          (0x2D, 0x7E),  # PA_CFG0
#          (0x2E, 0x18),  # PKT_LEN
#          (0x2F1D, 0x17),  # FS_DVC0
#          (0x2F17, 0x0E),  # FS_CAL0
#          (0x2F32, 0x0E),  # XOSC5
#          (0x2F36, 0x03),  # XOSC1
#          (0x2F1F, 0x50),  # FS_PFD
#          (0x2F20, 0x6E),  # FS_PRE
#          (0x2F21, 0x14),  # FS_REG_DIV_CML
#          (0x2F0C, 0x6C),  # FREQ2
#          (0x2F18, 0x28),  # FS_CHP
#          (0x2F13, 0x5F),  # FS_DIG0
#          (0x2F00, 0x00)  # IF_MIX_CFG
#  ]
#  
#  modem_registers = [
#          (0x0A, 0x3A),  # DEVIATION_M
#          (0x0B, 0x22),  # MODCFG_DEV_E
#          (0x11, 0x11),  # CHAN_BW
#          (0x13, 0x05),  # MDMCFG0
#          (0x14, 0x67),  # SYMBOL_RATE2
#          (0x15, 0x97),  # SYMBOL_RATE1
#          (0x16, 0xCC),  # SYMBOL_RATE0
#          (0x2F01, 0x22),  # FREQOFF_CFG
#          (0x2F0C, 0x6C),  # FREQ2
#          (0x2F0D, 0x8A),  # FREQ1
#          (0x2F0E, 0xE1)  # FREQ0
#  ]
#  
#  # offset compensation
#  modem_registers = [
#          (0x0A, 0x3A),  # DEVIATION_M
#          (0x0B, 0x22),  # MODCFG_DEV_E
#          (0x11, 0x11),  # CHAN_BW
#          (0x13, 0x05),  # MDMCFG0
#          (0x14, 0x67),  # SYMBOL_RATE2
#          (0x15, 0x97),  # SYMBOL_RATE1
#          (0x16, 0xCC),  # SYMBOL_RATE0
#          (0x2F01, 0x22),  # FREQOFF_CFG
#          (0x2F0C, 0x6C),  # FREQ2
#          (0x2F0D, 0x8A),  # FREQ1
#          (0x2F0E, 0xE1)  # FREQ0
#  ]

# --------------------------------------------------------------------- #

# including sync words
import time

modem_registers = [
        (0x04, 0x93),    # SYNC3
        (0x05, 0x0B),    # SYNC2
        (0x06, 0x51),    # SYNC1
        (0x07, 0xDE),    # SYNC0
        (0x0A, 0x3A),    # DEVIATION_M
        (0x0B, 0x22),    # MODCFG_DEV_E
        (0x11, 0x11),    # CHAN_BW
        (0x13, 0x05),    # MDMCFG0
        (0x14, 0x67),    # SYMBOL_RATE2
        (0x15, 0x97),    # SYMBOL_RATE1
        (0x16, 0xCC),    # SYMBOL_RATE0
        (0x2F01, 0x22),  # FREQOFF_CFG
        (0x2F0C, 0x6C),  # FREQ2
        (0x2F0D, 0x8A),  # FREQ1
        (0x2F0E, 0xE1)   # FREQ0
]

for addr, value in modem_registers:
    q.set_register(addr, value)
    time.sleep(0.2)

#q.set_modem_config(txPower=10)

# q.rx()

# Command library
ESTOP = 0x18  # @7 @12
X1 = 0x01  # @8 @12
X2 = 0x02
X3 = 0x04
X4 = 0x08
X5 = 0x10
X6 = 0x20
X7 = 0x40
X8 = 0x80
XSTART1 = 0x20  # @7
XSTART2 = 0x01  # @12

# Packet modifications
# E-stop
# direction commands
CMD = X1
q.reset_packet_modifications()
q.add_packet_modification(position=8,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet
# x1 = q.set_packet('\xA2\xB7\xCC\xD9\x4A\xDC\x9D\x76\xEB\x94\x3C\xE6\x2E', 10)

CMD = X2
q.reset_packet_modifications()
q.add_packet_modification(position=8,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet
# x2 = q.set_packet('\xA2\xB4\xC9\xD1\x57\xC8\x8C\x7A\xD9\x84\x39\xEE\x23', 10)

CMD = X3
q.reset_packet_modifications()
q.add_packet_modification(position=8,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet
# x3 = q.set_packet('\xA2\x59\xA2\x05\x90\xAC\x9B\xD2\xAC\xB4\xC2\xCA\x8F', 10)

CMD = X4
q.reset_packet_modifications()
q.add_packet_modification(position=8,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet
# x4 = q.set_packet('\xA2\x68\x9D\x39\x5B\x68\x38\x62\x2F\x24\x1D\x16\x79', 10)

CMD = X5
q.reset_packet_modifications()
q.add_packet_modification(position=8,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet
# x5 = q.set_packet('\xA2\x1B\x60\x81\x2E\xAC\xD9\x6E\x76\xB4\x00\x4E\x97', 10)

CMD = X6
q.reset_packet_modifications()
q.add_packet_modification(position=8,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet
# x6 = q.set_packet('\xA2\xF6\x0F\x45\x85\xD8\x5A\xF6\x09\x94\xFF\x6A\x01', 10)

CMD = X7
q.reset_packet_modifications()
q.add_packet_modification(position=8,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet
# x7 = q.set_packet('\xA2\x1A\x63\x8D\x59\xB8\xE6\x7E\xC5\xD4\x23\x72\x91', 10)

CMD = X8
q.reset_packet_modifications()
q.add_packet_modification(position=8,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet
# x8 = q.set_packet('\xA2\x61\x9A\x35\x28\x0C\x23\x62\xB0\x34\x3A\x3A\xAB',10)

CMD = [XSTART1, XSTART2]
q.reset_packet_modifications()
q.add_packet_modification(position=7,  operand=CMD[0], operation=3)
q.add_packet_modification(position=10, operand=CMD[1], operation=3)
q.add_packet_modification(position=12, operand=CMD[0] + CMD[1], operation=3)
q.get_packet_modifications()
# example valid packet
# xstart = q.set_packet('\xA2\xFB\x00\x41\x8E\x2C\x79\x8E\x46\xB4\x21\x8E\x26',10)

CMD = ESTOP
q.reset_packet_modifications()
q.add_packet_modification(position=7,  operand=CMD, operation=3)
q.add_packet_modification(position=12, operand=CMD, operation=3)
q.get_packet_modifications()
# example valid packet:
# xstop = q.set_packet(' A2 21 5A B5 E8 0C 63 FA F0 34 7A BA 33',10)

def x1():      q.set_packet('\xA2\xB7\xCC\xD9\x4A\xDC\x9D\x76\xEB\x94\x3C\xE6\x2E', 30)
def x2():      q.set_packet('\xA2\xB4\xC9\xD1\x57\xC8\x8C\x7A\xD9\x84\x39\xEE\x23', 30)
def x3():      q.set_packet('\xA2\x59\xA2\x05\x90\xAC\x9B\xD2\xAC\xB4\xC2\xCA\x8F', 30)
def x4():      q.set_packet('\xA2\x68\x9D\x39\x5B\x68\x38\x62\x2F\x24\x1D\x16\x79', 30)
def x5():      q.set_packet('\xA2\x1B\x60\x81\x2E\xAC\xD9\x6E\x76\xB4\x00\x4E\x97', 30)
def x6():      q.set_packet('\xA2\xF6\x0F\x45\x85\xD8\x5A\xF6\x09\x94\xFF\x6A\x01', 30)
def x7():      q.set_packet('\xA2\x1A\x63\x8D\x59\xB8\xE6\x7E\xC5\xD4\x23\x72\x91', 30)
def x8():      q.set_packet('\xA2\x61\x9A\x35\x28\x0C\x23\x62\xB0\x34\x3A\x3A\xAB', 30)
def xstart():  q.set_packet('\xA2\xFB\x00\x41\x8E\x2C\x79\x8E\x46\xB4\x21\x8E\x26', 30)
def xstop():   q.set_packet('\xA2\x21\x5A\xB5\xE8\x0C\x63\xFA\xF0\x34\x7A\xBA\x33', 30)

def stop_start_x1(): xstop(); xstart(); x1();

fw = x1
bw = x2
up = x7
down = x6
