import sys
from magma import *
from mantle import *
from boards.icestick import IceStick
from parts.lattice.ice40.primitives.RAMB import *

icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J1[i].input().on()

icestick.D1.on()
icestick.D2.on()
icestick.D3.on()
icestick.D4.on()

main = icestick.main()

N = 16
M = 4096//N
rom = [0]*M
for i in range(M):
    rom[i] = i & 0xffff
ram = RAMB(rom)

# read
wire(main.CLKIN, ram.RCLK)
wire(True, ram.RCLKE)
wire(True, ram.RE)
# write
wire(main.CLKIN, ram.WCLK)
wire(True, ram.WCLKE)
wire(True, ram.WE)

# read/write addresses
opp1 = False
for i in range(8):
    opp1 = not opp1
    wire(opp1, ram.RADDR[i])
    wire(opp1, ram.WADDR[i])
# write data input
opp2 = False
for i in range(16):
    opp2 = not opp2
    wire(opp2, ram.WDATA[i])

# read data output
lut4_0 = LUT4(I0&I1&I2&I3)
lut4_0(ram.RDATA[0], ram.RDATA[1], ram.RDATA[2], ram.RDATA[3])

lut4_1 = LUT4(I0&I1&I2&I3)
lut4_1(ram.RDATA[4], ram.RDATA[5], ram.RDATA[6], ram.RDATA[7])

lut4_2 = LUT4(I0&I1&I2&I3)
lut4_2(ram.RDATA[8], ram.RDATA[9], ram.RDATA[10], ram.RDATA[11])

lut4_3 = LUT4(I0&I1&I2&I3)
lut4_3(ram.RDATA[12], ram.RDATA[13], ram.RDATA[14], ram.RDATA[15])

wire(lut4_0, main.D1)
wire(lut4_1, main.D2)
wire(lut4_2, main.D3)
wire(lut4_3, main.D4)

compile(sys.argv[1], main)
