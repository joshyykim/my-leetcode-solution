class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        
        i = 0
        while i < len(intervals)-1:
            s1, e1 = intervals[i]
            s2, e2 = intervals[i+1]
            
            if s1 <= s2 <= e1:
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [s1, max(e1, e2)])
            else:
                i += 1
        
        return intervals