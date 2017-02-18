from src.Parser import Parse
import sys

args = sys.argv
try:
	command = args[1]
	if(command == 'parse'):
		instance = Parse()
		instance.proccess_urls()

except IndexError:
	print 'Command must be set'
	print 'Available commands: parse'