# Solution for LeetCode Problem 211: Design Add and Search Words Data Structure
# Time Complexity:
# - `addWord`: O(L), where L is the length of the word being added.
# - `search`: O(M * 26^N), where M is the average length of the word being searched, and N is the number of wildcard `.` characters.
# Space Complexity: O(N * L), where N is the number of words added, and L is the average length of the words (space used by the Trie).

class TrieNode:
    def __init__(self):
        """
        Initializes a TrieNode with an empty dictionary of children nodes
        and a boolean indicating if it marks the end of a word.
        """
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        """
        Initializes the WordDictionary with a root TrieNode.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word to the WordDictionary.
        
        :param word: The word to be added.
        """
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]
        ptr.is_end = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the WordDictionary. The word can contain the
        wildcard character '.' which matches any single character.
        
        :param word: The word or pattern to search for.
        :return: True if the word or pattern exists, otherwise False.
        """
        def dfs(node: TrieNode, index: int) -> bool:
            """
            Performs a depth-first search to match the word or pattern.
            
            :param node: The current TrieNode being processed.
            :param index: The current index in the word being matched.
            :return: True if the word or pattern matches, otherwise False.
            """
            cur_ptr = node
            for i in range(index, len(word)):
                if word[i] == ".":  # Wildcard case: check all possible children
                    for child in cur_ptr.children:
                        if dfs(cur_ptr.children[child], i + 1):
                            return True
                    return False
                else:
                    # Character match case
                    if word[i] not in cur_ptr.children:
                        return False
                    cur_ptr = cur_ptr.children[word[i]]
            
            # Check if the current node marks the end of a valid word
            return cur_ptr.is_end

        return dfs(self.root, 0)
