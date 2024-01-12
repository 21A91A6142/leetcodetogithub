class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st="aeiouAEIOU"
        k=len(s)//2
        a=s[:k]
        b=s[k:]
        c=0
        d=0
        for i in a:
            if i in st:
                c+=1
        for i in b:
            if i in st:
                d+=1
        if(c==d):
            return True
        else:
            return False