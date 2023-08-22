class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt, idx = 0, 0
        while cnt < len(nums):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                idx -= 1
            cnt += 1
            idx += 1