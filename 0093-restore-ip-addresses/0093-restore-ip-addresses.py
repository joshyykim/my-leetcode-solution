class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def isValid(ip):
            for integer in ip:
                i = int(integer)
                if i < 0 and i > 255:
                    return False
            return True
        
        def helper(ip, string):
            # print(ip, string)
            if len(string) == 0 and len(ip) == 4:
                if isValid(ip):
                    res.append(".".join(ip))
                return
            
            temp = ""
            cnt = 0
            for c in string:
                temp += c
                cnt += 1
                if temp[0] == "0" and len(temp) > 1:
                    break
                if int(temp) >= 0 and int(temp) <= 255:
                    ip.append(temp)
                    helper(ip, string[cnt:])
                    ip.pop()
                else:
                    break
            
        
        helper([], s)
        
        return res