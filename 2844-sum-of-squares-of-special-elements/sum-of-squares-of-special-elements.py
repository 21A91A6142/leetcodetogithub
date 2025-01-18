class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)
        s=0
        for i in range(1,len(nums)):
            if k%i==0:
                s+=(nums[i-1]*nums[i-1])
        s+=(nums[k-1]*nums[k-1])
        return s
