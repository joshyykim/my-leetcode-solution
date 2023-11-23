class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        
        for begin, end in zip(l,r):
            temp = nums[begin:end+1]
            temp.sort()
            diffs = [temp[i+1]-temp[i] for i in range(len(temp)-1)]
            # print(temp, diffs)
            if len(set(diffs)) == 1:
                res.append(True)
            else:
                res.append(False)
                
        return res