# Solution for LeetCode Problem 121: Best Time to Buy and Sell Stock
# Time Complexity: O(n), where n is the length of the input list `prices`
#   - The algorithm iterates through the list once.
# Space Complexity: O(1), as only two variables (`max_profit` and `min_price`) are used.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the maximum profit to 0
        max_profit = 0

        # Initialize the minimum price to the first price in the list
        min_price = prices[0]

        # Iterate through each price in the list
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price

            # Calculate the profit and update max_profit if the current profit is greater
            if max_profit < price - min_price:
                max_profit = price - min_price

        # Return the maximum profit found
        return max_profit
