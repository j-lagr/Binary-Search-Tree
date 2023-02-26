class BSTNodes:
    def __init__ (self, node):
        self.node = node
        self.right = None
        self.left = None
    
    def child_node (self,node):
        if node == self.node:
            return
    