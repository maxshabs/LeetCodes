# Solution for LeetCode Problem 146: LRU Cache
# Time Complexity:
#   - `get`: O(1), because both cache lookup and linked list operations take constant time.
#   - `put`: O(1), because linked list insertion and removal, and dictionary operations take constant time.
# Space Complexity: O(capacity), where `capacity` is the maximum size of the cache. This is because the cache and doubly-linked list can store at most `capacity` items.

class Node:
    """
    Represents a doubly-linked list node used to maintain the order of the Least Recently Used (LRU) cache.
    Each node stores:
    - key: The key associated with the cached value.
    - val: The cached value.
    - prev: Pointer to the previous node in the list.
    - next: Pointer to the next node in the list.
    """
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    """
    Implements an LRU Cache using a hash map and a doubly-linked list.

    Methods:
    - `get(key)`: Retrieves the value associated with the key if it exists in the cache, and marks the key as recently used.
    - `put(key, value)`: Adds or updates the value associated with the key, while maintaining the LRU property.

    Attributes:
    - `cap`: The maximum capacity of the cache.
    - `cache`: A dictionary to map keys to their corresponding nodes in the doubly-linked list.
    - `left` and `right`: Sentinel nodes marking the boundaries of the doubly-linked list.
    - `counter`: Tracks the current size of the cache.
    """

    def __init__(self, capacity: int):
        """
        Initializes the LRUCache with a given capacity.

        :param capacity: int - The maximum number of items the cache can store.
        """
        self.cap = capacity
        self.cache = {}  # Maps keys to Node objects
        self.counter = 0  # Tracks the number of elements in the cache
        self.left, self.right = Node(0, 0), Node(0, 0)  # Sentinel nodes for the doubly-linked list
        self.left.next, self.right.prev = self.right, self.left  # Connect sentinel nodes

    def remove(self, node: Node):
        """
        Removes a node from the doubly-linked list.

        :param node: Node - The node to be removed.
        """
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
        self.counter -= 1

    def insert(self, node: Node):
        """
        Inserts a node at the end of the doubly-linked list (most recently used position).

        :param node: Node - The node to be inserted.
        """
        prv, nxt = self.right.prev, self.right
        prv.next = node
        nxt.prev = node
        node.next, node.prev = nxt, prv
        self.counter += 1

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with the key if it exists in the cache.
        Moves the key to the most recently used position in the list.

        :param key: int - The key to look up.
        :return: int - The value associated with the key, or -1 if the key is not in the cache.
        """
        if key in self.cache:
            cur_node = self.cache[key]
            self.remove(cur_node)  # Remove the node from its current position
            self.insert(cur_node)  # Reinsert the node at the end of the list
            return cur_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Adds or updates a key-value pair in the cache. If the cache is full, evicts the least recently used item.

        :param key: int - The key to be added or updated.
        :param value: int - The value to be associated with the key.
        """
        # If the key already exists, remove it from its current position
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new node and insert it at the end of the list
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If the cache exceeds its capacity, remove the least recently used item
        if self.counter > self.cap:
            lru = self.left.next  # The least recently used node is next to the left sentinel
            self.remove(lru)
            del self.cache[lru.key]  # Remove the corresponding entry from the hash map
