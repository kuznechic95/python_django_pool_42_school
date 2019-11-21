#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
	"""CoffeeMachine class"""
	def __init__(self):
		self.count = 0

	class EmptyCup(HotBeverage):
		desc = "An empty cup?! Gimme my money back!"

		def __init__(self, price=0.90, name="empty cup"):
			HotBeverage.__init__(self, price, name)

	class BrokenMachineException(Exception):
		def __init__(self, msg="This coffee machine has to be repaired."):
			Exception.__init__(self, msg)

	def serve(self, instance_derived):
		print('use ', self.count)
		self.count += 1
		if self.count > 9:
			raise self.BrokenMachineException()
		return instance_derived() if random.randrange(2) == 0 else self.EmptyCup()

	def repair(self):
		self.count = 0
		print('##### service information: machine has been repaired! #####')


if __name__ == "__main__":
	bev_dict = {0: HotBeverage, 1: Coffee, 2: Tea, 3: Chocolate, 4: Cappuccino}
	for i in range(2):
		machine = None
		try:
			machine = CoffeeMachine()
			for j in range(10):
				print(machine.serve(bev_dict.get(random.randrange(5))))
		except Exception as e:
			print(e)
			machine.repair()
