# Solution for LeetCode Problem 2390: Removing Stars From a String
# Time Complexity: O(N), where N is the length of the string.
#   - We iterate through the string once, performing O(1) operations per character.
# Space Complexity: O(N), as we use a stack to store characters.

from typing import List

class Solution:
    def removeStars(self, s: str) -> str:
        """
        Removes stars from the string based on the following rule:
        - Each '*' removes the most recently added character (like a backspace).

        Parameters:
        s (str): The input string containing letters and '*' characters.

        Returns:
        str: The final string after removing stars.
        """
        stack = []  # Stack to store characters that are not removed

        # Iterate through each character in the string
        for char in s:
            if char == "*":
                stack.pop()  # Remove the last added character when encountering '*'
            else:
                stack.append(char)  # Append non-star characters to the stack

        return ''.join(stack)  # Convert stack back to a string and return
