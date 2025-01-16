# Solution for LeetCode Problem 2614: Prime Number in Diagonal
# Time Complexity: O(n*√m), where n is the size of the matrix (number of diagonal elements),
#                  and m is the maximum value in the matrix (for prime checking).
# Space Complexity: O(1), as we use a constant amount of extra space.

from typing import List

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        largest_prime = 0  # To store the largest prime number found
        nums_len = len(nums)  # Length of the square matrix
        
        # Iterate through both diagonals of the matrix
        for i in range(nums_len):
            # Check the primary diagonal element
            if nums[i][i] > largest_prime and self.isPrime(nums[i][i]):
                largest_prime = nums[i][i]
            
            # Check the secondary diagonal element
            if nums[i][nums_len - i - 1] > largest_prime and self.isPrime(nums[i][nums_len - i - 1]):
                largest_prime = nums[i][nums_len - i - 1]
        
        return largest_prime  # Return the largest prime found
    
    def isPrime(self, num: int) -> bool:
        if num <= 1:  # Numbers less than or equal to 1 are not prime
            return False
        
        # Check divisibility up to the square root of the number
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False  # Not a prime number
        
        return True  # The number is prime
