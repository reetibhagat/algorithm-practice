class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(0)
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = first
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

while (head != None):
    print(head.data)
    head = head.next
