"""
--- Description ---

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
"""

class Solution:
    def getRow(self, rowIndex: int) -> int:
        
        def get_row(r):
            if r == 0:
                return [1]
            
            row = []
            add = 0

            for n in get_row(r-1):
                row.append(add + n)
                add = n
            row.append(add)

            return row

        return get_row(rowIndex)

obj = Solution()
print(obj.getRow(33))

"""
--- Submission ---

Runtime: 33 ms, faster than 91.58% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 96.88% of Python3 online submissions for Pascal's Triangle II.
"""