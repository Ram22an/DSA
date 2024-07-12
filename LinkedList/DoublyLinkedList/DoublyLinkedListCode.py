class Node:
    def __init__(self,Item=None,Prev=None,Next=None):
        self.Item=Item
        self.Prev=Prev
        self.Next=Next
class DoublyLinkedList:
    def __init__(self):
        self.Start=None
        self.End=None
    def is_empty(self):
        return self.Start==None
    def Insert_At_Start(self,data):
        N=Node(data,None,self.Start)
        if self.is_empty():
            self.Start=N
            self.End=N
        else:
            self.Start.Prev=N
            self.Start=N
    def Insert_At_End(self,data):
        N=Node(data,self.End,None)
        if self.is_empty():
            self.Start=N
            self.End=N
        else:
            self.End.Next=N
            self.End=N
    def Insert_At_Point(self,data,Index):
        if self.is_empty():
            self.Insert_At_Start(data)
        else:
            temp=self.Start
            for i in range(Index-1):
                temp=temp.Next
            new_node= Node(data, temp, temp.Next)
            if temp.Next is None:
                self.Insert_At_End(data)
            else:
                temp.Next.Prev = new_node
                temp.Next = new_node
    def Show_DLL_From_Last(self):
        temp=self.End
        while temp is not None:
            print(temp.Item,end=" ")
            temp=temp.Prev
        print(" ")
    def Show_DLL(self):
        temp=self.Start
        while temp is not None:
            print(temp.Item,end=" ")
            temp=temp.Next
        print(" ")
Dll=DoublyLinkedList()
Dll.Insert_At_Start(3)
Dll.Insert_At_End(4)
Dll.Insert_At_Point(5,2)
Dll.Show_DLL()
Dll.Show_DLL_From_Last()
