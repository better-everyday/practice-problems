class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = s[0]

        # Odd palindromes
        for i in range(len(s)):
            m = 1
            while True:
                try:
                    if s[i-m] != s[i+m] or i-m < 0:
                        break
                except:
                    break

                if m*2+1 > len(longest):
                    longest = s[i-m:i+m+1]

                m += 1

        print(longest)
        # Even palindromes
        for j in range(len(s)-1):
            if s[j] == s[j+1]:
                if len(longest) < 2:
                    longest = s[j:j+2]

                m = 1
                while True:
                    try:
                        if s[j-m] != s[j+1+m] or j-m < 0:
                            break
                    except:
                        break

                    if m*2+2 > len(longest):
                        print(j,m)
                        longest = s[j-m:j+1+m+1]

                    m += 1

        return longest
