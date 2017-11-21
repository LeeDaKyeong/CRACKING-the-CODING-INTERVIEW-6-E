import linkedlist

def addList():
    li = linkedlist.LinkedList()
    li.add(0, 1)
    li.add(1, 1)
    li.add(2, 1)
    li.add(3, 2)
    li.add(4, 3)
    li.add(5, 2)
    li.add(6, 4)

    return(li)

def removeOverlap(LinkedList):
    li_list = LinkedList
    li = list()

    node = li_list.head
    while(node):
        li.append(node.data)
        node = node.next

    li = list(set(li))
    return(li)

if __name__ == "__main__":
    li = addList()
    print(removeOverlap(li))