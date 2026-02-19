class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in bulbs:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
        return sorted(l)        