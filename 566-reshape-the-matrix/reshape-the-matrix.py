class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        a=sum(mat,[])
        if len(a)!= r*c:
            return mat
        return [a[i*c:(i+1)*c] for i in range(r)]