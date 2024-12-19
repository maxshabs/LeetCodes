# Solution for LeetCode Problem 22: Generate Parentheses
# Time Complexity: O(4^n / sqrt(n)), which is the Catalan number for n pairs of parentheses
#   - This is the number of valid combinations of balanced parentheses.
# Space Complexity: O(n), due to the depth of the recursion stack (maximum depth is `n`).
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Stack to store the current combination of parentheses
        stack = []

        # List to store all valid combinations
        res = []

        # Helper function to generate parentheses recursively
        def recursive(open_paren, closed_paren):
            # Base case: when the number of open and closed parentheses equals n
            if open_paren == closed_paren == n:
                res.append("".join(stack))  # Add the current valid combination to the result
                return

            # If the number of open parentheses used is less than n, add an open parenthesis
            if open_paren < n:
                stack.append("(")
                recursive(open_paren + 1, closed_paren)
                stack.pop()  # Backtrack to explore other possibilities

            # If the number of open parentheses is greater than the number of closed, add a closed parenthesis
            if open_paren > closed_paren:
                stack.append(")")
                recursive(open_paren, closed_paren + 1)
                stack.pop()  # Backtrack to explore other possibil
