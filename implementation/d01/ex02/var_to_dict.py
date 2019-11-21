#!/usr/bin/env python3
# -*-coding:utf-8 -*

def var_to_dyc():
	""" transforms list of tuples to inverted dictionary"""
	d = [
		('Hendrix', '1942'),
		('Allman', '1946'),
		('King', '1925'),
		('Clapton', '1945'),
		('Johnson', '1911'),
		('Berry', '1926'),
		('Vaughan', '1954'),
		('Cooder', '1947'),
		('Page', '1944'),
		('Richards', '1943'),
		('Hammett', '1962'),
		('Cobain', '1967'),
		('Garcia', '1942'),
		('Beck', '1944'),
		('Santana', '1947'),
		('Ramone', '1948'),
		('White', '1975'),
		('Frusciante', '1970'),
		('Thompson', '1949'),
		('Burton', '1939')
	]
	new_dict = {}
	for name, year in d:
		list_of_names_already_to_this_year = new_dict.setdefault(year, [])
		list_of_names_already_to_this_year.append(name)
	for key, value in new_dict.items():
		print("{} : {}".format(key, " ".join(value)))

if __name__ == '__main__':
	var_to_dyc()