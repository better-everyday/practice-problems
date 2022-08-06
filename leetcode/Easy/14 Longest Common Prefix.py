"""
--- Description ---

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        prefix = ""
        for i in range(len(max(strs, key=len))):
            prefix += max(strs, key=len)[i]

            for word in strs:
                if prefix != word[:i+1]:
                    return prefix[:i]
                    
        return prefix

# obj = Solution()
# print(obj.longestCommonPrefix(["flower","flow","flight"]))

"""
--- Submission ---

Runtime: 36 ms, faster than 92.35% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 88.43% of Python3 online submissions for Longest Common Prefix.
"""