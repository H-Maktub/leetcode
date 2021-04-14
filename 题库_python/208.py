class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp = [None]*26
        self.end = False
    def  dfs(self, strs: str):
        node = self
        for ch in strs:
            ch = ord(ch) - ord("a")
            if not node.temp[ch]:
                return None
            node = node.temp[ch]
        return node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.temp[ch]:
                node.temp[ch] = Trie()
            node = node.temp[ch]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.dfs(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self.dfs(prefix) is not None
