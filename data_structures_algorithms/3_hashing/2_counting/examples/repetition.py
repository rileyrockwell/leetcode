# 1. find_longest_substring		0.00
# 2. intersection				0.00
# 3. are_occurences_equal		0.00
# 4. subarray_sum				0.00
# 5. number_of_subarrays		0.00

from collections import defaultdict

# 1. find_longest_substring
def find_longest_substring(s, k):
	# use a hashmap w/in the context of a sliding window
	counts = defaultdict(int)
	
	left = ans = 0

	for right in range(len(s)):
		# build the dictionary
		counts[s[right]] += 1

		while len(counts) > k:
			counts[s[left]] -= 1

			# if the value (of the key:value pair) does not exist?
			if counts[s[left]] == 0:
				del counts[s[left]]
			left += 1

		ans = max(ans, right - left + 1)

	return ans


# 2. intersection
def intersection(nums):
	# using a hashmap w/in a sliding window
	

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(intersection(nums))

# 3. are_occurences_equal


# 4. subarray_sum


# 5. number_of_subarrays

