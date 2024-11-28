class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        currNum = None
        toRemove = []
        for i, num in enumerate(nums):
            if currNum == None:
                currNum = num
                count += 1
                continue

            if num == currNum:
                count += 1
                if count > 2:
                    count -= 1
                    toRemove.append(i-count)
            else:
                currNum = num
                count = 1

        for n in toRemove:
            nums.pop(n)
            