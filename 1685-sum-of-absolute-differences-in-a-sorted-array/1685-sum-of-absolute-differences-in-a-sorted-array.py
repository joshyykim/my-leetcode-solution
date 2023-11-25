class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        res = [total-nums[0]*len(nums)]
        
        for i in range(1, len(nums)):
            diff = nums[i]-nums[i-1]
            res.append(res[-1] + i*diff - (len(nums)-i)*diff)
            
        return res