class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1        
class BBST:
    def _init_(self):
        self.root = None

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, root, key):
        if not root:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._find(root.left, key)
        else:
            return self._find(root.right, key)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
        
        return self._balance(root)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, root, key):
        if not root:
            return root
        
        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self._remove(root.right, temp.key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
        
        return self._balance(root)

    def order_of_key(self, key):
        return self._order_of_key(self.root, key)

    def _order_of_key(self, root, key):
        if not root:
            return 0
        if key < root.key:
            return self._order_of_key(root.left, key)
        elif key > root.key:
            left_size = self.get_size(root.left) if root.left else 0
            return 1 + left_size + self._order_of_key(root.right, key)
        else:
            return self.get_size(root.left) if root.left else 0

    def get_by_order(self, k):
        return self._get_by_order(self.root, k)

    def _get_by_order(self, root, k):
        if not root:
            return None
        
        left_size = self.get_size(root.left) if root.left else 0
        if k < left_size:
            return self._get_by_order(root.left, k)
        elif k > left_size:
            return self._get_by_order(root.right, k - left_size - 1)
        else:
            return root.key

    def get_height(self, root):
        return root.height if root else 0

    def get_size(self, root):
        return root.size if root else 0

    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def _balance(self, root):
        balance = self.get_balance(root)
        if balance > 1:
            if self.get_balance(root.left) < 0:
                root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if balance < -1:
            if self.get_balance(root.right) > 0:
                root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        return root

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.size = 1 + self.get_size(z.left) + self.get_size(z.right)
        y.size = 1 + self.get_size(y.left) + self.get_size(y.right)
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.size = 1 + self.get_size(y.left) + self.get_size(y.right)
        x.size = 1 + self.get_size(x.left) + self.get_size(x.right)
        return x 