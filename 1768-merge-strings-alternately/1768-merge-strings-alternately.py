class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        shorter = min(len(word1), len(word2))
        for i in range(shorter):
            res += word1[i] + word2[i]
        return res + word1[shorter:] + word2[shorter:]