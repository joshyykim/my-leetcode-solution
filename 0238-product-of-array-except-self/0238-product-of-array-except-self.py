class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        res = []
        for i in nums:
            tmp = 1
            for k in d:
                if k != i:
                    tmp *= pow(k, d[k])
                else:
                    tmp *= pow(k, d[k]-1)
            res.append(tmp)
        return res
        