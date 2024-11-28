class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_map = defaultdict(int)
        for rect in rectangles:
            ratio_map[rect[0] / rect[1]] += 1

        Total = 0
        for count in ratio_map.values():
            if count == 1 or count == 0:
                Total += 0
            elif count == 2:
                Total += 1
            else:
                Total += (count-1) * (count) / 2

        return int(Total)
