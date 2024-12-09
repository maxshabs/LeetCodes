# Solution for LeetCode Problem 739: Daily Temperatures
# Time Complexity: O(n), where n is the length of the input list `temperatures`
#   - Each temperature is pushed to and popped from the stack at most once, making it linear.
# Space Complexity: O(n), as the worst-case scenario requires storing all indices on the stack.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack to keep track of indices of temperatures in decreasing order
        mono_stack = []

        # Result list initialized with zeros, same length as temperatures
        res = [0] * len(temperatures)

        # Iterate through the temperatures list with their indices
        for index, temp in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the temperature
            # at the index stored at the top of the stack, update the result
            while mono_stack and temperatures[mono_stack[-1]] < temp:
                # Pop the index from the stack and calculate the days to wait
                x = mono_stack.pop()
                res[x] = index - x

            # Push the current index onto the stack
            mono_stack.append(index)

        # Return the result list
        return res
