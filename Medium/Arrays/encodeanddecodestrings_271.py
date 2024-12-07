# Solution for LeetCode Problem 271: Encode and Decode Strings
# Time Complexity:
#   - `encode`: O(n), where n is the total length of all strings in `strs`
#   - `decode`: O(n), where n is the length of the encoded string `s`
# Space Complexity:
#   - `encode`: O(n), for storing the encoded string
#   - `decode`: O(n), for storing the list of decoded strings

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # Initialize an empty string to store the encoded result
        ret_str = ""

        # Iterate through each word in the input list
        for word in strs:
            # Append the length of the word, followed by a '#', and the word itself
            ret_str += str(len(word)) + "#" + word

        # Return the final encoded string
        return ret_str

    def decode(self, s: str) -> List[str]:
        # Initialize an empty list to store the decoded strings
        res = []
        i = 0

        # Iterate through the encoded string
        while i < len(s):
            # Find the position of the '#' character to determine the length of the current word
            j = i
            while s[j] != '#':
                j += 1

            # Convert the substring representing the length to an integer
            length = int(s[i:j])

            # Move the pointer `i` to the start of the word (after the '#')
            i = j + 1

            # Extract the word using the length and add it to the result list
            j = i + length
            res.append(s[i:j])

            # Move the pointer `i` to the next encoded segment
            i = j

        # Return the list of decoded strings
        return res
