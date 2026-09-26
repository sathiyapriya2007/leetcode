class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        row = [0] * m
        col = [0] * n
        for i, j in indices:
            row[i] += 1
            col[j] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2:
                    count += 1
        return count