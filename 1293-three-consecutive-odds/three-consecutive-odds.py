class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c=0
        a=[]
        for i in arr:
            if i%2!=0:
                c+=1
            else:
                c=0
            a.append(c)
        if 3 in a:
            return True
        else:
            return False
        