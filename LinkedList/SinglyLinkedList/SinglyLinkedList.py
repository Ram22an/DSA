class Node:
    def __init__(self,item=None,Next=None):
        self.item=item
        self.Next=Next
    def NextNode(self,Next):
        self.Next=Next
    def InsertItem(self,Item):
        self.item=Item
    def PrintItem(self):
        print(self.item)
print("Singly linked list")
A=Node()
B=A
while True:
    print("Enter a item")
    x=int(input())
    B.InsertItem(x)
    C=Node()
    B.NextNode(C)
    B=C
    print("Do you want to continue 1/0")
    Choice=int(input())
    if Choice==0:
        B.Next=None
        break
D=A
print("")
while D is not None:
    if D.Next!=None:
        print(D.item,end="->")
    D=D.Next