import linkedlist

def myFindBeginning(head):
    li = list()
    while(head):
        li.append(id(head))
        li2 = set(li)

        if len(li)!=len(li2):
            return(head.data)
        head = head.next



if __name__ == "__main__":
    node1 = linkedlist.Node("A")
    node2 = linkedlist.Node("B")
    node3 = linkedlist.Node("C")
    node4 = linkedlist.Node("D")
    node5 = linkedlist.Node("E")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3

    print(myFindBeginning(node1))
