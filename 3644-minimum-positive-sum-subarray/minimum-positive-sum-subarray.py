class Solution:
    def minimumSumSubarray(self, a: List[int], l: int, r: int) -> int:
        a1=[]
        for j in range(l,r+1):
            print(j)
            for i in range(0,len(a)-j+1):
                k=a[i:i+j]
                if(sum(k)>0):
                    a1.append(sum(k))
        if len(a1)>0:
            if min(a1)>0:
                return min(a1)
            else:
                return -1
        else:
            return -1

