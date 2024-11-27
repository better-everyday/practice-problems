"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda time:(time.start, time.end))

        time_map = defaultdict(list)
        for i in intervals:
            time_map[i.start].append(i.end)

        count = 0
        print(time_map)
        for start in time_map.keys():
            for end in range(len(time_map[start])):
                count += 1

                new_end = time_map[start].pop(0)
                for time in time_map.keys():
                    if time >= new_end and time_map[time] != []:
                        new_end = time
                        break
                while new_end in time_map and time_map[new_end] != []:
                    new_end = time_map[new_end].pop(0)
                    for time in time_map.keys():
                        if time >= new_end and time_map[time] != []:
                            new_end = time
                            break

                print(time_map)

        return count