class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def helper(ip, string):
            if len(string) == 0 and len(ip) == 4:
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