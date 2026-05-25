class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        z=nums.count(0)
        l=len(nums)-z
        c=0
        for i in range(len(nums)):
            if nums[i]==0 and i<l:
                c+=1
        return c

