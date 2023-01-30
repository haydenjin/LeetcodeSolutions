class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        for i in range(len(intervals)):
            # New interval is smaller, add it to the front
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # New interval is bigger, add the old one
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            # Create a new interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        result.append(newInterval)

        return result
