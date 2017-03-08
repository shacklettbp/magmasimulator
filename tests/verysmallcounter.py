import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(4):
    icestick.J1[i].input().on()

icestick.D1.on()
icestick.D2.on()

main = icestick.main()

counter = Counter(2, cout=False)

wire(counter.O[0], main.D1)
wire(counter.O[1], main.D2)


compile(sys.argv[1], main, sys.argv[2])
