from ..measure_times import measure_time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@measure_time
def middleNode(head):
    # Initialize slow and fast pointers
    slow = head
    fast = head
    # Loop while fast is not None and fast.next is not None
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


# Helper to test 
if __name__ == "__main__":
    # Create List: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    mid = middleNode(head)
    print(f"Middle Value: {mid.val}") # Should be 3