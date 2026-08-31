class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        # Remaining characters in typed must all be long presses
        while j < len(typed):
            if typed[j] != typed[j - 1]:
                return False
            j += 1

        return i == len(name)
        

        