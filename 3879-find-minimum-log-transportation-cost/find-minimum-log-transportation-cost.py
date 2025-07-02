class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        if n<=k and m<=k:
            return 0
        elif n>k:
            l1=n-k
            l2=n-l1
            return l1*l2
        elif m>k:
            l1=m-k
            l2=m-l1
            return l1*l2
        