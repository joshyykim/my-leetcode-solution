class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = "-1"
        for i in range(len(num)-2):
            temp = num[i:i+3]
            if len(set(list(temp))) == 1 and int(temp) > int(res):
                res = temp
        return res if int(res) >= 0 else ""