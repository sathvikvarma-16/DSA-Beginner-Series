class Solution:
    def romanToInt(self, s: str) -> int:
        values = {  # Store Roman symbols and their values
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0  # Store the final integer

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]  # Subtract if smaller value comes before larger
            else:
                total += values[s[i]]  # Otherwise, add the value
        return total  # Return the integer

  
"""
For example, s = "IV":
Current symbol: I → value 1
Next symbol: V → value 5
Is 1 < 5? Yes!
So we subtract I:
total -= 1
Then, when we reach V, we add 5.
Final result: -1 + 5 = 4.

Current < Next → subtract current value.
Current ≥ Next → add current value.
The last symbol has no next symbol, so we simply add it.
"""