class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word='a'
        while(len(word)<=k):
            new_word=word
            for i in range(len(word)):
                if ord(word[i])==122:
                    new_word+='a'
                else:
                    new_word+=chr(ord(word[i])+1)
            word=new_word
        return word[k-1]

        