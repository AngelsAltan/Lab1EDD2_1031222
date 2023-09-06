class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        
        self.update_height(node)
        
        balance = self.balance_factor(node)
        
        # Rotaciones equilibrio
        if balance > 1:
            if key < node.left.key:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        if balance < -1:
            if key > node.right.key:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.find_min(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        
        self.update_height(node)
        
        balance = self.balance_factor(node)
        
        #Rotaciones equilibrio
        if balance > 1:
            if self.balance_factor(node.left) >= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        if balance < -1:
            if self.balance_factor(node.right) <= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        
        return node

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)