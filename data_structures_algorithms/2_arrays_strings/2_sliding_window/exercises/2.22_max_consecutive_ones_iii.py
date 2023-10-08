# Collaborator: Alan Hussey

def test_equal(actual, expected):
	assert actual == expected, f"{actual} != {expected}"
	print("pass")

def longestOnes(nums, k):
	"""
	nums: [int]
	k: int
	return: int
	
	objective: Given a binary array nums and an integer k, return the maximum number of
	consecutive "1" elements in the array if you can flip at most k "0" elements.
	"""
	# using sliding window techinque
	
	# answer == right - left | s.t. at most k "0" are converted to "1"

	left = right = 0

	answer = right - left

	while right < len(nums):
		
		if nums[right] == 1:
			right += 1
		elif k > 0:
			# use one of your k values
			k -= 1
			# fliping the "0" element and increasing the length of window by decreasing k
			right += 1
		elif nums[left] == 0:
			left += 1
			k += 1
		else:
			left += 1

		# keeping track of best answer; if an additional subarray is better than current answer, store that subarray length
		answer = max(answer, right - left)

	return answer

	# hint: give ourselves permission to move left to the right (+= 1) when the left value equals 1 (and not only when left == 0)
	# hint: keep track of the "best_answer_thus_far" to compare with later "best_answer_thus_far" values


test_equal(longestOnes([1], 1), 1)
test_equal(longestOnes([1, 1], 1), 2)
test_equal(longestOnes([1]*5, 1), 5)
test_equal(longestOnes([0], 0), 0)
test_equal(longestOnes([0], 1), 1)
test_equal(longestOnes([0, 0], 1), 1)
test_equal(longestOnes([0, 1], 1), 2)
test_equal(longestOnes([0, 0], 2), 2)
test_equal(longestOnes([0]*7, 2), 2)
test_equal(longestOnes([0]*7, 7), 7)
test_equal(longestOnes([0, 0, 1], 1), 2)
test_equal(longestOnes([0, 0, 0, 0, 1], 1), 2)
test_equal(longestOnes([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 1), 2)
test_equal(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2), 6)

# test-driven: work from the simplest case and generalize from there, step-by-step gradaully adding complexity to meet the requirements.