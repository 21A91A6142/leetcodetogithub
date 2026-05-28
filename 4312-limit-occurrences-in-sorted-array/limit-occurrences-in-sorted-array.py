class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        lst=[]
        for i in nums:
            if i not in lst:
                if nums.count(i)>=k:
                    lst.extend([i]*k)
                elif nums.count(i)<k:
                    lst.extend([i]*nums.count(i))
        return lst
