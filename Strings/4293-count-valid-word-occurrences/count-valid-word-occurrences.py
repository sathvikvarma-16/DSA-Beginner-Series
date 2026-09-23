class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = ""
        for chunk in chunks:
            s += chunk  # Join chunks manually

        words = {}
        word = ""
        i = 0

        while i < len(s):
            ch = s[i]

            if ch.isalpha():
                word += ch
            elif ch == "-" and word != "" and i + 1 < len(s) and s[i + 1].isalpha():
                word += ch  # Keep a single hyphen between letters
            else:
                if word != "":
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
                    word = ""

            i += 1

        if word != "":  # Count the final word
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

        ans = []
        for q in queries:
            if q in words:
                ans.append(words[q])
            else:
                ans.append(0)

        return ans