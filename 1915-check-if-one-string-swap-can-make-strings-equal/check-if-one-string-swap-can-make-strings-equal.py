class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c=0
        if sorted(s1)==sorted(s2):
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    c+=1
            if c==2 or c==0:
                return True
            else:
                return False
        else:
            return False
        