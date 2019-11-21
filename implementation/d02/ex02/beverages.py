#!/usr/bin/env python3
# -*-coding:utf-8 -*-

class HotBeverage:
	"""Hot Beverage class"""
	desc = "Just some hot water in a cup."

	def __init__(self, price=0.30, name="hot beverage"):
		self.price = price
		self.name = name

	def __str__(self):
		return self.name

	@property
	def description(self):
		return self.desc

	def __str__(self):
		return "name : {0}\nprice : {1}\ndescription : {2}".format(self.name, '%.2f' % self.price, self.description)

class Coffee(HotBeverage):
	"""Coffee"""
	desc = "A coffee, to stay awake."
	def __init__(self):
		HotBeverage.__init__(self, price=0.40, name="coffee")

class Tea(HotBeverage):
	"""Tea"""
	desc = "Just some hot water in a cup."
	def __init__(self):
		 HotBeverage.__init__(self, name="tea")

class Chocolate(HotBeverage):
	"""Chocolate"""
	desc = "Chocolate, sweet chocolate..."
	def __init__(self):
		HotBeverage.__init__(self, price=0.50, name="chocolate")

class Cappuccino(HotBeverage):
	"""Cappuccino"""
	desc = "Un po’ di Italia nella sua tazza!"
	def __init__(self):
		HotBeverage.__init__(self, price=0.45, name="cappuccino")


if __name__ == "__main__":
	hot_bev_instance = HotBeverage()
	print(hot_bev_instance)
	coffee_instance = Coffee()
	print(coffee_instance)
	tea_instance = Tea()
	print(tea_instance)
	chocolate_instance = Chocolate()
	print(chocolate_instance)
	cappuccino_instance = Cappuccino()
	print(cappuccino_instance)
