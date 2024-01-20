class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n=int(math.sqrt(num))
        if(n*n==num):
            return True
        else:
            return False
        