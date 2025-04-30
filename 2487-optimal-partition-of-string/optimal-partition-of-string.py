class Solution:
    def partitionString(self, s: str) -> int:
        s1=""
        c=0
        for i in s:
            if i not in s1:
                s1+=i
            else:
                print(s1)
                c+=1
                s1=""
                s1+=i
        return c+1
        