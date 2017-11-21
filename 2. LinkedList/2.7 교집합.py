import linkedlist

def myFindIntersection(head1, head2):
    size1 = 0
    size2 = 0

    node1 = head1
    node2 = head2

    while(node1):
        size1+=1
        node1 = node1.next
    while(node2):
        size2+=1
        node2 = node2.next

    if size1>size2:
        for i in range(size1-size2):
            head1 = head1.next
    else:
        for i in range(size2-size1):
            head2 = head2.next

    while(head1):
        #print(head1.data)
        if id(head1)==id(head2):
            print(head1.data)
        head1 = head1.next
        head2 = head2.next

if __name__ == "__main__":
    node1 = linkedlist.Node(3)
    node2 = linkedlist.Node(1)
    node3 = linkedlist.Node(5)
    node4 = linkedlist.Node(9)
    node5 = linkedlist.Node(4)
    node6 = linkedlist.Node(6)
    node7 = linkedlist.Node(7)
    node8 = linkedlist.Node(2)
    node9 = linkedlist.Node(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node7
    node7.next = node8
    node8.next = node9

    node5.next = node6
    node6.next = node7

    myFindIntersection(node1,node5)


