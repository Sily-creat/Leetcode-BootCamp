class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the linked list (using slow and fast pointers)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Step 3: Compare the first and the reversed second half
    left, right = head, prev
    while right:  # Only need to compare until the end of the reversed half
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
