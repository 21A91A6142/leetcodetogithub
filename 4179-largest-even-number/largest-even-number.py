class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        while(True):
            if n==0:
                return ""
            elif s[n-1]!="2":
                n=n-1
            else:
                return s[:n]

        