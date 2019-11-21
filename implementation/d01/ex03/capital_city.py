#!/usr/bin/env python3
# -*-coding:utf-8 -*

def find_capital_by_state(*argv):
	""":returns str that contains capital name or phrase 'Unknown state'"""
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
	state = sys.argv[1]
	result_str = "Unknown state"
	if state in states:
		state_abbreviation = states[state]
		if state_abbreviation in capital_cities:
			result_str = capital_cities[state_abbreviation]
	print(result_str)

if __name__ == '__main__':
	import sys
	find_capital_by_state(sys.argv)