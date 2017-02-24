import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.D1.on()
icestick.D2.on()
icestick.D3.on()
icestick.D4.on()
icestick.D5.on()

main = icestick.main()

wire(main.CLKIN, main.D1)
wire(0, main.D2)
wire(0, main.D3)
wire(0, main.D4)
wire(0, main.D5)


compile(sys.argv[1], main, sys.argv[2])
