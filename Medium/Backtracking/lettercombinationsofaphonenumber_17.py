# Solution for LeetCode Problem 17: Letter Combinations of a Phone Number
# Time Complexity: O(4^n * n), where n is the length of the input digits.
# Space Complexity: O(n) for recursion stack.

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generates all possible letter combinations that the input digits could represent.

        :param digits: A string containing digits from '2' to '9'.
        :return: A list of all possible letter combinations.
        """
        # Mapping of digits to corresponding letters
        number_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        result = []  # List to store the combinations
        combination = []  # Temporary list to build each combination

        if not digits:
            return result  # If no digits are provided, return an empty list
        
        def recursive(i: int):
            """
            Backtracking function to generate combinations.

            :param i: Current index in the input digits string.
            """
            # Base case: If we've processed all digits, add the combination to results
            if i == len(digits):
                result.append("".join(combination))  # Append current combination as a string
                return
            
            cur_digit = digits[i]  # Current digit to process
            app_list = number_dict[cur_digit]  # Get the corresponding letters
            
            # Iterate through each letter corresponding to the current digit
            for char in app_list:
                combination.append(char)  # Add the letter to the current combination
                recursive(i + 1)  # Recurse for the next digit
                combination.pop()  # Backtrack to explore other combinations
        
        # Start recursive exploration from the first digit
        recursive(0)
        return result
