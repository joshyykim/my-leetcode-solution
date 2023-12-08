class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_idx = -1
        for i, digit in enumerate(num):
            if int(digit) % 2 == 1:
                last_idx = i
        return num[:last_idx+1] if last_idx >= 0 else ""