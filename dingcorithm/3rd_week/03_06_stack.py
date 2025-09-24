class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            print("")
        delete_head = self.head
        self.head = delete_head.next
        return delete_head

    def peek(self):

        # 어떻게 하면 될까요?
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?
        return