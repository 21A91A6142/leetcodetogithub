class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        k=[]
        for i in range(len(arr)):
            if arr.count(arr[i])==arr[i]:
                k.append(arr[i])
        if len(k)>0:
            return max(k)
        else:
            return -1
        