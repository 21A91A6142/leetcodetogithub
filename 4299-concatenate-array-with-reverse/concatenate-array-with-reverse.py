class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        lst=nums[::-1]
        nums.extend(lst)
        return nums
        
        