"""
--- Description ---

Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # 1. Brute Force
        """
        def find(seq):
            list = []
            for x in seq:
                if x not in list:
                    list.append(x)
                else:
                    break
            return list

        length = 0
        s = list(s)
        
        print(s)
        for x in range(len(s)):
            print(find(s[x:]))
            string = len(find(s[x:]))
            if string > length:
                length = string
            if length >= len(s) - x:
                break
        
        return length
        """

        # 2
        """
        string = ""
        length = 0
        s = list(s)
        for x in range(len(s)):
            popped = s.pop(0)
            string += popped
            print(string)
            try:
                if s.index(popped) + 1 <= len(string):
                    if len(string) > length:
                        length = len(string)
                    string = ""
            except:
                if len(string) > length:
                    length = len(string)

        return length
        """

        # 3 Recursion (better because have to check every substring)
        string = ""
        length2 = 0
        for x in s:
            if x not in string: string += x
            else: break
        length = len(string)

        next = s[1:]
        if len(next) > length:
            length2 = self.lengthOfLongestSubstring(next)
        return max(length, length2)


obj = Solution()
print(obj.lengthOfLongestSubstring("dvdf"))

"""
--- Submission ---

1. Brute Force
Runtime: 4144 ms, faster than 5.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 5.33% of Python3 online submissions for Longest Substring Without Repeating Characters.

3. Recursion
Runtime: 390 ms, faster than 18.06% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 520.8 MB, less than 5.36% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
