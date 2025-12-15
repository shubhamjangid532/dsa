class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    tail = dummy
    
    # 1. The Zipper Loop
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            # Handles both (list2 < list1) AND (list2 == list1)
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    # 2. The Cleanup (O(1) Speed)
    # If one list is empty, just point tail to the other list's head.
    # We don't need a loop because the rest of the chain is already intact.
    tail.next = list1 if list1 else list2
    
    return dummy.next

# --- Helper for visualization ---
def print_list(node):
    chain = []
    while node:
        chain.append(str(node.val))
        node = node.next
    print(" -> ".join(chain))

# --- Test Data Setup ---
if __name__ == "__main__":
    # Create List 1: 1 -> 2 -> 4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    # Create List 2: 1 -> 3 -> 4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    print("List 1:", end=" ")
    print_list(l1)
    print("List 2:", end=" ")
    print_list(l2)

    # Run Merge
    merged_head = mergeTwoLists(l1, l2)

    print("Merged:", end=" ")
    print_list(merged_head) 
    # Expected Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4