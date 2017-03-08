import sys
from parts.lattice.ice40.primitives.PLB import SB_CARRY
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(4):
    icestick.J1[i].input().on()

icestick.D1.on()

main = icestick.main()

carry = SB_CARRY()
carry(main.J1[0], main.J1[1], main.J1[2]);
 
wire(carry, main.D1)


compile(sys.argv[1], main, sys.argv[2])
