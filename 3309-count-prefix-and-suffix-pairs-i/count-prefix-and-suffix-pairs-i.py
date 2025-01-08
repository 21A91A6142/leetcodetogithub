class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if len(words[i])>len(words[j]):
                    continue
                if words[i] == words[j][0:len(words[i])] and words[i]==words[j][len(words[j])-len(words[i]):len(words[j])]:
                    c+=1
        return c



        