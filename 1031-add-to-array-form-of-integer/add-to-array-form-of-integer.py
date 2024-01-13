class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s=""
        for i in num:
            s+=str(i)
        a=int(s)
        l=a+k
        b=[]
        while(l):
            r=l%10
            b.append(r)
            l=l//10
        return b[::-1]
