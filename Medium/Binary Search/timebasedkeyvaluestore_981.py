# Solution for LeetCode Problem 981: Time Based Key-Value Store
# Time Complexity:
#   - `set`: O(1), as appending to a list is constant time.
#   - `get`: O(log n), where n is the number of timestamps for a given key (binary search is used).
# Space Complexity: O(n), where n is the total number of key-value pairs stored.

class TimeMap:

    def __init__(self):
        # Dictionary to store keys mapping to a list of (value, timestamp) pairs
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key does not exist, initialize an empty list for it
        if key not in self.keyStore:
            self.keyStore[key] = []
        # Append the (value, timestamp) pair to the key's list
        self.keyStore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # If the key does not exist, return an empty string
        if key not in self.keyStore:
            return ""
        
        # Retrieve the list of (value, timestamp) pairs for the given key
        value_list = self.keyStore[key]
        left, right = 0, len(value_list) - 1
        current_max = ""  # Variable to store the most recent value at or before the timestamp

        # Perform binary search
        while left <= right:
            middle = (left + right) // 2
            cur_timestamp = value_list[middle][1]

            # If the exact timestamp is found, return the corresponding value
            if cur_timestamp == timestamp:
                return value_list[middle][0]
            
            # If the current timestamp is greater than the target, search the left half
            if cur_timestamp > timestamp:
                right = middle - 1
            # If the current timestamp is less than or equal to the target, update `current_max`
            # and search the right half
            else:
                current_max = value_list[middle][0]
                left = middle + 1

        # Return the most recent value at or before the given timestamp
        return current_max
