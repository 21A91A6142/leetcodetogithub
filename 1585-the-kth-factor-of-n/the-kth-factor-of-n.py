class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n//2+1):
            if n%i==0:
                l.append(i)
        l.append(n)
        if k>len(l):
            return -1
        else:
            return l[k-1]