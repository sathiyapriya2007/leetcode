class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        years = [0] * 101   # 1950 to 2050
        for birth, death in logs:
            for y in range(birth, death):
                years[y - 1950] += 1
        return years.index(max(years)) + 1950