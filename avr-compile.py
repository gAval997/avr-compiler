#!/usr/bin/env python3
__author__ = "Hector Gerardo Avalos"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Hector Gerardo Avalos"
__email__ = "gerardo.avalos97@hotmail.com"
__status__ = "Production"

import argparse


def do_compile(sourceFile, microcontroller, outputFile):
	import os
	sourceFile = sourceFile[0:-2] # Removes .c extension
	if not outputFile:
		outputFile = sourceFile

	os.system(
		'avr-gcc -g -Os -mmcu={MICROCONTROLLER} -c {SOURCEFILE}.c'
		.format(
			MICROCONTROLLER=microcontroller,
			SOURCEFILE=sourceFile
		)
	)

	os.system(
		'avr-gcc -g -mmcu={MICROCONTROLLER} -o {SOURCEFILE}.elf {SOURCEFILE}.o'
		.format(
			MICROCONTROLLER=microcontroller,
			SOURCEFILE=sourceFile
		)
	)

	os.system(
		'avr-objcopy -j .text -j .data -O ihex {SOURCEFILE}.elf {OUTPUTFILE}.hex'
		.format(
			SOURCEFILE=sourceFile,
			OUTPUTFILE=outputFile
		)
	)

	os.system(
		'avr-size --format=avr --mcu={MICROCONTROLLER} {SOURCEFILE}.elf'
		.format(
			MICROCONTROLLER=microcontroller,
			SOURCEFILE=sourceFile
		)
	)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description='Compile *.c into *.hex file for atmel devices'
	)
	parser.add_argument(
		'-s', '--source',
		required=True
	)
	parser.add_argument(
		'-m', '--micro',
		required=True
	)
	parser.add_argument(
		'-o', '--output'
	)
	args = parser.parse_args()

	do_compile(
		args.source,
		args.micro,
		args.output,
	)
