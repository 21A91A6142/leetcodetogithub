class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=len(s)
        if k<=1:
            return s
        elif k==n:
            return s[::-1]
        else:
            pre=s[:k]
            suf=s[k:]
            #print(pre,suf)
            return pre[::-1]+suf
        