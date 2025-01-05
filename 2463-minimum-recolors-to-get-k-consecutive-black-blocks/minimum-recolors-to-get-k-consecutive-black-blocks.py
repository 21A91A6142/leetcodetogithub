class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        k1=[]
        for i in range(len(blocks)-k+1):
            s=blocks[i:i+k]
            k1.append(k-s.count('B'))
        return min(k1)
        