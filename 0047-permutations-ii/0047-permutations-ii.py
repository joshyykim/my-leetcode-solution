class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        
        def helper(indices, cnt):
            if cnt == len(nums):
                temp = []
                for index in indices:
                    temp.append(nums[index])
                permutation.append(tuple(temp))

            for i in range(len(nums)):
                if not i in indices:
                    helper(indices+[i], cnt+1)
        
        helper([], 0)
        
        return set(permutation)