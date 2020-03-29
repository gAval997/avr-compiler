# Atmel uC compiler simplifier
###### Author: Hector Gerardo Avalos

## Pre-requisites:
##### Linux installation (Ubuntu 18.04)
`sudo apt install build-essential binutils gcc-avr avr-libc uisp flex bison byacc`

### Usage:
`avr-compile.py -s/--source -m/--micro [-o/--output]`

## Examples:
`avr-compile.py --source example.c --micro atmega32a`
`avr-compile.py --source example.c --micro atmega8 --output example_output`

### Output
###### This compiler produces the following files, in the same directory where the *.c source code file is located.
* *.o file
* *.elf file
* *.hex file
