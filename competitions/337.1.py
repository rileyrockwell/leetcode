class Solution:
    def evenOddBit(self, n: int) -> [int]:
        # ensure 1 <= n <= 1000
        # ...

        # binary reporesentation of n: (return binary rep of n), omiting the 0-th and 1-st element
        binary_rep = bin(n)[2:]

        # create list of the binary rep (from above)
        binary_list = [int(i) for i in binary_rep]

        # iterate over the list (from above)
        even = 0
        odd = 0
        count = 0

        for i in binary_list:
            if i == 1 and count % 2 == 0:
                even += 1
            elif i == 1 and count % 2 != 0:
                odd += 1
            count += 1

        return [even, odd]
        
    
n = 13
print(bin(n)[2:])
print(Solution().evenOddBit(n))
