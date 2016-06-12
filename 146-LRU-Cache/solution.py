class CacheNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None
    
    '''
    A method to insert a node
    @return the head,tail of list
    '''
    @staticmethod
    def insert(head, tail, node):
        # print 'insert ' + str(node.val)
        if tail is None and head is None:
            return node, node
        
        tail.next = node
        node.prev = tail
        return head, node
    
    '''
    A method to remove the least used node
    @return the new header, tail of list
    '''
    @staticmethod
    def pop(head, tail):
        if head is tail:
            return None, None
        
        # print 'pop ' + str(head.val)
        tmp = head.next
        tmp.prev = None
        return tmp, tail
    
    
    @staticmethod
    def update(head, tail, node):
        # print 'update ' + str(node.val)
        if node is tail:
            return head, tail
        elif node is head:
            head = head.next
            head.prev = None
            tail.next = node
            node.prev = tail
            node.next = None
            return head, node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            tail.next = node
            node.prev = tail
            return head, node

    
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.d = {}
        self.head, self.tail = None, None
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self.head, self.tail = CacheNode.update(self.head, self.tail, node)
            return node.val
        else:
            return -1
        
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.d:
            node = self.d[key]
            self.head, self.tail = CacheNode.update(self.head, self.tail, node)
            node.val = value
        else:
            node = CacheNode(key, value)
            self.d[key] = node
            self.head, self.tail = CacheNode.insert(self.head, self.tail, node)
            
            # check whether the size is beyond the capacity
            if len(self.d) > self.capacity:
                del self.d[self.head.key]
                self.head, self.tail = CacheNode.pop(self.head, self.tail)