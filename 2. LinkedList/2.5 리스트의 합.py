import linkedlist

def addList1():
    li = linkedlist.LinkedList()
    li.add(0, 7)
    li.add(1, 1)
    li.add(2, 6)

    return(li)

def addList2():
    li = linkedlist.LinkedList()
    li.add(0, 5)
    li.add(1, 9)
    li.add(2, 2)

    return(li)

def myAddList(LinkedList1, LinkedList2):
    head1 = LinkedList1.head
    head2 = LinkedList2.head

    result = linkedlist.LinkedList()

    list1 = list()
    list2 = list()
    while(head1):
        list1.append(head1.data)
        head1 = head1.next

    while (head2):
        list2.append(head2.data)
        head2 = head2.next

    list1.reverse()
    list2.reverse()

    _result = int(''.join(str(i) for i in list1)) + int(''.join(str(i) for i in list2))

    _result2 = list(str(_result))
    _result2.reverse()

    idx = 0
    for i in range(len(_result2)):
        result.add(idx,_result2[i])
        idx += 1

    return(result)


#def addList(head1, head2, value = 0):
#    print("value : ",value)
#    if head1 == None and head2 == None:
#        return(None)
#
#    result = linkedlist.LinkedList()
#
#    if head1 != None:
#        value = value + head1.data
#    if head2 != None:
#        value = value + head2.data
#    #result.setNext(value % 10)
#
#    if head1 != None and head2 != None:
#        if head1 == None:
#            _head1 = None
#        else:
#            _head1 = head1.next
#
#        if head2 == None:
#            _head2 = None
#        else:
#            _head2 = head2.next
#        addList(_head1, _head2, int(value / 10))
#        result.setNext(value % 10)
#
#    return(result)


if __name__ == "__main__":

    li1 = addList1()
    li2 = addList2()

    list1 = myAddList(li1,li2)
    list1.printNode()

#    print("============")
#
#    head1 = li1.find(0)
#    head2 = li2.find(0)
#
#    list2 = addList(head1,head2)
#    list2.printNode()
