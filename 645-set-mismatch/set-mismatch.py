class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(1,len(nums)+1):
            if nums.count(i)>1:
                a.append(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                a.append(i)
        return (a)
        