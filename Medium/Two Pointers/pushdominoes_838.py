# Solution for LeetCode Problem 838: Push Dominoes
# Time Complexity: O(n), where n is the length of the input string
# Space Complexity: O(n), for the result list

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Add virtual 'L' to the start and 'R' to the end to handle boundaries uniformly
        dominoes = "L" + dominoes + "R"
        result = []      # List to build final state efficiently
        prev = 0         # Pointer to track the position of the last non-dot character (L or R)

        for cur in range(1, len(dominoes)):
            if dominoes[cur] == ".":
                continue  # Skip until we find a non-dot

            range_between = cur - prev - 1  # Number of dominoes between two non-dot characters

            if prev > 0:
                result.append(dominoes[prev])  # Append the last push (if it's not the virtual 'L' at start)

            # Case 1: Same direction (e.g., L...L or R...R)
            if dominoes[prev] == dominoes[cur]:
                result.append(dominoes[prev] * range_between)

            # Case 2: Opposite forces (R...L)
            elif dominoes[prev] == "R" and dominoes[cur] == "L":
                half = range_between // 2
                result.append("R" * half)
                if range_between % 2:
                    result.append(".")  # The middle one stays upright
                result.append("L" * half)

            # Case 3: Inward forces (L...R) → no effect on dots between
            else:
                result.append("." * range_between)

            prev = cur  # Move the previous pointer

        return ''.join(result)
