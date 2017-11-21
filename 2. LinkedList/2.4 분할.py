import linkedlist


def addList():
    li = linkedlist.LinkedList()
    li.add(0, 2)
    li.add(1, 1)
    li.add(2, 5)
    li.add(3, 2)
    li.add(4, 3)
    li.add(5, 6)
    li.add(6, 7)

    return(li)

#1
def listPartition(LinkedList,k):
    li = list()
    node = LinkedList.head
    while(node):
        li.append(node.data)
        node = node.next

    li.sort()
    return(li)

#2
def partition(Node,k):
    before = linkedlist.LinkedList()
    after = linkedlist.LinkedList()

    idx1 = 0
    idx2 = 0
    while(Node):
        if(Node.data<k):
            before.add(idx1,Node.data)
            idx1+=1
        elif(Node.data>=k):
            after.add(idx2,Node.data)
            idx2+=1
        Node = Node.next

    head = after.head

    idx = before.size
    while(head):
        before.add(idx,head.data)
        idx += 1
        head=head.next


    return(before)

if __name__ == "__main__":
    li = addList()
    print(listPartition(li,3))

    head = li.find(0)
    node = partition(head,3)
    node.printNode()
