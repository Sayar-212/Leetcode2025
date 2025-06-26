class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Initialize answer and the binary number value
        ans = 0  # Will store the longest subsequence length
        val = 0  # Will store the value of the current subsequence in binary
        power = 1  # Represents the current power of 2 (starting from the least significant bit)
        
        # Traverse the string from right to left (least significant bit to most)
        for ch in reversed(s):
            # If the character is '0', always safe to include it
            if ch == '0':
                ans += 1
                # No change to val or power, move to next bit
            else:
                # If including this '1' does not exceed k, include it
                if val + power <= k:
                    val += power  # Add current power to val
                    ans += 1  # Increase subsequence length
                # If not, skip this '1'
            # Update power for next bit (move left)
            power *= 2
            # If power exceeds k, no point in adding higher bits
            if power > k:
                # After this, only zeros can be included
                break
        
        # After the main loop, count all remaining zeros on the left
        for ch in s[:len(s)-ans]:
            if ch == '0':
                ans += 1
        
        return ans  # Return the result
