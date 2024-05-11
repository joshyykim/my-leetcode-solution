class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(idx, per):
            if idx == len(per):
                res.append(per)
                return;
            for i in range(idx, len(per)):
                per[idx], per[i] = per[i], per[idx]
                local = per[:]
                helper(idx+1, local)
                
        helper(0, nums)
        return res