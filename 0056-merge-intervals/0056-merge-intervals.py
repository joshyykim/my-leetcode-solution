class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i = 0
        
        while i < len(intervals)-1:
            s1, e1 = intervals[i]
            s2, e2 = intervals[i+1]
            if s1 <= s2 <= e1 or s2 <= s1 <= e1:
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [min(s1, s2), max(e1, e2)])
            else:
                i += 1

        return intervals