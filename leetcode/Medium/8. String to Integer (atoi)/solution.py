class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        s = set()
        for i, num in enumerate(nums):
            j = i+1
            k = len(nums)-1
            while j<k:
                sum = num + nums[j] + nums[k]
                if sum == 0:
                    s.add((num, nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1

        result = list(s)
        return result

                
        return result