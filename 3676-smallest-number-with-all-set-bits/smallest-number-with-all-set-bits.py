import math
class Solution:
    def smallestNumber(self, n: int) -> int:
        c=0
        c1=0
        while(n>0):
            
            if n&1>0:
                c+=1
            else:
                c1+=1
            n=n>>1
        print(c+c1)
        return int(math.pow(2,c+c1)-1)
        