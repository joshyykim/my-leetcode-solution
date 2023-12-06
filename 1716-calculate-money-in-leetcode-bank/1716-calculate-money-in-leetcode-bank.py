class Solution:
    def totalMoney(self, n: int) -> int:
        return sum([(_ % 7) + (_ // 7) + 1 for _ in range(n)])