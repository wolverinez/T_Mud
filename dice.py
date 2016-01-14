"""this module contains functions for rolling dice from a cointoss 
to a one hundred sided dice the 
funtions are named with the letter 'd' and then a number forinstance
the function to simulate a d20 is simply named d20(pluss=0) where the pluss argument
makes it possible to modify the roll
"""

import random as R


def d2(pluss=0):
	"""Simulates a coin toss"""
	return R.randint(1, 2) + pluss


def d3(pluss=0):
	"""Simulates a threesided dice"""
	return R.randint(1, 3) + pluss


def d4(pluss=0):
	"""Simulates a four sided dice"""
	return R.randint(1, 4) + pluss


def d6(pluss=0):
	"""Simulates a six sided dice"""
	return R.randint(1, 6) + pluss


def d8(pluss=0):
	"""Simulates a eight sided dice"""
	return R.randint(1, 8) + pluss


def d10(pluss=0):
	"""Simulates a ten sided dice"""
	return R.randint(1, 10) + pluss


def d12(pluss=0):
	"""Simulates a twelve sided dice"""
	return R.randint(1, 12) + pluss


def d20(pluss=0):
	"""Simulates a twenty sided dice"""
	return R.randint(1, 20) + pluss


def d100(pluss=0):
	"""Simulates a hundred sided dice"""
	return R.randint(1, 100) + pluss