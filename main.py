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
        
        
