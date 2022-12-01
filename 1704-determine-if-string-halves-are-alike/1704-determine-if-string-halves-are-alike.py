class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        front = s[:len(s)//2:]
        back = s[len(s)//2:]
        cnt1, cnt2 = 0, 0

        for c1,c2 in zip(front, back):
            if c1 in vowels:
                cnt1 += 1
            if c2 in vowels:
                cnt2 += 1

        return cnt1 == cnt2