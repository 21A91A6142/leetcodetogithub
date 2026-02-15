class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        st=""

        for i in range(len(words)):
            wordsum=0
            for j in words[i]:
                wordsum+=weights[ord(j)%97]
            st+=chr(122-(wordsum%26))
        return st
            
