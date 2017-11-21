# 단일 연결 리스트 구현

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.size = 0
        self.head = None

    def addFirst(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size = 1
        #print("size : ", self.size)

    def addLast(self, data):
        new_node = Node(data)
        lastNode = self.find(self.size - 1)
        lastNode.next = new_node
        self.size += 1

        #print("size : ", self.size)

    def find(self, index):
        node = self.head
        if index == 0:
            return (self.head)
        else:
            for i in range(index):
                node = node.next
            return (node)

    def add(self, index, data):
        if index == 0:
            self.addFirst(data)
        else:
            new_node = Node(data)

            if index == self.size:
                self.addLast(data)
            else:
                prev_node = self.find(index - 1)
                prev_node.next = new_node
                new_node.next = self.find(index + 1)
                self.size += 1

                #print("size : ", self.size)

    def setNext(self, data):
        node = Node(data)
        head = self.head
        if head==None:
            self.size += 1
            return(self.addFirst(node.data))
        else:
            for i in range(self.size-1):
                head = head.next
            head.next = node
            node.next = None

            self.size +=1

    def removeFirst(self):
        if self.size == 1:
            self.head = None
            self.size -= 1
            #print("size : ", self.size)
            return (None)
        else:
            temp = self.head
            self.head = temp.next
            self.size -= 1

            #print("size : ", self.size)

    def removeLast(self):
        node = self.find(self.size - 2)
        node.next = None
        self.size -= 1
        #print("size : ", self.size)

    def remove(self, index):
        if index == 0:
            self.removeFirst()
        elif index == self.size - 1:
            self.removeLast()

        else:
            prev_node = self.find(index - 1)
            next_node = self.find(index + 1)
            prev_node.next = next_node
            self.size -= 1
            #print("size : ", self.size)

    def getSize(self):
        print(self.size)

    def printNode(self):
        if self.size == 0:
            #print("no list")
            return
        else:
            node = self.head
            for i in range(self.size):
                print(node.data)
                node = node.next

