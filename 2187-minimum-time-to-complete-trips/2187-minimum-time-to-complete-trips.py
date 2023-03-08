class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, 10**14+1
        res = []
        while l < r-1:
            c = (l+r)//2
            li_l = [l//t for t in time]
            li_c = [c//t for t in time]
            li_r = [r//t for t in time]
            # print(l,c,r, sum(li_l),sum(li_c),sum(li_r))
            if sum(li_l) < totalTrips and sum(li_c) >= totalTrips:
                r = c
            if sum(li_c) < totalTrips and sum(li_r) >= totalTrips:
                l = c
            if sum(li_c) >= totalTrips:
                res.append(c)
            if sum(li_l) == totalTrips:
                res.append(l)
                break
        return min(res)