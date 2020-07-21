# linked list implementation and traversal, insertion and deletion, searching
class node:  # node class
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:  # linkedlist class
    def __init__(self):
        self.head = None

    def printlist(self):  # linklist traversal
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next

    def push(self, new_data):  # insert in the beginning
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertafter(self, prev_node, new_data):  # insert after given node
        if prev_node == None:
            print("prev_node is must for insertion")
            return
        new_node = node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):  # insert at the end
        new_node = node(new_data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next

        temp.next = new_node


if __name__ == '__main__':
    llist = linkedlist()
    llist.head = node(1)
    second = node(2)
    third = node(5)
    llist.head.next = second
    second.next = third
    llist.push(7)
    llist.push(27)
    llist.push(54)
    llist.insertafter(llist.head.next.next, 9)
    llist.append(6)
    print("created linked list after all insertion is:", end=' ')

llist.printlist()
