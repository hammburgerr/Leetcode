class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        answer = True

        for i in range(row-1):
            for j in range(col-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    answer = False
                else:
                    pass

        return answer