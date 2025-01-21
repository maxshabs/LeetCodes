# Solution for LeetCode Problem 134: Gas Station
# Time Complexity: O(n), where n is the number of gas stations. The algorithm iterates through the `gas` and `cost` arrays once.
# Space Complexity: O(1), as the solution uses only a few integer variables for calculations.

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if the total gas is less than the total cost; if so, return -1 (impossible to complete the circuit)
        if sum(gas) < sum(cost):
            return -1
        
        # Initialize variables to track the starting gas station and the current gas balance
        res = 0
        cur_sum = 0
        n = len(gas)
        
        # Iterate through all gas stations
        for i in range(n):
            # Update the current gas balance by adding gas and subtracting cost
            cur_sum = cur_sum + gas[i] - cost[i]
            
            # If the current gas balance drops below zero, reset it and update the starting station
            if cur_sum < 0:
                cur_sum = 0
                res = i + 1
        
        # Return the starting gas station index
        return res
