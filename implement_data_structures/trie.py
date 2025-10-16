class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    def startsWth(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
        return True
    
    def print_words(self, node=None, word="", words=[]):
        if node is None:
            node = self.root
        
        if node.isWord:
            words.append(word)
        
        for c, child in node.children.items():
            self.print_words(child, word + c, words)
        
        return words

# Driver code
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # return True
    print(trie.search("app"))     # return False
    print(trie.startsWth("app"))  # return True
    trie.insert("bat")
    trie.insert("ball")
    trie.insert("batman")
    print(trie.print_words())     # return ['apple', 'app', 'bat',