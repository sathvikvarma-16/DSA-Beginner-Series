from typing import List
from collections import Counter

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        answer = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                target_block = target[start:start + k]

                # The block must contain the correct elements.
                if Counter(block) != Counter(target_block):
                    valid = False
                    break

                # Count descents around the circular block.
                descents = 0

                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        descents += 1

                # A circularly sorted block has at most one descent.
                if descents > 1:
                    valid = False
                    break

            if valid:
                answer += k

        return answer