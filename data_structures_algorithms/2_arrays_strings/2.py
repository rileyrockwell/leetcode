def find_length(s):
	left = curr_sum = answer = 0

	for right in range(len(s)):
		if s[right] == "0":
			curr_sum += 1

		while curr_sum > 1:
			if s[left] == "0":
				curr_sum -= 1
			left += 1

		answer = max(answer, right - left + 1)

	return answer

print(find_length("11110110"))


def find_length(s):
	left = curr_sum = answer = 0
	for right in range(len(s)):
		if s[right] == "0":
			curr_sum += 1

		while curr_sum > 1:
			if s[left] == "0":
				curr_sum -= 1

			left += 1

		answer = max(answer, right - left + 1)

	return answer


def find_length(s):
	# using the sliding window techinque
	# notice, the only thing that has changes is the data structure (string rather than list)
	# q: what is the objective? what are we find the length with respect to? what are the constraints?

	"""
	Objective: You may choose up to one "1" and flip it to a "0". What is the length of the longest substring
	achievable that contains only "1"?

	Objective B/c you can flip one "0" to a "1", what is the longest substring that contains at most one "0".
	"""

	left = answer = curr_sum = 0

	for right in range(len(s)):
		# explain...
		if s[right] == "0":
			# turn on the dumby variable
			curr_sum += 1

			while curr_sum > 1:
				# explain...
				if s[left] == "0":
					# turn off the dumby variable
					curr_sum -= 1

				# b/c left is not iterating
				left += 1

			# recall: answer = 0, to begin with
			# right - left + 1: right b/c ...; left b/c ...; + 1 b/c range(len(s))?
			answer = max(answer, right - left + 1)

	return curr_sum
print(find_length("00110100"))



def find_length1(s):
	left = curr = answer = 0

	for right in range(len(s)):
		if s[right] == "0":
			# activate binary variable b/c we can flip from "0" to "1"
			curr += 1

		# if the binary variable is activated, ensure that the element
		# to the left of the frist identified "0" is not another "0"
		while curr > 1:
			if s[left] == "0":
				# indicate that the length of the "examined" subarray
				# is no longer the maximum subarray
				curr -= 1 
				# b/c we are not iterating
			left += 1

			# explain: right - left + 1
			answer = max(answer, right - left + 1)

	return answer

s = "00110100"
print("###")
print(find_length1(s))

# objective: find the longest substring that contains at most one "0"
