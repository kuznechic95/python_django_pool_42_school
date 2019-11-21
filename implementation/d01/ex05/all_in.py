#!/usr/bin/env python3
# -*-coding:utf-8 -*

def normalize_args(arg_str):
	""":returns arg list from arg string, separated by comma"""
	arg_list = [item for item in arg_str.split(',')]
	arg_list = [item.lstrip().rstrip() for item in arg_list \
		if not item.isspace()]
	# print(arg_list)
	return arg_list

def reverse_dict(initial_dictionary):
	""":returns  reversed dictionary"""
	return dict([[v, k] for k, v in initial_dictionary.items()])

def all_in(*argv):
	""":returns string (contains phrase what is the arg) for every arg"""
	import sys
	states = {
		"Oregon":"OR",
		"Alabama":"AL",
		"New Jersey":"NJ",
		"Colorado":"CO"
	}
	capital_cities = {
		"OR":"Salem",
		"AL":"Montgomery",
		"NJ":"Trenton",
		"CO":"Denver"
	}
	if len(sys.argv) != 2:
		sys.exit(1)
	argument_str = normalize_args(sys.argv[1])

	rev_states = reverse_dict(states)
	rev_cities = reverse_dict(capital_cities)

	for item in argument_str:
		if item.title() in states:
			print("{0} is the capital of {1}".\
				format(capital_cities[states[item.title()]], item.title()))
		elif item.title() in rev_cities:
			print("{0} is the capital of {1}".\
				format(item.title(), rev_states[rev_cities[item.title()]]))
		else:
			print("{0} is neither a capital city nor a state".format(item))

if __name__ == '__main__':
	import sys
	all_in(sys.argv)