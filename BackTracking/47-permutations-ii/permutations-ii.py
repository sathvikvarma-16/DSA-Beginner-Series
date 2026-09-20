class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans, sol = [], []  # ans stores answers; sol builds one permutation
        nums.sort()  # Put duplicate numbers next to each other
        n = len(nums)
        used = [False] * n  # Track which positions we have chosen

        def backtrack():
            if len(sol) == n:  # If all numbers are chosen
                ans.append(sol[:])  # Save a copy of this permutation
                return

            for i in range(n):  # Try every position
                if used[i]:  # Skip a number already chosen
                    continue

                # Skip duplicate choices to avoid repeated permutations
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                sol.append(nums[i])  # Choose this number
                used[i] = True  # Mark its position as used

                backtrack()  # Explore the next position

                sol.pop()  # Undo the choice
                used[i] = False  # Mark its position as unused

        backtrack()  # Start generating permutations
        return ans  # Return all unique permutations

"""
used = [False] * n

In LeetCode 46, we checked:
if x not in sol:
But with duplicate numbers, that check cannot distinguish between the two 1s.
For example, we need to be able to choose the first 1 and then choose the second 1. So instead, we track which position we have chosen.

For nums = [1, 1, 2]:
Index:  0      1      2
Value:  1      1      2
used = [False, False, False]
used[0] = True means we chose the 1 at index 0.
used[1] = True means we chose the 1 at index 1.
used[2] = True means we chose the 2.
This lets us choose both 1s, while making sure we don't choose the same position twice.
"""
       
"""
if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:

Let's break it into simple parts:

i > 0 → make sure there is a previous position.
nums[i] == nums[i - 1] → check whether this number is the same as the previous number.
not used[i - 1] → check whether the previous copy has not been chosen in the current permutation.
continue → skip this choice.

In simple words: If two numbers are equal, we choose the earlier copy first. We skip the later copy when the earlier copy hasn't been used yet.

This avoids creating the same arrangement in two different ways.

1. Imagine we haven't chosen anything yet
sol = []
used = [False, False, False]

The loop tries index 0 first.

It chooses the first 1:

sol = [1]
used = [True, False, False]

Now it can choose the second 1, because the first 1 has already been chosen. That is how we can make:

[1, 1, 2]

Choosing the second 1 after the first 1 is allowed.

2. Now imagine we go back to the beginning

Backtracking removes the first 1:

sol = []
used = [False, False, False]

Now the loop tries index 1, which is the second 1.

Check the condition:

if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue

For index 1:

i > 0                   → True
nums[1] == nums[0]      → 1 == 1 → True
not used[0]             → not False → True

All three parts are True, so continue skips this choice.

Why skip it?

Because choosing the second 1 first would give us the same arrangements as choosing the first 1 first.

For example, these two choices look different by index:

Choose index 0 first → [1, ...]
Choose index 1 first → [1, ...]

But both start with the exact same value, 1. So the second choice would repeat the same permutations.
"""


"""
Sort the numbers.
Put equal numbers next to each other so we can identify duplicates easily.
Create an empty list sol.
This stores the permutation we are currently building.
Create an empty list ans.
This stores all the completed, unique permutations.
Create a used list.
It tells us whether each position in nums has already been chosen for the current permutation.
Try each number one by one.
If its position is already used, skip it.
Avoid choosing duplicate numbers in the same order.
If the current number is equal to the previous number, skip it when the previous copy has not been used yet. This prevents generating the same permutation more than once.
Choose the number.
Add it to sol and mark its position as used.
Call the backtracking function again.
Continue choosing numbers until the permutation is complete.
Save the permutation.
When sol contains all the numbers, add a copy of it to ans.
Backtrack.
Remove the last chosen number and mark its position as unused, so we can try another choice.
Return the answer.
Once all choices have been explored, return ans.
"""