class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if len(intervals) == 0:
            return [newInterval]
        insertStart = newInterval[0]
        insertEnd = newInterval[1]
        curr = intervals[0]
        i = 0
        currStart = curr[0]
        currEnd = curr[1]
        while i + 1 < len(intervals) and currEnd < insertStart:
            i += 1
            curr = intervals[i]
            currStart = curr[0]
            currEnd = curr[1]
        # Now, curr must be either at the end of the list or currEnd >= insertStart
        # Handle clean insertion
        if i == len(intervals) - 1 and currEnd < insertStart:
            intervals.append(newInterval)
            return intervals
        # Otherwise, handle normally
        res = intervals[0:i]
        if insertEnd < currStart:
            return intervals[:i] + [newInterval] + intervals[i:]
        currStart = min(insertStart, currStart)
        currEnd = max(insertEnd, currEnd)
        while i + 1 < len(intervals):
            if currEnd < intervals[i + 1][0]:
                res.append([currStart, currEnd])
                currStart = intervals[i + 1][0]
                currEnd = intervals[i + 1][1]
            else:
                currEnd = max(currEnd, intervals[i + 1][1])
                i += 1
        # Last interval
        res.append([currStart, max(currEnd, intervals[i][1])])
        return res




# Given array of non overlapping intervals
# Already sorted
# Overlapping if:
    # [1, 3] [2, 5] [6, 9]
    # if end i < start i + 1