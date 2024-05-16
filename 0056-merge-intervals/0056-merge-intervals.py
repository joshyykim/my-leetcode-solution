class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        index = 0
        
        while index < len(intervals)-1:
            interval1, interval2 = intervals.pop(index), intervals.pop(index)
            if interval1[1] >= interval2[0]:
                intervals.insert(index,[interval1[0],max(interval1[1],interval2[1])])
            else:
                intervals.insert(index, interval2)
                intervals.insert(index, interval1)
                index += 1

        return intervals