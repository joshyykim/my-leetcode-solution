class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams, matches = n, 0
        while teams > 1:
            matches += teams // 2
            teams = math.ceil(teams / 2)
        return matches