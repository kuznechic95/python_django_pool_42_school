# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import antigravity
import sys

def usage():
	print('Put the arguments in one of the next forms:\n'
	      '<latitude> <longitude> <date in the format yyyy-mm-dd> <most recent opening value for the DJIA>\n'
	      '<latitude> <longitude> <date in the format yyyy-mm-dd>-<most recent opening value for the DJIA>')
	sys.exit(1)


def calculate_geohash(latitude, longitude, date_index):
	"""calculates geohash"""
	# print(latitude, longitude, date_index, type(date_index.encode()))
	antigravity.geohash(latitude, longitude, date_index.encode())


def geohashing():
	"""parses arguments and sends to calculate_geohash"""
	arg_num = len(sys.argv) - 1
	# print(arg_num)
	if arg_num == 4:
		try:
			latitude = float(sys.argv[1])
			longitude = float(sys.argv[2])
			date = sys.argv[3]
			index = float(sys.argv[4])
			date_index = date + "-" + str(index)
			calculate_geohash(latitude, longitude, date_index)
		except ValueError as e:
			print("Error while parsing arguments. Error description: {}".format(e))
			usage()
		except Exception as e:
			print("An unknown error occurred. Error description: {}".format(e))
			usage()
	elif arg_num == 3:
		try:
			latitude = float(sys.argv[1])
			longitude = float(sys.argv[2])
			possible_date_index = sys.argv[3]
			date = possible_date_index[:10]
			index = float(possible_date_index[11:])
			# print('date={}, index={}'.format(date, index))
			date_index = date + "-" + str(index)
			calculate_geohash(latitude, longitude, date_index)
		except ValueError as e:
			print("Error while parsing arguments. Error description: {}".format(e))
			usage()
		except Exception as e:
			print("An unknown error occurred. Error description: {}".format(e))
			usage()
	else:
		usage()


if __name__ == '__main__':
	geohashing()
# python3 geohashing.py 50.468964 30.462287 2019-11-07-27590.16
# python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68