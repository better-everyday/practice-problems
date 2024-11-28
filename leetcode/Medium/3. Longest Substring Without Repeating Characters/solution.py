class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Map = defaultdict(int)
        left = 0
        Count = 0
        maxCount = 0
        for right in range(len(s)):
            Map[s[right]] += 1
            while Map[s[right]] > 1:
                Map[s[left]] -= 1
                left += 1
                Count -= 1
            Count += 1
            maxCount = max(maxCount, Count)

        return maxCount
