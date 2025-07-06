class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(num):
            n=num
            s=0
            while(n>0):
                r=n%10
                s+=r
                n=n//10
            return s
        m=nums[0]
        for i in range(len(nums)):
            k=digit_sum(nums[i])
            if m>k:
                m=k
        return m
        