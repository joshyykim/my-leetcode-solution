class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        count = 0
        
        player1 = arr.pop(0)
        player2 = arr.pop(0)
        
        while True:
            if player1 > player2:
                count += 1
            else:
                count = 1
                player1 = player2
            
            if count == k or not arr:
                break
            player2 = arr.pop(0)
        return player1