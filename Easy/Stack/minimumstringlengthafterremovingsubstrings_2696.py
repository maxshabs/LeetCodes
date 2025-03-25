# Solution for LeetCode Problem 2696: Minimum String Length After Removing Substrings
# Time Complexity: O(N), where N is the length of the input string `s`.
#   - Each character is pushed and popped from the stack at most once.
# Space Complexity: O(N), for the stack that stores characters.

class Solution:
    def minLength(self, s: str) -> int:
        """
        Removes all instances of the substrings "AB" and "CD" from the input string `s` using a stack-based approach.

        The operation is:
        - Whenever "AB" or "CD" appears as adjacent characters, they can be removed.
        - This removal continues until no more such substrings are left.
        
        Parameters:
        s (str): The input string consisting of uppercase English letters.

        Returns:
        int: The minimum length of the string after repeatedly removing all "AB" and "CD" substrings.
        """
        stack = []

        # Process each character in the input string
        for char in s:
            # Check if the top of the stack + current char form "AB"
            if char == "B" and stack and stack[-1] == "A":
                stack.pop()  # Remove the "A", skip adding "B" → effectively remove "AB"
            # Check if the top of the stack + current char form "CD"
            elif char == "D" and stack and stack[-1] == "C":
                stack.pop()  # Remove the "C", skip adding "D" → effectively remove "CD"
            else:
                # No match found, push the character onto the stack
                stack.append(char)

        return len(stack)  # Remaining characters are not removable
