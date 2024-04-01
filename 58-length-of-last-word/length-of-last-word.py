class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=[]
        c=0
        for i in s:
            if i==" ":
                a.append(c)
                c=0
                continue
            else:
                c+=1
        a.append(c)
        for i in range(len(a)-1,-1,-1):
            if a[i]>0:
                return (a[i])
                break

