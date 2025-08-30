from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the current maximum candies any kid has
        max_candies = max(candies)
        
        # For each kid, check if they can reach or exceed max_candies
        return [c + extraCandies >= max_candies for c in candies]
