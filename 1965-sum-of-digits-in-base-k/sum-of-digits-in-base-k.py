import math
def findsum(m):
    s=0
    while(m>0):
        q=m%10
        s+=q
        m=m//10
    return s
def findbase(n,k):
    s=0
    while(n>0):
        q=n%k
        s=s*10+q
        n=n//k
    return s

class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        m=findbase(n,k)
        l=findsum(m)
        return l
        