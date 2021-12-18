
class linkedNode:
    head = None
    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None

    def show(cls):
        temp = cls.head
        while  temp != None:
            print(temp.val,end=" ")
            temp = temp.next
        print()
        
    def add(self,val):
        node = self.Node(val)
        # if head is empty
        if linkedNode.head == None:
            linkedNode.head = node
            return
        
        temp = linkedNode.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
    
    
if __name__ == "__main__":
    p1 = linkedNode()
    p1.add(12)
    p1.add(13)
    p1.add(14)
    p1.add(15)
    print(p1.head.val)
    p1.show()