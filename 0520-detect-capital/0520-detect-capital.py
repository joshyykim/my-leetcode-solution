class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper(): return True
        if word[1:] == word[1:].lower(): return True
        return False