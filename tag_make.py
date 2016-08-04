from trie_tree import TrieTree

class TagMake(object):
    
    def __init__(self):
        self.tree = TrieTree()

    def add_tag(self, tag):
        self.tree.insert(tag)
    
    def add_tag_file(self, filename, func=lambda x:x):
        with open(filename) as f:
            for line in f:
                if line.strip():
                    self.tree.insert(func(line.strip()))

    def make(self, line):
        result = []
        for ind,_ in enumerate(line):
            cut = line[ind:]
            length = self.tree.findMax(cut)
            if length > 0:
                result.append((cut[:length], ind, length))
        return result

