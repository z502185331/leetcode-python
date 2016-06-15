# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        # return self.sol_insert(head)
        return self.sol_dict(head)
        
    '''
    A solution solved by dict
    '''
    def sol_dict(self, head):
        node_dict = {}
        cur = head
        while cur is not None:
            node_dict[cur] = RandomListNode(cur.label)
            cur = cur.next
        
        for key, value in node_dict.items():
            if key.random is not None:
                value.random = node_dict[key.random]
        
        prehead = RandomListNode(-1)
        tail = prehead
        cur = head
        
        while cur is not None:
            tail.next = node_dict[cur]
            tail = tail.next
            cur = cur.next
        
        return prehead.next
    
    
    '''
    A solution by insert the copy node into the list and then separate
    '''
    def sol_insert(self, head):
        
        prehead = RandomListNode(-1)
        prehead.next = head
        
        # copy the node and insert into the list
        while head is not None:
            copy = RandomListNode(head.label)
            tmp = head.next
            head.next = copy
            copy.next = tmp
            head = tmp
        
        # copy the random pointer
        head = prehead.next
        while head is not None:
            if head.random is not None:
                head.next.random = head.random.next
            head = head.next.next
        
        # separate the list into two list
        copy_prehead = RandomListNode(-1)
        tail = copy_prehead
        head = prehead.next
        while head is not None:
            tail.next = head.next
            head = head.next.next
            tail = tail.next
            
        return copy_prehead.next
        
        