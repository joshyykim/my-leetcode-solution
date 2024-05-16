class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        idx = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[idx][1]:
                res[idx][1] = max(intervals[i][1], res[idx][1])
            else:
                res.append(intervals[i])
                idx += 1

        return res