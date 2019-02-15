from __future__ import division
from pylab import *
from sympy import *

class Junction:
	def __init__(self, attribute=None, children=None):
		self.attribute = attribute
		self.children = children

	def set_node(self, attribute, children):
		self.attribute = attribute
		self.children = children

	def replace(self, element, value):
		for child in children:
			child.replace(element, value)

	def evaluate(self):
		attribute = self.attribute
		children = self.children
		if attribute == "+": return children[0].evaluate() + children[1].evaluate()
		elif attribute == "*": return children[0].evaluate() * children[1].evaluate()
		elif attribute == "**": return children[0].evaluate() ** children[1].evaluate()
		elif attribute == "sin": return sin(children[0].evaluate())
		elif attribute == "log":
			argument = children[0].evaluate()
			if len(children) == 1: return log(argument)
			elif len(children) == 2:
				base = children[1].evaluate()
				return log(argument, base)			
