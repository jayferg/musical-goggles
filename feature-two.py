# feature-two.py
from random import shuffle

def feature-two(s: str) -> str:
	"""Return a shuffled version of s"""
	l = list(s)  # We can't shuffle a string, so make a list
	shuffle(l)   # in place
	return "".join(l)

def feature-three(s: str) -> str:
	"""Return an upper case, shuffled version of s"""
	return feature-two(s).upper()


