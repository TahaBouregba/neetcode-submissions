class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # LRU
        self.right = Node(0, 0)  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Insert at the right = most recently used
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # It was just used, so move it to MRU
            self.remove(node)
            self.insert(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node

        # New/updated key becomes MRU
        self.insert(node)

        if len(self.cache) > self.capacity:
            # Remove LRU node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
