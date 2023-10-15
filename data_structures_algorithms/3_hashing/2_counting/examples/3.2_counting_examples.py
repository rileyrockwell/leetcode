from collections import defaultdict
from collections import Counter

class Solution:

    # sliding window; use a hashmap to keep track of items in the window
    def find_longest_substring(self, s, k):
        # map elements in s to their frequency
        counts = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans


    def intersection(self, nums: [[int]]) -> [int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)
        
        return sorted(ans)


    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1


    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1


    def subarraySum(self, nums: [[int]], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
    
        return ans


    def numberOfSubarrays(self, nums: [[int]], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
        

if __name__ == "__main__":
    print(Solution().find_longest_substring("abc", 3))
    print(Solution().areOccurrencesEqual("abacbc"))