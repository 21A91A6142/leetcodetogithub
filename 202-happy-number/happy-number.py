class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l=[]
        while(True):
            c=n
            s=0
            while(n):
                q=n%10
                s+=q*q
                n=n//10
            c=s
            if c not in l and c==1:
                return True
            elif c in l:
                return False
            else:
                n=c
                l.append(s)

        