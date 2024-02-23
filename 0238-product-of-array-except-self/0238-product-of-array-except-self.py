class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnts = collections.Counter(nums)
        res = []
        for i in nums:
            temp = 1
            for k in cnts:
                if i == k:
                    temp *= pow(k, cnts[k]-1)
                else:
                    temp *= pow(k, cnts[k])
            res.append(temp)
        return res