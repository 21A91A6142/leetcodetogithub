class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]'''
        for i in range(len(nums)):
            k=(target-nums[i])
            if k in nums:
                if nums.index(k)!=i:
                    return [i,nums.index(k)]
            