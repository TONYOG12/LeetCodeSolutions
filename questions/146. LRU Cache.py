class Node:
    def __init__(self, key, value):
        self.key , self.value = key, value
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        #left = lru , right = most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next , self.right.prev = self.right, self.left

    #remove node from list    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
        
    #insert node at right most of list
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev  = node
        node.prev, node.next = prv, nxt
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
