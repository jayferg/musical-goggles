# feature-two.py
from random import shuffle

def feature-two(s: str) -> str:
	"""Return a manipulated version of s"""
	l = list(s)
	shuffle(l)
	return "".join(l)



