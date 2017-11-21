import linkedlist


def addList():
    li = linkedlist.LinkedList()
    li.add(0, 0)
    li.add(1, 1)
    li.add(2, 2)
    li.add(3, 1)
    li.add(4, 0)


    return(li)

def myIsPalindrome(head):
    li1 = list()
    while(head):
        li1.append(head.data)
        head = head.next

    li2 = li1.copy()
    li2.reverse()

    if li1==li2:
        return(True)
    else:
        return(False)

if __name__ == "__main__":
    li = addList()
    head = li.find(0)

    print(myIsPalindrome(head))