class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = "AEIOUaeiou"
        temp_vowels = []
        for c in s:
            if c in vowels:
                temp_vowels.append(c)
        
        for i in range(len(s)):
            if s[i] in vowels:
                temp = temp_vowels.pop(-1)
                s[i] = temp
        return "".join(s)