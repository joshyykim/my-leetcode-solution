class Solution:
    def maxUniqueSplit(self, s: str) -> int:
#         split_string = {}
#         start_idx = 0
        
#         while start_idx < len(s):
#             temp = s[start_idx]
#             if temp in split_string:
#                 for j in range(start_idx+1, len(s)):
#                     temp += s[j]
#                     start_idx += 1
#                     if temp not in split_string:
#                         split_string[temp] = 1
#                         break
#             else:
#                 split_string[temp] = 1
#             start_idx += 1
                
#         print(split_string)
#         return len(split_string)

        def helper(d, s):
            if len(s) == 0:
                return len(d)
            
            temp = ""
            res = 0
            for i in range(len(s)):
                temp += s[i]
                if temp not in d:
                    new_d = d.copy()
                    new_d[temp] = 1
                    res = max(res, helper(new_d, s[i+1:]))
            return res
        
        return helper({}, s)