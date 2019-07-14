class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create(l1):
    head = ListNode(l1[0])
    temp = head
    for i in range(1, len(l1)):
        temp1 = ListNode(l1[i])
        temp.next = temp1
        temp = temp.next

    return head


def display(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("")


def removeElements(head: ListNode, val: int):
    temp = ListNode(-1)
    temp.next = head
    prev = temp
    while (head):
        if head.val == val:
            prev.next = head.next
            head = head.next
        else:
            prev = head
            head = head.next
    return temp.next


arr = [1, 2, 2, 3, 4, 5]
l1 = create(arr)
display(l1)
l1 = removeElements(l1, 2)
display(l1)
