class BSTNodes:
    def __init__ (self, node):
        self.node = node
        self.right = None
        self.left = None
    
    def child_node (self,node):
        if node == self.node:
            return
        if node < self.node:
            if self.left:
                self.left.child_node(node)
            else: 
                self.left = BSTNodes(node)
        else:
            if self.right:
                self.right.child_node(node)
            else:
                self.right = BSTNodes(node)
    
    def post_order(self):
        characters =[]
        if self.left:
            characters += self.left.post_order()
        if self.right:
            characters += self.right.post_order()
        characters.append(self.node)
        return characters
    
    def pre_order(self):
        characters = []
        characters.append(self.node)
        if self.right:
            characters += self.right.pre_order()
        if self.left:
            characters += self.left.pre_order()
        return characters
    def in_order(self):
        characters = []
        if self.right:
            characters += self.right.in_order()
        elements.append(self.node)
        if self.left:
            characters += self.left.in_order()
        return characters

def tree(characters):
    branches = BSTNodes(characters[0])
    for i in range (1,len(characters)):
        branches.child_node(characters[i])
    return branches
        
