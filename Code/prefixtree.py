#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        if self.size == 0:
            return True 
        return False 

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        node, depth = self._find_node(string)
        
        if depth == len(string) and node.is_terminal():
            return True 
            
        return False 

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # TODO
        
        node = self.root
        for char in string:
            
            # if node has a child
            if node.has_child(char):
                # grab child 
                node = node.get_child(char)
            else:
            # add the node 
                
                new_node = PrefixTreeNode(char)
                # add it to trie
                node.add_child(char, new_node)
                # reassign
                node = new_node
                
        # check if new string is inserted
        if not node.is_terminal():
            self.size += 1 
            node.terminal = True     

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        depth = 0 
        # TODO
        for letter in string:
            if node.has_child(letter):
                node = node.get_child(letter)
                depth += 1 
            else:
                return None, depth 
                
        return node, depth 
        
    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        # TODO
        
        # get the node object using find prefix node 
        node = self._find_node(prefix)[0]
        
        
        # check if node is found 
        if node == None:
            # means node not found 
            return completions 
        
        # check if the node's a terminal node 
        if node.is_terminal():
            # add prefix to completions list
            completions.append(prefix)
            
        # if not terminal we neeed to traverse 
        # for every child of this node 
        for char in node.children:
            # grab its children 
            child_node = node.get_child(char)
            # use traverse on the child with the prefix + completions.append()
            self._traverse(child_node, prefix+char, completions.append)
            
        return completions 


    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        node = self.root
        for child in node.children:
            child_node = node.get_child(child)
            self._traverse(child_node, child, all_strings.append)
            
        return all_strings 

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # TODO

        # if node is terminal 
        # call visit 
        if node.is_terminal():
            visit(prefix)
        
        # if the node has children (can be terminal AND have children)
        if len(node.children) > 0: 
            # need to loop through children 
            for child in node.children:
                # child = node.get_child(child)
                # call traverse on the children
                self._traverse(node.get_child(child), prefix+child, visit)    

        
def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
