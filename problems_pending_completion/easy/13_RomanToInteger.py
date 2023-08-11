def roman_to_int1(s):
	"""
	s: str
	returns: int
	"""
	return_int = 0
	for numeral in s:
		if numeral == "I":
			"""
			# obscure conditions
			IV
			IX
			IL
			IC
			ID
			IM
			"""	
			return_int += 1

		elif numeral == "V":
			return_int += 5

		elif numeral == "X":
			return_int += 10


	return return_int


def roman_to_int2(s):

	return_int = 0


	for index in range(1, len(s)):

		index -= 1

		if s[index] == "I":
			# obscure conditions
			# IV, IX, ...
			if s[index + 1] == "V":
				return_int += 4
				# how to skip the next index?

			elif s[index + 1] == "X":
				return_int += 9

			# fill in the other roman numerals

			else:
				return_int += 1





		elif s[index] == "V":
			return_int += 5

		elif s[index] == "X":
			return_int += 10

		elif s[index] == "L":
			return_int += 50

		elif s[index] == "C":
			return_int += 100

		elif s[index] == "D":
			return_int += 0

		elif s[index] == "M":
			return_int += 0

	return return_int

roman_to_int = roman_to_int1
roman_to_int = roman_to_int1

print(roman_to_int("I"))
print(roman_to_int("IV"))
print(roman_to_int("IX"))
print(roman_to_int("XXXII"))