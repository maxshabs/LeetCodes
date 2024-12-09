# Solution for LeetCode Problem 150: Evaluate Reverse Polish Notation
# Time Complexity: O(n), where n is the number of tokens in the input list `tokens`
#   - Each token is processed once, and stack operations (push and pop) are O(1).
# Space Complexity: O(n), as we may need to store up to n numbers on the stack in the worst case.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize a stack to store numbers during the evaluation
        num_stack = []

        # Iterate through each token in the input list
        for token in tokens:
            if token == "+":
                # Pop the last two numbers, add them, and push the result back to the stack
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif token == "-":
                # Pop the last two numbers, subtract them (x - y), and push the result
                y = num_stack.pop()
                x = num_stack.pop()
                num_stack.append(x - y)
            elif token == "*":
                # Pop the last two numbers, multiply them, and push the result
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif token == "/":
                # Pop the last two numbers, divide them (x / y), and push the result
                # Use int() to truncate towards zero for division
                y = num_stack.pop()
                x = num_stack.pop()
                num_stack.append(int(x / y))
            else:
                # If the token is a number, convert it to an integer and push it onto the stack
                num_stack.append(int(token))

        # The final result is the last remaining element on the stack
        return num_stack.pop()
