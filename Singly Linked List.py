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
    num1 = input()
    LL.head = Node(num1)
    temp = LL.head
    for i in range(0,4):
        num = input()
        new = Node(num)
        temp.next = new
        temp = new
    LL.printL()                         
