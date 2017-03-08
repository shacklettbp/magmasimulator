Magma Python Simulator:

Peter Do (peterhdo) & Brennan Shacklett (bps)

github.com/shacklettbp/magmasimulator

Goals & Motivation:

We want to create a python simulator for the Magma project,
to aid in debugging and testing of hardware designs in Magma. In its current
iteration, Magma makes writing the first pass of a design fairly straightforward
in comparison to Verilog. However, only simulation or debugging tools available
operate on the Verilog that Magma outputs. Unfortunately, this Verilog loses
many of the abstractions and naming of the original Magma code, so it is
difficult to extract useful information from a simulator. In addition, debugging
Verilog can result in an extra layer of complexity that we hope to avoid.
Therefore, we feel that the addition of a simulator to Magma will allow for
debugging and testing in a convenient python environment, which will improve the
utility of magma for rigorous and more rapid testing and prototyping.

Deliverables:

We plan on having a working Magma python simulator for Ice40
hardware at the conclusion of this project. It will be forked from the existing
Magma codebase and will theoretically work seamlessly should users want to debug
existing hardware designs created with Magma.  As part of the simulator, we plan
to implement a simple debugger that allows stepping through clock cycles and
examining register and possibly wire values. If given enough time we could also
potentially extend this into a visual debugger, but that depends on how long it
takes to get the base simulator to work. 

Significance:

If Magma were to have a python simulator built-in, it would allow
for easier hardware design for existing users. In addition, individuals
interested in starting to learn about hardware design would have an easier
time understanding what’s happening behind-the-scenes if they had access to a
simulator with a debugger. Debugging is an essential element to software
development, and it would be incredibly helpful to be able to debug the
hardware we design as well.

Inspiration:

PyMTL shows that having a host language simulator is a very useful
and possibly even essential tool when designing hardware.  There is also a large
body of work on high performance simulators for hardware, but our project will
be more geared towards debugging and testing than performance.  Logic analyzers
have proven to be useful in hardware design, so having a simulator at the python
level would hopefully help in a similar manner.

Resources:

We plan on discussing our plan and any issues that arise with Pat
Hanrahan. We’ll be working very closely with the existing Magma codebase, so we
will use that as a resource to develop the simulator.

Project Plan:

The final result we hope to achieve is a working magma python
simulator.  The first step of the project will involve simulating the output of
a very simple test program that simply toggles one of the Icestick’s output bits
in time with the clock. This will allow us to delve into magma’s wiring
architecture without needing to yet worry about more complicated primitives like
registers. We plan to finish this step within a week, since it will mostly
involve familiarizing ourselves with magma in order to build a wiring dependency
graph.  The next step will be simulating the SB_LUT4 primitive of the Icestick,
which combined with wiring simulation should allow us to simulate combinational
magma programs.  The final steps for the simulator will be simulating flip
flops, and then creating an interface so the state of the simulation can be
examined. The initial version of the debugger will simply be a python console,
with functions to advance the clock and examine the values of inputs and
outputs. Ideally this will be finished before the preliminary project
presentation, but we may present a combinational only simulator depending on
time constraints.  Extending the simulator into a more full featured debugger
will be the last part of our project, which we will work on after the
presentation.

Division of Responsibility:

We plan to use pair programming when working on the
project, so all parts of the project will be worked on by both of us.
