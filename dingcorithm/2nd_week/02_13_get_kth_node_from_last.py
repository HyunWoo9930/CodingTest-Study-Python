class Node:
    def __init__(self, data):
        self.data = data
        self.last = None
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
        cur.next.last = cur

    def get_kth_node_from_last(self, k):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        for i in range(k - 1):
            cur = cur.last
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
