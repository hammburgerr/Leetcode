class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattened_mat = [num for sublist in mat for num in sublist]
        flattened_mat_len = len(flattened_mat)
        reshaped_mat_len = r*c
        zero_mat = [[0] * c for _ in range(r)]

        if flattened_mat_len != reshaped_mat_len:
            return(mat)
        else:
            for i in range(r):
                for j in range(c):
                    zero_mat[i][j] = flattened_mat[i * c + j]
            return(zero_mat)