# Solution for LeetCode Problem 9: Palindrome Number
# Time Complexity: O(n), where n is the number of digits in the integer `x`. The algorithm processes each digit once.
# Space Complexity: O(1), as the solution does not use any extra space proportional to the size of the input.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # A negative number cannot be a palindrome
        if x < 0:
            return False
        
        # Store the original number for comparison
        original = x
        new = 0
        
        # Reverse the digits of the number
        while x > 0:
            new = new * 10 + x % 10  # Add the last digit of `x` to `new`
            x //= 10  # Remove the last digit of `x`
        
        # Check if the reversed number is equal to the original
        return new == original
