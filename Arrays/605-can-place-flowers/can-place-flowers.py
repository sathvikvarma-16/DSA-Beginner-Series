class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        At every position, check three things:

Current position is 0
Left side is empty or doesn't exist
Right side is empty or doesn't exist
"""
        for i in range(len(flowerbed)):          
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):        
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0
        