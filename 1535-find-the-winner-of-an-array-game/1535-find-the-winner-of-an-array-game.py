class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        winner = {}
        
        player1 = arr.pop(0)
        player2 = arr.pop(0)
        
        while True:
            if player1 > player2:
                if player1 not in winner:
                    winner[player1] = 1
                else:
                    winner[player1] += 1
            else:
                if player2 not in winner:
                    winner[player2] = 1
                else:
                    winner[player2] += 1
                player1 = player2
            
            if winner[player1] == k or not arr:
                break
            player2 = arr.pop(0)
        return player1