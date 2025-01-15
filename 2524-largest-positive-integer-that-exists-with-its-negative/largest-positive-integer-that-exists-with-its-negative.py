class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        k=sorted(nums)
        for i in k:
            if i<0:
                if -1*i in k:
                    a.append(-1*i)
        if len(a)>0:
            return max(a)
        else:
            return -1        