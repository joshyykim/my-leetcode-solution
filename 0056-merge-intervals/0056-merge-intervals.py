class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ### method 2 (sorting, less memory) 
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
    
#         ### method 3 (sorting, more memory)
#         intervals.sort(key=lambda x:x[0])
#         index = 0
#         res = []
        
#         while index < len(intervals):
#             if res[-1][1] >= interval[index][0]:
#                 res.append([res[-1][0],max(res[-1][1],interval[index][1])])
#             else:
#                 res.append(interval[index])
#                 index += 1
                
#         return res