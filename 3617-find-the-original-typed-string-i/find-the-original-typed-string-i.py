class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        s=0
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                s+=1
        return s+1
