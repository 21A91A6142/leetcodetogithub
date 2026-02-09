import math
class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n+1
        m=int(math.log(n+1)/math.log(2))
        return m+1