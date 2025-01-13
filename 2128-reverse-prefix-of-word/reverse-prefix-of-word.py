class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch in word:
            k=word.index(ch)
            s=word[0:k+1]
            s1=word[k+1:]
            return (s[::-1]+s1)
        else:
            return word
        