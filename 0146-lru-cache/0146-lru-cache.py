class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # 哨兵节点，简化边界处理
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                removed = self._pop_tail()
                if removed:
                    del self.cache[removed.key]

    # --- 以下是你代码中引用但未定义的“发动机”部分 ---

    def _add_node(self, node):
        """将节点插入到 head 后面（最新使用）"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """将节点从链表中彻底断开"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """移动到开头：先删后加"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """弹出最久未使用的节点（tail 之前那个）"""
        res = self.tail.prev
        if res == self.head: # 链表为空的情况（虽然 capacity>0 不会发生）
            return None
        self._remove_node(res)
        return res    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)