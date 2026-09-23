class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0  # Store the reversed bits
        for i in range(32):  # Process all 32 bits
            bit = n & 1  # Get the last bit of n
            ans = (ans << 1) | bit  # Shift ans left and add the bit
            n >>= 1  # Remove the last bit from n
        return ans  # Return the reversed integer