class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal = []
        
        for i in range(len(nums)):
            for j, num in enumerate(nums[i]):
                if len(diagonal) <= i+j:
                    diagonal.append([])
                diagonal[i+j].insert(0,num)
        
        res = []
        for li in diagonal:
            res += li
        return res