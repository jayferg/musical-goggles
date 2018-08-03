# feature-two.py
from random import shuffle

def feature-two(s: str) -> str:
	"""Return a shuffled version of s"""
	l = list(s)  # We can't shuffle a string, so make a list
	shuffle(l)   # in place
	return "".join(l)




def feature-four(s: str) -> str:
	"""return an upper case version of s"""
	return s.upper()

