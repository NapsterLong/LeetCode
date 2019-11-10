'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

'''


class Node:
    def __init__(self, value, is_word):
        self.value = value
        self.is_word = is_word
        self.children = {}


class Trie:

    def __init__(self):
        self.data = Node("Root", False)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        children = self.data.children
        for w in word[:-1]:
            if w not in children:
                children[w] = Node(w, False)
            children = children[w].children
        last = word[-1]
        if last not in children:
            children[last] = Node(last, True)
        else:
            children[last].is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        children = self.data.children
        for w in word[:-1]:
            if w not in children:
                return False
            children = children[w].children
        last = word[-1]
        if last not in children or children[last].is_word is False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        children = self.data.children
        for w in prefix:
            if w not in children:
                return False
            children = children[w].children
        return True


word = "apple"
prefix = "app"
obj = Trie()
obj.insert(word)
print(obj.search(word))
print(obj.startsWith(prefix))
