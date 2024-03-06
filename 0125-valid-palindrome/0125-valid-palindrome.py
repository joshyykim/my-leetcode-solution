class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid_characters = string.ascii_letters + string.digits
        i = 0
        while i < len(s):
            if s[i] not in valid_characters:
                s = s.replace(s[i], "")
            else:
                i += 1
        return s == s[::-1]