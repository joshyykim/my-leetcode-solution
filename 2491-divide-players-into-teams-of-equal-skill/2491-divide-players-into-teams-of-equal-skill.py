class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = min(skill) + max(skill)
        cnt = collections.Counter(skill)
        li = set()
        for k in cnt.keys():
            if cnt[k] != cnt[s-k]: return -1
            if k > s-k:
                li.add((k,s-k, cnt[k]))
            elif k < s-k:
                li.add((s-k,k, cnt[k]))
            else:
                li.add((s-k,k, cnt[k]//2))
        res = 0
        for l in li:
            res += l[0]*l[1]*l[2]
        return res