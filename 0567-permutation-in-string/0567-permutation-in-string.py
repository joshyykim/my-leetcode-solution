class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        lengthToCompare = len(s2)-len(s1)
        for i in range(lengthToCompare+1):
            d = collections.Counter(s2[i:i+len(s1)])
            flag = True
            for k in d1.keys():
                if k not in d or d[k] != d1[k]:
                    flag = False
            if flag:
                return True
        return False
            
            
#         len s1 = 3
#         len s2 = 10
#         xxx yyy xxxx
        
#         iterate 10-3 times
#         iterate length = 3
        