# Solution for LeetCode Problem 394: Decode String
# Time Complexity: O(N), where N is the length of the input string.
#   - Each character is processed once and added/removed from the stack at most once.
# Space Complexity: O(N), as we use a stack to store intermediate values.

from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decodes an encoded string where patterns of the form "k[encoded_string]"
        are expanded to repeat `encoded_string` k times.

        Parameters:
        s (str): The encoded string.

        Returns:
        str: The fully decoded string.
        """
        stack = []  # Stack to store characters and partial results
        
        for char in s:
            if char != "]":
                stack.append(char)  # Push characters onto the stack
            else:
                # Step 1: Retrieve the encoded substring inside brackets
                cur_str = ""
                while stack and stack[-1] != "[":
                    cur_str = stack.pop() + cur_str  # Build the substring in reverse order
                
                stack.pop()  # Remove the opening "["

                # Step 2: Retrieve the number preceding the brackets
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num  # Extract the full digit

                num = int(num)  # Convert the extracted number to an integer

                # Step 3: Expand the string and push it back to the stack
                stack.append(num * cur_str)  # Repeat the substring `num` times
        
        return "".join(stack)  # Construct the final decoded string
