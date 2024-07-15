class Node:
    def __init__(self,Item=None,Prev=None,Next=None):
        self.Item=Item
        self.Prev=Prev
        self.Next=Next
class DoublyLinkedList:
    def __init__(self,Node=None):
        self.Start=Node
        self.End=Node
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
    def Search(self,data):
        temp=self.Start
        if self.is_empty():
           print("List is empty")
           return False
        else:
            while temp!=None:
                if temp.Item==data:
                    print("Item found")
                    return True
                temp=temp.Next
            print("Item not found")
            return False
    def Delete_From_Start(self):
        if self.is_empty():
            print("List is already empty")
            return
        else:
            self.Start=self.Start.Next
            if self.Start!=None:
                self.Start.Prev=None
            else:
                self.End=None
            print("item has been deleted")
            return
    def Delete_From_End(self):
        if self.is_empty():
            print("List is already empty")
            return
        else:
            if self.Start==self.End:
                self.End=None
                self.Start=None
                print("List is now empty")
                return
            else:
                self.End=self.End.Prev
                self.End.Next=None
                print("item has been deleted")
                return
    def Delete_By_item(self,item):
        if self.is_empty():
            print("List is already empty")
            return
        temp=self.Start
        while temp!=None:
            if self.Start.Item==item:
                self.Delete_From_Start()
            if self.End.Item==item:
                self.Delete_From_End()
            if temp.Item==item:
                temp.Prev.Next=temp.Next
                temp.Next.Prev=temp.Prev
                temp.Next=None
                temp.Prev=None
                return
            temp=temp.Next
    def __iter__(self):
        return DllIterator(self.Start)
class DllIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.Item
        self.current=self.current.Next
        return data
Dll=DoublyLinkedList()
Dll.Insert_At_Start(3)
Dll.Insert_At_End(4)
Dll.Insert_At_Point(5,2)
Dll.Show_DLL()
Dll.Show_DLL_From_Last()
Dll.Search(5)
Dll.Show_DLL_From_Last()
Dll.Show_DLL()
