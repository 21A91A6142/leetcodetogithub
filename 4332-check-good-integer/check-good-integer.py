class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        t=n
        s=0
        sq=0
        while t>0:
            r=t%10
            print(r)
            s+=r
            sq+=(r*r)
            t=t//10
        # print(sq,s)
        if sq-s>=50:
            return True
        else:
            return False
