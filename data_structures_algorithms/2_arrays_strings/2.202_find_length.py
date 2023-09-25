def find_length(s):
	# note: string rather than array
	left = curr = answer = 0

	for right in range(len(s)):
		if s[right] == "0":
			curr += 1

		while curr > 1:
			if s[left] == "0":
				curr -= 1
			left += 1

		answer = max(answer, right - left + 1)

	return answer


def find_length(s):
	left = curr = answer = 0

	for right in range(len(s)):
		if s[right] == "0":
			curr += 1

		while curr > 1:
			if s[left] == "0":
				curr -= 1
			left += 1

		answer = max(answer, right - left + 1)

	return answer


def find_length(s):
	left = curr = answer = 0

	for right in range(len(s)):
		if s[right] == "0":
			curr += 1

		while curr > 1:
			if s[left] == "0":
				curr -= 1
			left += 1

		range_ = right - left + 1
		answer = max(answer, range_)

	return answer


def find_length(s):
	left = curr = answer = 0

	for right in range(len(s)):
		if s[right] == "0":
			curr += 1

		while curr > 1:
			if s[left] == "0":
				curr -= 1
			left += 1

		range_ = right - left + 1
		answer = max(answer, range_)

	return answer

print(find_length("110110"))