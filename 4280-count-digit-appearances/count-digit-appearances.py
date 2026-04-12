class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        c=0
        for i in nums:
            temp=str(i)
            dig=str(digit)
            c+=temp.count(dig)
        return c
        