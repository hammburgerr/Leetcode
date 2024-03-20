class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        zero_matrix = [[0] * row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                zero_matrix[j][i] = matrix[i][j]
                
        return zero_matrix