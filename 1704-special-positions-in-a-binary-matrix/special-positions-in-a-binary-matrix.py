class Solution(object):
    def numSpecial(self, mat):
        
        row_sums = [sum(row) for row in mat]
        
        col_sums = [sum(col) for col in zip(*mat)]
        
        special_count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1
        
        return special_count