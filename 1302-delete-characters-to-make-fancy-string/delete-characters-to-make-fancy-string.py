class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return s
        s1=""
        for i in range(len(s)-2):
            if s[i]==s[i+1]==s[i+2]:
                continue
            else:
                s1+=s[i]
        return s1+s[-2]+s[-1]