"""
--- Description ---

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""

class Solution:
    def guessNumber(self, n: int) -> int:

        left, right = 0, n
        while left <= right:
            
            mid = (left + right) // 2
            
            if guess(mid) > 0:
                left = mid + 1
            elif guess(mid) < 0:
                right = mid - 1
            else:
                return mid

"""
--- Submission ---

Runtime: 32 ms, faster than 91.30% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 13.9 MB, less than 66.35% of Python3 online submissions for Guess Number Higher or Lower.
"""