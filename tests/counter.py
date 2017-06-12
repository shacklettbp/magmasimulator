import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(4):
    icestick.J1[i].input().on()
    icestick.J3[i].output().on()

icestick.D1.on()

main = icestick.main()

update_counter = Counter(10)
counter = Counter(4, ce=True)
wire(update_counter.COUT, counter.CE)

wire(counter.COUT, main.D1)
wire(counter.O, main.J3)


compile(sys.argv[1], main, sys.argv[2])
