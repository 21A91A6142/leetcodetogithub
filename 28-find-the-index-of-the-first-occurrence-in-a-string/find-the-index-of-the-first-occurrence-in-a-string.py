class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            st=0
            end=len(needle)
            for i in range(0,len(haystack)):
                print(haystack[i:i+end])
                if haystack[i:i+end]==needle:
                    return i
        else:
            return -1
        