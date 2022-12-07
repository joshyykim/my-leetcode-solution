class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] < duration:
                res += timeSeries[i+1] - timeSeries[i]
            else:
                res += duration
        return res + duration