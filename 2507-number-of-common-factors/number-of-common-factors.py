class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        c=max(a,b)
        d=0
        for i in range(1,c+1):
            if a%i==0 and b%i==0:
                d+=1
        return d
        