# Solution for LeetCode Problem 3206: Alternating Groups I
# Time Complexity: O(N), where N is the number of tiles (length of colors).
# Space Complexity: O(1), constant space used.

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        """
        Counts the number of alternating groups in a circular array of colored tiles.

        An alternating group is defined as 3 consecutive tiles (with circular wrapping),
        where the middle tile has a different color from both its neighbors:
            colors[i - 1], colors[i], colors[i + 1] form a group if:
                colors[i] != colors[i - 1] and colors[i] != colors[i + 1]

        Parameters:
        colors (List[int]): A circular list where colors[i] == 0 (red) or 1 (blue).

        Returns:
        int: The number of alternating groups in the circular array.
        """
        n = len(colors)
        ans = 0
        
        for i in range(n):
            prev = colors[(i - 1) % n]
            curr = colors[i]
            next = colors[(i + 1) % n]

            if curr != prev and curr != next:
                ans += 1

        return ans
