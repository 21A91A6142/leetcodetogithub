import math
def add(a,b):
        l1=0
        l2=0
        if(len(a)>=1 and len(b)>=1):
            for i in range(len(a)):
                if a[i]=="0":
                    l1+=1
            for i in range(len(b)):
                if b[i]=="1":
                    l2+=1
        return l1+l2
class Solution(object):
    def maxScore(self, s):
        a=[]
        s1=0
        for i in range(len(s)+2):
            left=s[0:i+1]
            right=s[i+1:len(s)+1]
            s1=add(left,right)
            a.append(s1)
        return max(a)