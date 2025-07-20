class Solution(object):
    
    def splitArray(self, nums):
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            else:
                return True
        """
        :type nums: List[int]
        :rtype: int
        """
        A=[]
        B=[]
        for i in range(len(nums)):
            if isprime(i):
                A.append(nums[i])
            else:
                B.append(nums[i])
        return abs(sum(A)-sum(B))
        