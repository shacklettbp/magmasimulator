import sys
from magma import *
from mantle import *
from boards.icestick import IceStick
from parts.lattice.ice40.primitives.RAMB import *

icestick = IceStick()
icestick.Clock.on()
for i in range(4):
    icestick.J1[i].input().on()
    icestick.J3[i].output().on()

main = icestick.main()

ram = SB_RAM40_4K()

#wire(ram, main.J3)

compile(sys.argv[1], main)
