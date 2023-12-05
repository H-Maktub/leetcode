class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        def find(node,s)->bool:
            if len(s) == 0:
                return node.isEnd
            ch = s[0]
            if ch != '.':
                child = node.children[ord(ch) - ord('a')]
                if child != None and find(child,s[1:]):
                    return True
            else:
                for child in node.children:
                   if child != None and find(child,s[1:]):
                        return True 
            return False
    
        return find(self.root,word)