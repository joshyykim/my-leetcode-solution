class Solution:
    def totalMoney(self, n: int) -> int:
        base = sum([_ for _ in range(1,8)])
        num_week = 0
        res = 0
        while n > 0:
            if n >= 7:
                res += base + num_week * 7
                n -= 7
                num_week += 1
            else:
                res += sum([_ for _ in range(1,n+1)]) + num_week * n
                break
        return res