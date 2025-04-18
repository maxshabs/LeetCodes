# Solution for LeetCode Problem 38: Count and Say
# Time Complexity: O(n * m), where n is the number of iterations and m is the length of the strings generated
# Space Complexity: O(m), for storing the temporary result at each step

class Solution:
    def countAndSay(self, n: int) -> str:
        cur_str = "1"  # Starting string for n = 1

        # Generate the sequence iteratively from 1 to n
        for _ in range(n - 1):
            cur_counter = 1  # Count occurrences of the current digit
            temp = []        # Temporary list to build the next string

            # Go through the string from left to right
            for i in range(1, len(cur_str)):
                if cur_str[i] == cur_str[i - 1]:
                    cur_counter += 1  # Continue counting the same digit
                else:
                    # Append count and digit (e.g., "21" means "two 1s")
                    temp.append(str(cur_counter))
                    temp.append(cur_str[i - 1])
                    cur_counter = 1  # Reset counter for the new digit

            # Don't forget to append the last group
            temp.append(str(cur_counter))
            temp.append(cur_str[-1])

            # Prepare for the next iteration
            cur_str = "".join(temp)

        return cur_str
