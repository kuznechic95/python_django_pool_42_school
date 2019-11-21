#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys


def main():
	if len(sys.argv) != 2:
		exit("Usage: python3 roads_to_philosophy.py string_to_find")

	string_to_find = sys.argv[1]

	if string_to_find == "Philosophy":
		print("0 roads from Philosophy to philosophy !")
		exit(0)
	nexturl = "http://en.wikipedia.org/wiki/" + string_to_find

	visited = []
	i = 0
	try:
		while True:
			i += 1
			req = requests.get(nexturl)

			if req.status_code != 200 or not req:
				exit("Something wrong with Server")

			if not req.text:
				exit(f"Can't find {string_to_find}")

			soup = BeautifulSoup(req.text, 'html.parser')
			article = soup.findAll('h1', {'class': 'firstHeading'})[0].contents[0]
			print(article)

			if article == "Philosophy":
				break
			maincontent = soup.findAll("div", {"class": "mw-parser-output"})[0]
			paragraphs = maincontent.findAll('p')
			next_url_found = False
			for paragraph in paragraphs:
				if not next_url_found:
					parenthesis_in_progress = False
					for thing in paragraph.contents:
						if not next_url_found:
							if "(" in thing:
								parenthesis_in_progess = True
							if ")" in thing and parenthesis_in_progress:
								parenthesis_in_progress = False

							if not parenthesis_in_progress:
								if not isinstance(thing, str):
									try:
										n = thing['href']
										if not n in visited:
											next_url_found = True
											nexturl = n
											visited.append(nexturl)
										else:
											exit("It leads to an infinite loop ! ")
									except:
										pass

			nexturl = "http://en.wikipedia.org" + nexturl

		print("{} roads from {} to Philosophy !".format(i, string_to_find))
	except:
		exit("It leads to a dead end!")


if __name__ == '__main__':
	main()