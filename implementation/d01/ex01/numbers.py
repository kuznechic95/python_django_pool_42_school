#!/usr/bin/env python3
# -*-coding:utf-8 -*

def numbers():
	""" function reads whole file 'numbers.txt'.
		String from file content splits by ','.
		List of partitioned strings strips
		(removes whitespace characters from the beginning and the end of the string )
		and prints"""
	with open("numbers.txt", "r") as file:
		numbers = file.read().split(",")
		for elem in numbers:
			print(elem.strip())

if __name__ == '__main__':
	numbers()