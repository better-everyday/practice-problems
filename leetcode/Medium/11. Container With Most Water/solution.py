class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        maxWater = 0
        while start < end:
            currWater = (end-start) * min(height[start], height[end])
            maxWater = max(maxWater, currWater)

            if height[start] < height[end]:
                start += 1
            elif height[end] < height[start]:
                end -= 1
            else:
                start += 1
                end -= 1

        return maxWater
