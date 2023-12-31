# references: https://stackoverflow.com/questions/212358/binary-search-bisection-in-python

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        elif n > 1:
            # use bisection search to determine the first bad version
            # in order to limit the number of calls to the api
            guess = n // 2 + 1
    
        ###################
        # EXAMPLE: bisection cube root (only positive cubes!)
        ###################
        cube = 27
        #cube = 8120601
        # won't work with x < 1 because initial upper bound is less than ans
        #cube = 0.25
        epsilon = 0.01
        num_guesses = 0
        low = 0
        high = cube
        guess = (high + low)/2.0
        while abs(guess**3 - cube) >= epsilon:
            if guess**3 < cube:
                # look only in upper half search space
                low = guess
            else:
                # look only in lower half search space
                high = guess
        # next guess is halfway in search space
        guess = (high + low)/2.0
        num_guesses += 1
        print('num_guesses =', num_guesses)
        print(guess, 'is close to the cube root of', cube)

print(Solution().firstBadVersion(5))
print(Solution().firstBadVersion(1))