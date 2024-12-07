# Solution for LeetCode Problem 347: Top K Frequent Elements
# Time Complexity: O(n), where n is the length of the input list `nums`
#   - Building the frequency dictionary takes O(n).
#   - Creating and filling the frequency list takes O(n).
#   - Collecting the top k elements takes O(n) in the worst case.
# Space Complexity: O(n), as we store the frequency of each element and use a list to group elements by frequency.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build a frequency dictionary to count the occurrences of each number
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)

        # Step 2: Create a list of empty lists to group numbers by their frequencies
        # The index represents the frequency count
        freq_list = []
        for i in range(len(nums) + 1):
            freq_list.append([])

        # Step 3: Populate the frequency list with numbers based on their frequency
        for number, count in count_dict.items():
            freq_list[count].append(number)

        # Step 4: Collect the top k frequent elements from the frequency list
        top_k = []
        for i in range(len(freq_list) - 1, 0,
                       -1):  # Iterate from the highest frequency to the lowest
            for number in freq_list[i]:
                top_k.append(number)
                k -= 1
                if k == 0:
                    return top_k
