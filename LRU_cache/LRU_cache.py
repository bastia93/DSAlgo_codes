class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.hm = {}
        self.head = None
        self.tail = None

    def _move_to_tail(self, node):

        if self.head is None and self.tail is None:
            self.head = self.tail = node
            return

        if self.tail is node:
            return

        if node.right is not None:
            # Node is already exist
            # if the node is head node and more than one node is present
            if node.left is None:
                self.head = self.head.right
                self.head.left = None
            else:
                pre_node = node.left
                post_node = node.right

                pre_node.right = post_node
                post_node.left = pre_node

        # Attaching at the tail
        self.tail.right = node
        node.left = self.tail
        self.tail = self.tail.right
        self.tail.right = None

        return

    def _check_capacity(self):
        if len(self.hm) > self.capacity:
            temp_key = self.head.key
            self.head = self.head.right
            self.head.left = None
            del self.hm[temp_key]
        return

    # @return an integer
    def get(self, key):
        if key in self.hm:
            self._move_to_tail(self.hm[key])
            return self.hm[key].value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # Change the value of the key
        if key in self.hm:
            node_address = self.hm[key]
            node_address.value = value
        else:
            node_address = Node(key, value)
            self.hm[key] = node_address

        self._move_to_tail(node_address)
        self._check_capacity()
        return