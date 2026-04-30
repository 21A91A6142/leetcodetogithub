class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums)<=2:
            return nums
        lst=[]
        lst.append(nums[0])
        for i in range(1,len(nums)-1):
            if nums[i]>max(nums[:i]) or nums[i]>max(nums[i+1:]):
                lst.append(nums[i])
        lst.append(nums[-1])
        return lst