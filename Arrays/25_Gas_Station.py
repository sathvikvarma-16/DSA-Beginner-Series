"""
Problem: Gas Station
Link: https://leetcode.com/problems/gas-station/

Approach:
- If total gas < total cost → impossible → return -1.
- Traverse and maintain current tank.
- If tank becomes negative → reset start to next index.
- Greedy approach ensures valid start.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def canCompleteCircuit(gas, cost):
    total_tank = 0
    current_tank = 0
    start_index = 0

    for i in range(len(gas)):
        # Net gas at this station
        diff = gas[i] - cost[i]

        total_tank += diff
        current_tank += diff

        # If current tank becomes negative → cannot start from previous
        if current_tank < 0:
            start_index = i + 1
            current_tank = 0

    # If total gas is enough → return start index
    return start_index if total_tank >= 0 else -1
