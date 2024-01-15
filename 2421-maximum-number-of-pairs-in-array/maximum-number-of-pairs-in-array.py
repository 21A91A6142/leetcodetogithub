class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=0
        l=0
        a=[]
        b=[]
        for i in nums:
            if i not in a:
                a.append(i)
        for i in a:
            p+=(nums.count(i))//2
            l+=(nums.count(i))%2
        b.append(p)
        b.append(l)
        return b