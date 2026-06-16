class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        s=0
        for i in range(max(1,(n-k)),n+k+1):
            if abs(n-i)<=k:
                if (n&i)==0:
                    s+=i
        return s