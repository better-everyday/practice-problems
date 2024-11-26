class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        for n in range(len(s)+1):
            memo[n] = -1
        memo[len(s)] = 1 # Represents "" the base case (when the index reaches the end)

        def isValid(i):
            if memo[i] != -1:
                return memo[i]

            if s[i:][0] == "0":
                memo[i] = 0
            elif len(s[i:]) > 1 and int(s[i+0] + s[i+1]) >= 27:
                memo[i] = isValid(i+1)
            elif len(s[i:]) > 1:
                memo[i] = isValid(i+1) + isValid(i+2)
            else:
                memo[i] = isValid(i+1)

            return memo[i]

        isValid(0)
        return memo[0]