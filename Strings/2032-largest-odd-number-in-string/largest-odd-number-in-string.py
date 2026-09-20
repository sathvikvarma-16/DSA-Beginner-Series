class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):  # Check digits from right to left
            if int(num[i]) % 2 == 1:  # If the digit is odd
                return num[:i + 1]  # Return substring ending at this digit
        return ""  # Return empty string if no odd digit exists