import os
import argparse
import importlib



class Parsers:

	def __init__(self, *args, **kwargs):
		self.root = argparse.ArgumentParser(*args, **kwargs)
	
	def load(
		self, 
		main_module_name,
		subcommands, 
		subparsers_title='subparsers', 
		subcommands_module_name='subcommands'
	):

		subparsers = self.root.add_subparsers(title=subparsers_title)

		for c in subcommands:

			command_module = importlib.import_module(f'{main_module_name}.{subcommands_module_name}.{c}')
			
			command_parser = subparsers.add_parser(c, description=command_module.description)
			command_parser.set_defaults(handler=command_module.handler)
			
			keywords = command_module.args[0]
			for row in command_module.args[1:]:
				kwargs = {
					keywords[i]: row[i]
					for i in range(len(row))
				}
				names = kwargs['names']
				del kwargs['names']
				command_parser.add_argument(
					*names,
					**kwargs
				)
	
	def run(self):

		args = self.root.parse_args()
		
		return args.handler(args)



import sys
sys.modules[__name__] = Parsers