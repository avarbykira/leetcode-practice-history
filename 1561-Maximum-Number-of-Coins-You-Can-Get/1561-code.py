class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        l = len(piles)
        
        piles.sort()
        
        num = 0
        for i in range(0, (l/3)-1):
            num += piles[l/3 + 2*i]

        return num
