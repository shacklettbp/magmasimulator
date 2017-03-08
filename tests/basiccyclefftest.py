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

ff = DFF(ce=True)
n = Not()

ff(n)

wire(main.J1[0], ff.CE)
wire(ff, n)
 
wire(ff, main.D1)


compile(sys.argv[1], main, sys.argv[2])
