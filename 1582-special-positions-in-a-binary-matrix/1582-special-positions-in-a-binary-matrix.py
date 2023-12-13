class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                counter1 = Counter(mat[j])
                counter2 = Counter([_[i] for _ in mat])
                if counter1[1] == 1 and counter2[1] == 1 and mat[j][i] == 1:
                    res += 1
        return res