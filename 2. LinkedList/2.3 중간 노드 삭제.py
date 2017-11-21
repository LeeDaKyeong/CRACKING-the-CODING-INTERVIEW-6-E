import linkedlist


def deleteNode(Node):
    node = Node
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    return True


if __name__ == "__main__":
    node1 = linkedlist.Node(1)
    node2 = linkedlist.Node(2)
    node3 = linkedlist.Node(3)
    node4 = linkedlist.Node(4)
    node5 = linkedlist.Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("before delete")
    node = node1
    while(node):
        print(node.data)
        node = node.next

    deleteNode(node3)
    print("after delete")
    node = node1
    while(node):
        print(node.data)
        node = node.next