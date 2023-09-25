def maxOddBinaryNumber(s):
	"""
	rearrange the bits in such a way that the result binary number
	is the maximum odd binary number that can be created from this
	combination.

	return a string representing the maximum odd binary number that
	can be created from the given combination.
	"""
	



s = "0010"
print(maxOddBinaryNumber(s))

s = "010"
print(maxOddBinaryNumber(s))
# => "001"

s = "0101"
print(maxOddBinaryNumber(s))
# => "1001"