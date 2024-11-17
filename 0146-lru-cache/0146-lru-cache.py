class Node:
    """A node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        Initialize the LRU cache with a given capacity.
        """
        self.capacity = capacity
        self.cache = {}  # HashMap to store key -> node
        # Initialize a dummy head and tail for the doubly linked list
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """
        Remove a node from the doubly linked list.
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        """
        Add a node right after the dummy head.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        Return the value of the key if it exists, otherwise return -1.
        """
        if key in self.cache:
            node = self.cache[key]
            # Move the node to the head (most recently used)
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        Add or update the value of the key.
        If the cache exceeds capacity, evict the least recently used key.
        """
        if key in self.cache:
            # Remove the old node
            self._remove(self.cache[key])
        # Create a new node
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_head(new_node)

        if len(self.cache) > self.capacity:
            # Remove the least recently used node (from the tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)