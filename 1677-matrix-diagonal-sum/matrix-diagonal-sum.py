class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s=0
        for i in range(len(mat)):
            s+=mat[i][i]
            s+=mat[i][len(mat)-1-i]
        if len(mat) % 2 == 1:
            s -= mat[len(mat)//2][len(mat)//2]
        return s