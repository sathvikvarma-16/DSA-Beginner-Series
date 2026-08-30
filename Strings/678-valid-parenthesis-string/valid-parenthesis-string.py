class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for ch in s:
            if ch == '(':  
                low += 1   # low = minimum possible open brackets
                high += 1  # high = maximum possible open brackets
            elif ch == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1
                high += 1
            if high < 0:
                # high < 0 => That means even the maximum possible balance became negative.
                # So there are too many ).
                # Immediately : return False
                return False
            low = max(0, low)
            # Suppose: low = -1 => 
            # That just means we chose * as ) when there weren't enough open brackets.
            # We can instead treat that * as empty.
        return low == 0