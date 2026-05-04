import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copymat = copy.deepcopy(matrix)
        n=len(matrix)-1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])-1,-1,-1):
                matrix[i][n-j]=copymat[j][i]
                # print(i,n-j)