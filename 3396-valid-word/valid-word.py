class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vo=0
        con=0
        dig=0
        vowels="aeiouAEIOU"
        if len(word)<3:
            return False
        for i in word:
            if i.isalpha():
                if i in vowels:
                    vo+=1
                else:
                    con+=1
            elif i.isdigit():
                dig+=1
            else:
                return False
        if vo>=1 and con>=1 and (con+vo+dig==len(word)):
            return True
        else:
            return False

        