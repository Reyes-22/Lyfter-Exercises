
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left

            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right

            else:
                return

    def print_tree(self, node):
        if node is not None:
            print(node.data)
            self.print_tree(node.left)
            self.print_tree(node.right)


tree = BinaryTree()

tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(3)
tree.insert(7)
tree.insert(15)
tree.insert(25)

tree.print_tree(tree.root)
