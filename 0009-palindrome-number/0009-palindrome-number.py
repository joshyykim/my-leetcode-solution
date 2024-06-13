class Solution(object):
    def isPalindrome(self, x):
        st = str(x)
        n = len(st)
        for i in range(0, int(n/2)):
            if st[i] != st[-(i+1)]:
                return False
        return True