class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0    # insertions made
        need = 0   # right parens still needed to close the open '('
        for c in s:
            if c == '(':
                # An odd 'need' means the previous '(' has only one ')'.
                # Insert one ')' to complete that pair first.
                if need % 2 == 1:
                    ans += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                # Unmatched ')' with no open '(': insert a '('
                # (which brings 2 needed, one of them used by this ')').
                if need < 0:
                    ans += 1
                    need += 2
        return ans + need