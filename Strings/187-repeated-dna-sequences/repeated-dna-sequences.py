class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        count = {}  # Store how many times each sequence appears
        ans = []
        for i in range(len(s) - 9):  # Every substring must have length 10
            word = s[i:i + 10]  # Take 10 characters
            if word in count:
                count[word] += 1  # Increase its count
                if count[word] == 2:  # Add it only when it repeats first time
                    ans.append(word)
            else:
                count[word] = 1  # First occurrence
        return ans