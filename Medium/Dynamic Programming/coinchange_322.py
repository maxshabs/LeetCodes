# Solution for LeetCode Problem 322: Coin Change
# Time Complexity: O(n * m), where n is the `amount` and m is the number of coins in the `coins` list.
# Space Complexity: O(n), where n is the `amount`, due to the `arr` array used to store intermediate results.

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Finds the fewest number of coins needed to make up a given amount using the provided denominations.

        :param coins: List of integers representing coin denominations.
        :param amount: Integer representing the target amount.
        :return: The fewest number of coins needed to make up the amount, or -1 if it is not possible.
        """
        arr = [amount + 1] * (amount + 1)  # Initialize the array with an impossible high value.
        arr[0] = 0  # Base case: 0 coins are needed to make up amount 0.
        
        for current_amount in range(1, amount + 1):
            for coin in coins:
                if current_amount - coin >= 0:  # Ensure we are within bounds.
                    arr[current_amount] = min(arr[current_amount], arr[current_amount - coin] + 1)
        
        # If no solution exists, return -1; otherwise, return the minimum number of coins for `amount`.
        if arr[amount] == amount + 1:
            return -1
        return arr[amount]
