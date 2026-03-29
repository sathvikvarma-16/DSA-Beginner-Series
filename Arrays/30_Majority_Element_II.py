"""
Problem: Majority Element II
Link: https://leetcode.com/problems/majority-element-ii/

Approach:
- Extension of Boyer-Moore Voting Algorithm.
- At most 2 elements can appear more than n/3 times.
- Maintain two candidates and their counts.
- First pass → find potential candidates.
- Second pass → verify their frequencies.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def majorityElement(nums):
    # Step 1: Find candidates
    count1 = count2 = 0
    candidate1 = candidate2 = None

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Step 2: Verify candidates
    result = []
    count1 = count2 = 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result  
