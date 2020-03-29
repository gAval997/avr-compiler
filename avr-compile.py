#!/usr/bin/env python3
__author__ = "Hector Gerardo Avalos"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Hector Gerardo Avalos"
__email__ = "gerardo.avalos97@hotmail.com"
__status__ = "Production"

import argparse


def get_instruction_set(operating_system):
	import json

	instruction_set = {}

	try:
		with open("instruction_set.jso") as fp:
			lines = fp.read()
			instructions = json.loads(lines)

			if operating_system == "Linux":
				instruction_set = { name:instr for (name, instr) in instructions["Linux"].items() }
			else:
				instruction_set = { name:instr for (name, instr) in instructions["Windows"].items() }
	except:
		print("Instructions not found, using fallback values...")
	return instruction_set


def fallback_instruction_set(operating_system):
	instruction_set = {}

	if operating_system == "Linux":
		instruction_set["c_to_obj"] = './avr8-gnu-toolchain-linux/bin/avr-gcc -g -Os -mmcu={MICROCONTROLLER} -c {SOURCEFILEPATH}{SOURCEFILE}.c'
		instruction_set["obj_to_elf"] = './avr8-gnu-toolchain-linux/bin/avr-gcc -g -mmcu={MICROCONTROLLER} -o {SOURCEFILEPATH}{SOURCEFILE}.elf {SOURCEFILEPATH}{SOURCEFILE}.o'
		instruction_set["elf_to_hex"] = './avr8-gnu-toolchain-linux/bin/avr-objcopy -j .text -j .data -O ihex {SOURCEFILEPATH}{SOURCEFILE}.elf {SOURCEFILEPATH}{OUTPUTFILE}.hex'
		instruction_set["get_filesize"] = './avr8-gnu-toolchain-linux/bin/avr-size --format=avr --mcu={MICROCONTROLLER} {SOURCEFILEPATH}{SOURCEFILE}.elf'
		instruction_set["mv_obj_to_srcpath"] = 'mv ./{SOURCEFILE}.o {SOURCEFILEPATH}'
	else:
		instruction_set["c_to_obj"] = './avr8-gnu-toolchain-win32/bin/avr-gcc.exe -g -Os -mmcu={MICROCONTROLLER} -c {SOURCEFILEPATH}{SOURCEFILE}.c'
		instruction_set["obj_to_elf"] = './avr8-gnu-toolchain-win32/bin/avr-gcc.exe -g -mmcu={MICROCONTROLLER} -o {SOURCEFILEPATH}{SOURCEFILE}.elf {SOURCEFILEPATH}{SOURCEFILE}.o'
		instruction_set["elf_to_hex"] = './avr8-gnu-toolchain-win32/bin/avr-objcopy.exe -j .text -j .data -O ihex {SOURCEFILEPATH}{SOURCEFILE}.elf {SOURCEFILEPATH}{OUTPUTFILE}.hex'
		instruction_set["get_filesize"] = './avr8-gnu-toolchain-win32/bin/avr-size.exe --format=avr --mcu={MICROCONTROLLER} {SOURCEFILEPATH}{SOURCEFILE}.elf'
		instruction_set["mv_obj_to_srcpath"] = 'move {SOURCEFILE}.o {SOURCEFILEPATH}'
	return instruction_set


def do_compile(sourceFile, microcontroller, outputFile):
	import os
	import platform

	source_file_location = os.path.abspath(sourceFile)
	source_file_path, sourceFile = os.path.split(source_file_location)
	source_file_path = "{}/".format(os.path.dirname(source_file_location))
	sourceFile = sourceFile[0:-2] # Removes .c extension
	instruction_set = {};

	if not outputFile:
		outputFile = sourceFile

	instruction_set = get_instruction_set(platform.system())
	if len(instruction_set.items()) == 0:
		instruction_set = fallback_instruction_set(platform.system())

	print(
		instruction_set["c_to_obj"].format(
			MICROCONTROLLER=microcontroller,
			SOURCEFILEPATH=source_file_path,
			SOURCEFILE=sourceFile
		)
	)

	print(
		instruction_set["mv_obj_to_srcpath"].format(
			SOURCEFILE=sourceFile,
			SOURCEFILEPATH=source_file_path
		)
	)

	print(
		instruction_set["obj_to_elf"].format(
			MICROCONTROLLER=microcontroller,
			SOURCEFILEPATH=source_file_path,
			SOURCEFILE=sourceFile
		)
	)

	print(
		instruction_set["elf_to_hex"].format(
			SOURCEFILE=sourceFile,
			SOURCEFILEPATH=source_file_path,
			OUTPUTFILE=outputFile
		)
	)

	print(
		instruction_set["get_filesize"].format(
			MICROCONTROLLER=microcontroller,
			SOURCEFILEPATH=source_file_path,
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
