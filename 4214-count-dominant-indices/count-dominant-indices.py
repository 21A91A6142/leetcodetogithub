class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(0,len(nums)-1):
            avg=sum(nums[i+1:])/(len(nums)-(i+1))
            print(avg)
            if avg >= nums[i]:
                continue
            else:
                c+=1
        return c