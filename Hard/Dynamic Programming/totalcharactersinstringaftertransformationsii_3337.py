# Solution for LeetCode Problem 3337: Length of Transformed String II
# Time Complexity: O(26^3 * log t + len(s)), due to matrix exponentiation and string scan
# Space Complexity: O(26^2), for transformation and frequency matrices

from typing import List

class Solution:
    MOD = 10 ** 9 + 7

    # Multiplies two matrices A and B under modulo MOD
    def multiplyMatrices(self, A, B):
        rows_a, cols_a = len(A), len(A[0])
        cols_b = len(B[0])
        multiplication = [[0] * cols_b for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                temp = 0
                for k in range(cols_a):
                    temp += A[i][k] * B[k][j]
                multiplication[i][j] = temp % self.MOD
        return multiplication

    # Computes matrix exponentiation: matrix^exp using binary exponentiation
    def powerMatrix(self, matrix, exp):
        n = len(matrix)
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        while exp > 0:
            if exp & 1:
                result = self.multiplyMatrices(result, matrix)
            matrix = self.multiplyMatrices(matrix, matrix)
            exp >>= 1
        return result
                
    # Main function to compute the length after t transformations
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Build the transformation matrix based on the rules in nums
        # Each transform[i][j] tells how many times character i transforms to j
        transform = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for shift in range(nums[i]):
                transform[i][(i + 1 + shift) % 26] += 1

        # Raise the transformation matrix to the t-th power
        transform = self.powerMatrix(transform, t)

        # Build the initial frequency vector from string s
        freq = [[0] * 26]
        for c in s:
            freq[0][ord(c) - ord('a')] += 1

        # Multiply frequency vector by the transformation matrix
        freq = self.multiplyMatrices(freq, transform)

        # The result is the total number of characters after all transformations
        return sum(freq[0]) % self.MOD
