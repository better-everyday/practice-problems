class Solution:
    def canJump(self, nums: List[int]) -> bool:

        i = 0
        while i < len(nums)-1:
            
            jumped = False
            for jump in range(1, nums[i]+1): # Check positions within jump range

                reach = jump + nums[i+jump]

                if reach+i >= len(nums)-1: return True
                if reach > nums[i]: # If satisfied,
                    i += jump # Then jump
                    jumped = True
                    break

            if not jumped:
                return False

        return True