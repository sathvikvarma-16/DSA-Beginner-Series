class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        score = 0
        ans = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                ans = max(ans, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return ans

"""
You have:
tokens = [100, 200, 300, 400]
power = 200
Each token has a value.
You have 2 choices for a token:

1. Play token face up
Pay its value from your power:
power -= token
score += 1
Example:
power = 200
token = 100
power = 100
score = 1

2. Play token face down
You get power, but lose 1 score:
power += token
score -= 1
You do this only when you need more power.
What is the goal?
Get the maximum possible score.
Greedy idea
Sort the tokens:
[100, 200, 300, 400]
Use two pointers:
left  → smallest token
right → largest token
When you have enough power
Use the smallest token:
power >= tokens[left]
Then:
power -= tokens[left]
score += 1
left += 1
Why smallest?
We want to spend as little power as possible to gain 1 score.
When you don't have enough power
Use the largest token face down:
power += tokens[right]
score -= 1
right -= 1

Why largest?
We sacrifice 1 score, so we want to get as much power as possible.
"""