class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones=s.count('1')
        zeros=s.count('0')
        s1=""
        if ones>1:
            s1=(ones-1)*"1"
        s2=zeros*"0"
        if len(s1)>0:
            return s1+s2+"1" 
        else:
            return s2+"1"      