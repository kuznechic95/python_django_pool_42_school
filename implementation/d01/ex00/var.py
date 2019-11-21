#!/usr/bin/env python3
# -*-coding:utf-8 -*

def print_val_and_type(val):
	print("{0} est de type {1}".format(val, type(val)))

def my_var():
	""" function prints values and its' type """
	print_val_and_type(42)
	print_val_and_type("42")
	print_val_and_type("quarante-deux")
	print_val_and_type(42.0)
	print_val_and_type(True)
	print_val_and_type([42])
	print_val_and_type({42: 42})
	print_val_and_type((42,))
	print_val_and_type(set())
	
if __name__ == '__main__' :
    my_var()