class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = set(nums)
        nums.clear()
        nums.extend(temp)
        nums.sort()
        return len(nums)