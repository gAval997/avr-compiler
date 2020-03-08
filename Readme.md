# Atmel uC compiler simplifier
###### Author: Hector Gerardo Avalos
#

### Pre-requisites:
##### Linux installation (Ubuntu 18.04)
* sudo apt install build-essential binutils gcc-avr avr-libc uisp flex bison byacc

### Usage:
avr-compile.py --source blink.c --micro atmega32a

#### Examples:
avr-compile.py --source rotabit.c --micro atmega32a
avr-compile.py --source rotabit.c --micro atmega8 --output rotabit

### Output
This compiler produces
*.o file
*.elf file
*.hex file
