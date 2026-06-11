
"""swap.py

Written by: Harley Dangan

A minimal Python template demonstrating a simple swap utility and
typical structure for scripts: imports, functions, CLI entrypoint,
and basic tests.

Usage:
	python swap.py 1 2

This will print the two values before and after swapping.
"""

# Allows for forward references in type hints, enabling the use of types that are defined later in the code or not yet defined at all.
from __future__ import annotations

import sys

def swap(a, b):
	"""Return a tuple with the values swapped.

	Args:
		a: First value.
		b: Second value.

	Returns:
		a: Swapped first value.
		b: Swapped Second value.
	"""
	a += b
	b = a - b
	a -= b
	return a, b

def main() -> int:
	"""Command-line entry point.

	If two arguments are provided, swap and print them. Otherwise show usage.
	Returns an exit code.
	"""
	
    # Check if any arguments are entered.
	if sys.argv is None:
		print("No arguments provided. Usage: python swap.py <value1> <value2>")
		return 1
	# Check if the correct number of arguments is provided.
	elif len(sys.argv) != 3:
		print("Usage: python swap.py <value1> <value2>")
		return 1    

    # Store input parameters into variables a and b, convert to integers, and print before swapping.
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print(f"Before: a={a}, b={b}")
	# Call the swap function and print after swapping.
	a, b = swap(a, b)
	print(f"After:  a={a}, b={b}")
	return 0

if __name__ == "__main__":
	raise SystemExit(main())

