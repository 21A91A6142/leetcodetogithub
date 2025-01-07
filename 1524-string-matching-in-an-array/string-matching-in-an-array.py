class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=[]
        for i in range(len(words)):
            c=0
            for j in range(len(words)):
                if i!=j:
                    if words[i] in words[j]:
                        c+=1
            if c>0:
                a.append(words[i])
        return a
        
        