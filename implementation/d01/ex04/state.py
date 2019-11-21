#!/usr/bin/env python3
# -*-coding:utf-8 -*

def reverse_dict(initial_dictionary):
	""":returns  reversed dictionary"""
	return dict([[v, k] for k, v in initial_dictionary.items()])

def find_state_by_capital(*argv):
	""":returns str that contains state name or phrase 'Unknown capital city'"""
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
	capital_city = sys.argv[1]
	result_str = "Unknown capital city"
	rev_states = reverse_dict(states)
	rev_cities = reverse_dict(capital_cities)
	if capital_city in rev_cities:
		state_abbreviation = rev_cities[capital_city]
		if state_abbreviation in rev_states:
			result_str = rev_states[state_abbreviation]
	print(result_str)

if __name__ == '__main__':
	import sys
	find_state_by_capital(sys.argv)