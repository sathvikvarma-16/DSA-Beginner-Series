class Solution:
    def myPow(self, x: float, n: int) -> float:
        # If exponent is negative, take reciprocal
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            # If n is odd, multiply current x into answer
            if n % 2 == 1:
                ans *= x
            # Square x for the next power
            x *= x
            # Divide exponent by 2
            n //= 2
        return ans