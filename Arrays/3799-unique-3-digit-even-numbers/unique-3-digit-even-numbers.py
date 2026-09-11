class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        k = 3
        ans = set()
        def generate(current, used):
            if len(current) == k:
                if current[0] != 0 and current[2] % 2 == 0:
                    num = current[0] * 100 + current[1] * 10 + current[2]
                    ans.add(num)
                return
            for i in range(len(digits)):
                if i not in used:
                    used.add(i)
                    current.append(digits[i])
                    generate(current, used)
                    current.pop()
                    used.remove(i)
        generate([], set())
        return len(ans)