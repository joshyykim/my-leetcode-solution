class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(idx, sub):
            res.append(sub)
            for i in range(idx, len(nums)):
                local = sub[:]
                local.append(nums[i])
                helper(i+1, local)
        
        helper(0, [])
        print(res)
        return res