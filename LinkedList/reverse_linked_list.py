from ..measure_times import measure_time
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@measure_time
def reverseList(head):
    # prev = None
    # curr = head
    # while curr is not None:
    #     next = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = next
    # return prev
    prev, curr = None, head
    while curr:
        # Python evaluates the right side (curr.next, prev, curr) FIRST
        # Then assigns them to the left side simultaneously.
        curr.next, prev, curr = prev, curr, curr.next
        
    return prev



# Test helper
if __name__ == "__main__":
    # Create 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    new_head = reverseList(head)
    
    # Print to verify: Should be 5 -> 4 -> 3 -> 2 -> 1
    curr = new_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next