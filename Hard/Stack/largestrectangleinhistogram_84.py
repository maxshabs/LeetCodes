# Solution for LeetCode Problem 84: Largest Rectangle in Histogram
# Time Complexity: O(n), where n is the length of the input list `heights`
#   - Each bar is pushed to and popped from the stack at most once, making the overall time complexity linear.
# Space Complexity: O(n), due to the use of a stack that can store up to n indices in the worst case.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize the maximum area to 0
        max_area = 0

        # Stack to store indices of the histogram bars in increasing order of height
        current_indices = []

        # Length of the heights array
        len_heights = len(heights)

        # Iterate through the histogram, with an additional iteration to process remaining bars in the stack
        for i in range(len_heights + 1):
            # While the stack is not empty and the current height is less than or equal to the height at the top of the stack
            while current_indices and (i == len_heights or heights[current_indices[-1]] >= heights[i]):
                # Pop the top index and get the height of the bar at that index
                cur_height = heights[current_indices.pop()]

                # Calculate the width of the rectangle with the popped height
                if not current_indices:
                    width = i  # The rectangle extends from the start to the current index
                else:
                    width = i - current_indices[-1] - 1  # Width between the current index and the new top of the stack

                # Update the maximum area found so far
                max_area = max(max_area, cur_height * width)

            # Push the current index onto the stack
            current_indices.append(i)

        # Return the maximum rectangle area found
        return max_area
