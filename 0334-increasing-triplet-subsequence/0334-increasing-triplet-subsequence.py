class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = sec_low = pow(2, 31)
        for i in nums:
            if low >= i:
                low = i
            elif sec_low >= i:
                sec_low = i
            else:
                return True
        return False