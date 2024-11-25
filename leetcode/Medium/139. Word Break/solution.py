class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        
        def breakoff(s):
            if s == "":
                return True
            try:
                if memo[s] == False:
                    return False
            except:
                pass

            word_indices = []
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    word_indices.append(i)

            for i in word_indices:
                if breakoff(s[i:]) == True:
                    return True

            memo[s] = False
            return False

        return breakoff(s)