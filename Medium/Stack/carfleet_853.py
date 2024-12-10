# Solution for LeetCode Problem 853: Car Fleet
# Time Complexity: O(n log n), where n is the number of cars.
#   - Sorting the `comb_arr` takes O(n log n).
#   - Iterating through the sorted list takes O(n).
# Space Complexity: O(n), for storing the combined `comb_arr` list and the `fleet_stack`.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Initialize a stack to keep track of the fleets
        fleet_stack = []

        # Step 1: Combine position and speed into tuples and sort by position in descending order
        comb_arr = []
        n = len(position)
        for i in range(n):
            comb_arr.append((position[i], speed[i]))
        comb_arr.sort(reverse=True)  # Sort cars by starting position in descending order

        # Step 2: Iterate through the sorted list and determine car fleets
        for pos, s in comb_arr:
            # Calculate the time it takes for the car to reach the target
            time = (target - pos) / s

            # If the stack is empty or the current car takes more time than the last car in the stack,
            # it forms a new fleet
            if not fleet_stack or fleet_stack[-1] < time:
                fleet_stack.append(time)

        # The number of fleets is the length of the stack
        return len(fleet_stack)
