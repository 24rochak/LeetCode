class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create(l1):
    if len(l1) == 0:
        return None
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


def isPalindrome(head):
    def isPalindrome(l):
        i = 0
        j = len(l) - 1
        print(i, j)
        while (i <= j):
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1
        return True

    if head == None or head.next == None:
        return True
    last = head
    l = []
    while last:
        l.append(last.val)
        last = last.next
    return isPalindrome(l)


arr = []
l1 = create(arr)
ans = isPalindrome(l1)
print(ans)
