class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
    def printL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
if __name__=='__main__':
    LL = SLL()
    LL.head = Node(10)
    two = Node(20)
    three = Node(30)
    LL.head.next = two
    two.next = three
    LL.printL()              
