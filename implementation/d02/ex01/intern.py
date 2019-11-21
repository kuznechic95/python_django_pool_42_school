#!/usr/bin/env python3
# -*-coding:utf-8 -*-


class Intern:
	"""class Intern"""

	def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
		self._name = name

	def __str__(self):
		return self._name

	class Coffee:
		"""class Coffee"""
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")

	def make_coffee(self):
		return self.Coffee()


if __name__ == '__main__':
	first_intern_instance = Intern()
	print(first_intern_instance)
	second_intern_instance = Intern("Mark")
	print(second_intern_instance)
	coffee_made_by_second_trainee = second_intern_instance.make_coffee()
	print(coffee_made_by_second_trainee)
	try:
		print(first_intern_instance.work())
	except Exception as e:
		print(e)
