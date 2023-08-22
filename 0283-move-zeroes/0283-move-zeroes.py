class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        for i in range(n):
            temp = nums.pop(count)
            # print(temp, nums)
            if temp == 0:
                nums.append(temp)
            else:
                nums.insert(count, temp)
                count += 1