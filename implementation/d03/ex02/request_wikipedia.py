#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
import requests
from dewiki import parser


def usage():
	print('Usage: python3 request_wikipedia.py "<search key words>"')


def parse_response(resp):
	pages = resp["query"]["pages"]
	revisions_position = None
	for _, page in pages.items():
		revisions_position = page.get("revisions")
		if revisions_position is None:
			print("Nothing has been found by your request")
			exit(1)
	# print(revisions_position)
	my_parser = parser.Parser()
	good = revisions_position[0]['*']
	to_write = my_parser.parse_string(good)
	return to_write


def search_in_wiki(search_str):
	try:
		link = 'https://en.wikipedia.org/w/api.php'
		query_params = {
			'action': 'query',
			'titles': search_str,
			'prop': 'revisions',
			'rvprop': 'content',
			'format': 'json'
		}
		resp = requests.get(link, params=query_params)
		if not resp.ok:
			exit("Error {} :: {}".format(resp.status_code, resp.reason))
		# print(resp.text)
		response_json = json.loads(resp.text)
		if 'error' in response_json.keys():
			print("Error in response: {}".format(response_json['error']['info']))
			exit(1)
		if 'query' not in response_json.keys():
			print("Nothing has been found by your request")
			exit(1)
		parsed_str = parse_response(response_json)
		with open(search_str.replace(' ', '_') + '.wiki', 'w') as fd:
			fd.write(parsed_str)
	except Exception as e:
		print(e)


def analyze_output__do():
	if len(sys.argv) == 2:
		search_in_wiki(sys.argv[1])
	else:
		print('Error: put exactly one argument or take few arguments in quotes')
		usage()


if __name__ == '__main__':
	analyze_output__do()

# python3 -m venv venv/
# source venv/bin/activate
# pip install -r requirement.txt

# pip freeze > requirement.txt
