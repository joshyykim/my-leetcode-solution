class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        vals = list(Counter(tasks).values())
        m = max(vals)
        repeats = (m-1) * (n+1)
        last = [1 for _ in vals if _ == m]
        
        return max(repeats + sum(last), len(tasks))