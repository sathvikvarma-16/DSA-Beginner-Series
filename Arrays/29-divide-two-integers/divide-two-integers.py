class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Special overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        # Determine the sign of the answer
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        # Keep subtracting the largest possible doubled divisor
        while dividend >= divisor:
            value = divisor
            count = 1
            while dividend >= value + value:
                value += value
                count += count
            dividend -= value
            quotient += count
        # Apply the sign
        if negative:
            quotient = -quotient
        return quotient