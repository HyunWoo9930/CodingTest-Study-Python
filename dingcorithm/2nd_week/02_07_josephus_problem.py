# BOJ 1158

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def print_delete(self, index):
        cur = self
        for i in range(index - 1):
            cur = cur.next
        delete_target = cur.next
        cur.next = cur.next.next
        return delete_target.data, cur


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_node(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur


def josephus_problem(n, k):
    answers = []
    if k == 1:
        for i in range(1, n + 1):
            answers.append(i)
        print("<", ", ".join(map(str, answers)), ">", sep='')
        return None
        # linked list에 append
    linked_list = LinkedList(1)
    for i in range(2, n + 1):
        linked_list.append(i)

    # 마지막을 처음과 연결
    linked_list.get_node(n - 1).next = linked_list.get_node(0)
    node = linked_list.get_node(0)
    for i in range(k - 2):
        node = node.next
    answers.append(node.next.data)
    node.next = node.next.next
    for i in range(1, n):
        data, node = node.print_delete(k)
        answers.append(data)
    # print(answers)
    print("<", ", ".join(map(str, answers)), ">", sep='')


n, k = map(int, input().split())
josephus_problem(n, k)
