class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            result = []

            for ch in string:
                if ch != "#":
                    result.append(ch)
                elif result:
                    result.pop()

            return "".join(result)

        return build(s) == build(t)