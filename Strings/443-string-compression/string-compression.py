class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0
        index = 0

        while i < len(chars):

            j = i

            # Count same characters
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            # Write the character
            chars[index] = chars[i]
            index += 1

            # Write count if greater than 1
            count = j - i

            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1

            i = j

        return index