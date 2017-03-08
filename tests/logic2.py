import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(4):
    icestick.J1[i].input().on()

icestick.D1.on()

main = icestick.main()

andy = And2()
andy(main.J1[1], 1)

lut4 = LUT4(I0&I1&I2&I3)
lut4(main.J1[0], main.J1[0], andy, main.J1[3]);
 
wire(lut4, main.D1)


compile(sys.argv[1], main, sys.argv[2])
