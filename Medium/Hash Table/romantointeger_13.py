# Solution for LeetCode Problem 13: Roman to Integer
# Time Complexity: O(N), where N is the length of the input string s.
#   - We traverse the string once, performing O(1) operations per character.
# Space Complexity: O(1), as we use a fixed-size dictionary and a few integer variables.

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        Parameters:
        s (str): A string representing a Roman numeral.

        Returns:
        int: The integer equivalent of the given Roman numeral.
        """
        # Dictionary to map Roman numerals to their integer values
        roman_to_int = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        res = 0  # Variable to store the final integer result

        # Iterate through the string with a sliding window of size 2
        for i, j in zip(s, s[1:]):
            if roman_to_int[i] < roman_to_int[j]:  # If a smaller numeral appears before a larger one
                res -= roman_to_int[i]  # Subtract the value (e.g., IV = 4 → -1 + 5)
            else:
                res += roman_to_int[i]  # Otherwise, add the value

        # Add the last character, as it was not included in the loop
        return res + roman_to_int[s[-1]]
