# Solution for LeetCode Problem 678: Valid Parenthesis String
# Time Complexity: O(n), where n is the length of the input string `s`.
# Space Complexity: O(1), as the solution uses constant extra space.

class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0  # Variables to track the range of possible open parentheses
        
        for char in s:
            if char == "(":  # Open parenthesis increases both minimum and maximum counts
                left_min += 1
                left_max += 1
            elif char == "*":  # Asterisk can act as open parenthesis, close parenthesis, or empty
                if left_min > 0:   
                    left_min -= 1  # Decrease minimum count if there are open parentheses
                left_max += 1      # Increase maximum count since '*' can act as '('
            else:  # Close parenthesis
                if left_min > 0:   
                    left_min -= 1  # Decrease minimum count if there are open parentheses
                left_max -= 1      # Decrease maximum count

            # If at any point `left_max` is negative, it means there are too many unmatched ')' 
            if left_max < 0:
                return False
        
        # If `left_min` is zero at the end, it means all open parentheses can be matched
        return not left_min
