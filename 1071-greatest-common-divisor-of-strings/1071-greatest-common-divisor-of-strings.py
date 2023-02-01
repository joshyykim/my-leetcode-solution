class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        li = []
        res = [""]
        for i in range(1,len(str1)+1):
            if len(str1) % i == 0:
                multiple = len(str1) // i
                if str1[:i] * multiple == str1:
                    li.append(str1[:i])
        for string in li:
            if len(str2) % len(string) == 0 and (len(str2) // len(string)) * string == str2:
                res.append(string)
        return res[-1]