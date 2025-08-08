from functools import lru_cache
import math

class Solution:
    def soupServings(self, n: int) -> float:
        # If n is large enough, the probability converges to 1.
        if n >= 4800:
            return 1.0

        # Convert to units of 25 mL (ceiling)
        units = (n + 24) // 25

        @lru_cache(None)
        def prob(a: int, b: int) -> float:
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            # four possible operations (in units)
            return 0.25 * (
                prob(a - 4, b) +
                prob(a - 3, b - 1) +
                prob(a - 2, b - 2) +
                prob(a - 1, b - 3)
            )

        return prob(units, units)
