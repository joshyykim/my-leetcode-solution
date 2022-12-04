class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        tmp = 0
        li = []
        for i in range(len(nums)):
            tmp += nums[i]
            if len(nums) > i+1:
                li.append(abs(tmp//(i+1)-(total_sum-tmp)//(len(nums)-i-1)))
            else:
                li.append(abs(tmp//(i+1)-0))
        print(li)
        return li.index(min(li))