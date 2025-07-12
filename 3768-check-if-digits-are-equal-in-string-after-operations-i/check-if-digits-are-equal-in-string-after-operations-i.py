class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while(len(s)>2):
            s1=""
            for i in range(len(s)-1):
                su=(int(s[i])+int(s[i+1]))%10
                s1+=str(su)
            s=s1
        if s[0]==s[1]:
            return True
        else:
            return False