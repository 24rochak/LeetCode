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


def display(l1):
    head = l1
    while head:
        print(head.val, end="->")
        head = head.next
    print("")


def mergeTwoLists(l1: ListNode, l2: ListNode):
    head = ListNode(-1)
    temp = head
    while l1 and l2:
        if l1.val < l2.val:
            temp1 = ListNode(l1.val)
            temp.next = temp1
            temp = temp.next
            l1 = l1.next

        elif l1.val > l2.val:
            temp1 = ListNode(l2.val)
            temp.next = temp1
            temp = temp.next
            l2 = l2.next

        else:
            temp1 = ListNode(l1.val)
            temp.next = temp1
            temp = temp.next
            l1 = l1.next

            temp1 = ListNode(l2.val)
            temp.next = temp1
            temp = temp.next
            l2 = l2.next

    while l1:
        temp1 = ListNode(l1.val)
        temp.next = temp1
        temp = temp.next
        l1 = l1.next

    while l2:
        temp1 = ListNode(l2.val)
        temp.next = temp1
        temp = temp.next
        l2 = l2.next

    return head.next


a1 = [1, 2, 4, 6, 7]
a2 = [1, 3, 4]

l1 = create(a1)
l2 = create(a2)

display(l1)
display(l2)

c = mergeTwoLists(l1, l2)
display(c)
