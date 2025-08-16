class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num1=""
        c=0
        num2=str(num)
        for i in num2:
            if i=='6' and c==0:
                num1+='9'
                c+=1
            else:
                num1+=i
        return int(num1)