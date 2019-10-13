# Definition for singly-linked list.
def stringToListNode(nums):
    # Generate list from the input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in nums:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next or not head.next.next:
        return head

    odd, even = head, head.next
    first_even = head.next

    while True:
        next_odd = even.next

        odd.next = next_odd
        even.next = next_odd.next

        next_odd.next = first_even

        odd = next_odd
        even = even.next

        if not even or not even.next:
            break

    return head


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head = stringToListNode(nums)
ans = oddEvenList(head)
print(listNodeToString(ans))
