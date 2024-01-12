class Solution(object):
    def intersection(self, n1, n2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in n1:
            if i in n2:
                if i not in a:
                    a.append(i)
        return a
        