class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=0
        for i in range(len(s)-1):
            s1+=(abs(ord(s[i])-ord(s[i+1])))
        return s1

        