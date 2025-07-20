class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        spe=""
        for i in range(len(s)):
            if s[i]=='#':
                spe+=(spe)
            elif s[i]=="%":
                spe=spe[::-1]
            elif s[i]=="*":
                spe=spe[0:len(spe)-1]
            else:
                spe+=(s[i])
            print(spe)
        return spe