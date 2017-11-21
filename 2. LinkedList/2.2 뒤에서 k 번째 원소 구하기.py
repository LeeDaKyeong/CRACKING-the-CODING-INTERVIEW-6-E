import linkedlist


def addList():
    li = linkedlist.LinkedList()
    li.add(0, 1)
    li.add(1, 2)
    li.add(2, 3)
    li.add(3, 4)
    li.add(4, 5)
    li.add(5, 6)
    li.add(6, 7)

    return(li)

def printKth(LinkedList, k):
    li = list()
    node = LinkedList.head
    while(node):
        li.append(node.data)
        node = node.next

    return(li[len(li)-k])

#재귀적으로 풀기
class Index:
    value = 0

def recursionKthToLast(Node, k):
    idx = Index()
    return(__recursionKthToLast__(Node,k,idx))

def __recursionKthToLast__(Node,k,idx):
    if (Node == None):
        return(None)
    node = __recursionKthToLast__(Node.next,k,idx)
    idx.value += 1

    if(idx.value == k):
        return(Node.data)
    return(node)

#순환적 방법
def iterativeKthToLast(Node,k):
    #node = Node
    p1 = Node
    p2 = Node

    for i in range(k):
        if(p1==None):
            return(None)
        p1 = p1.next

    while(p1):
        p2 = p2.next
        p1 = p1.next

    return(p2.data)

if __name__ == "__main__":
    li = addList()
    head = li.find(0)

    print("1. : ",printKth(li,3))

    print("2. : ",recursionKthToLast(head,3))

    print("3. : ",iterativeKthToLast(head,3))