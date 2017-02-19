from src.Parser import Parse
from src.Preproccess import Proccessor
import sys

args = sys.argv
try:
	command = args[1]
	if(command == 'parse'):
		instance = Parse()
		instance.proccess_urls()

	elif(command == 'create_indexes'):
		instance = Proccessor()
		instance.structurize_data()
		
except IndexError:
	print 'Command must be set'
	print 'Available commands: parse, create_indexes'