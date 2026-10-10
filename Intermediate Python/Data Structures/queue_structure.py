class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.left = None
        self.right = None

    def push_left(self, data):
        new_node = Node(data)

        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node

    def push_right(self, data):
        new_node = Node(data)

        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node

    def pop_left(self):
        if self.left is None:
            return None

        removed_node = self.left
        self.left = self.left.next

        if self.left is not None:
            self.left.prev = None
        else:
            self.right = None

        return removed_node.data

    def pop_right(self):
        if self.right is None:
            return None

        removed_node = self.right
        self.right = self.right.prev

        if self.right is not None:
            self.right.next = None
        else:
            self.left = None

        return removed_node.data

    def print_deque(self):
        current = self.left

        while current is not None:
            print(current.data)
            current = current.next
