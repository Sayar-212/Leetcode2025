from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:  # possible to place here
                # check left and right neighbors
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == length-1) or (flowerbed[i+1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1   # place a flower here
                    count += 1
                    if count >= n:     # already placed enough
                        return True
        
        return count >= n
