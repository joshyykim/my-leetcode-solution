class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        longest = ''
        result = set()
        for i in range(len(s)):
            if s[i] in longest:
                result.add(len(longest))
                longest = s[d[s[i]]+1:i+1:]
                # print(longest)
            else:
                longest += s[i]
            d[s[i]] = i
        result.add(len(longest))
        return max(result)