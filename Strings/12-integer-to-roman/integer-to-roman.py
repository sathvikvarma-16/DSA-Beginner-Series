class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans = ""  # Store the Roman numeral
        for i in range(len(values)):  # Check each Roman value
            while num >= values[i]:  # Use this value while possible
                ans += symbols[i]  # Add its Roman symbol
                num -= values[i]  # Subtract its value from num
        return ans  # Return the Roman numeral