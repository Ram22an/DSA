class Node:
    def __init__(self,item=None,Next=None):
        self.item=item
        self.Next=Next
class SLL:
    def __init__(self):
        self.start=None
    def is_empty(self):
        return self.start==None
    def Insert_At_Start(self,data):
        N=Node(data,self.start)
        self.start=N
    def Insert_At_Last(self,data):
        N=Node(data)
        if self.start is not None:
            temp=self.start
            while temp.Next is not None:
                temp=temp.Next
            temp.Next=N
            N.Next=None
        else:
            self.start=N
    def Search(self,data):
        temp=self.start
        counter=0
        while temp is not None:
            if temp.item==data:
                return print(f"the item is present at node {counter+1}")
            counter+=1
            temp=temp.Next
        return print("Can't find the item or it is not present")
    def Insert_After(self,Item,data=None,Index=None):
        if Index!=None:
            temp=self.start
            counter=0
            while counter==Index-1:
                temp=temp.Next
                counter+=1
            N=Node(Item)
            N.Next=temp.Next
            temp.Next=N
            return
        if data!=None:
            temp=self.start
            N=Node(Item)
            while temp.item!=data:
                temp=temp.Next
            N.Next=temp.Next
            temp.Next=N
            return
    def Show_LinkedList(self):
        if self.start!=None:
            temp=self.start
            while temp is not None:
                print(temp.item,end="->")
                temp=temp.Next
            print("")
            return
        else:
            print("List is empty")
            return
    def Delete_first(self):
        if self.start is not None:
            self.start=self.start.Next
    def Delete_Last(self):
        if self.start is None:
            return
        elif self.start.Next is None:
            self.start=None
        else:
            temp=self.start
            while temp.Next.Next is not None:
                temp=temp.Next
            temp.Next=None        
    def Delete_item(self,data):
        if self.start is None:
            print("List is empty")
            return
        elif  self.start.item == data:
            self.start=self.start.Next
            return
        else:
            temp=self.start
            while temp.Next is not None:
                if temp.Next.item==data:
                    temp2=temp.Next.Next
                    temp.Next=temp2
                    break
                temp=temp.Next
    def __iter__(self):
        return SLLIterator(self.start)
# now we have made this class now we want to make it itterable
class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.Next
        return data

Singly=Node()
List=SLL()
List.Insert_At_Start(1)
List.Insert_At_Start(2)
List.Insert_At_Start(3)
List.Show_LinkedList()
List.Delete_item(3)
List.Show_LinkedList()
List.Delete_item(2)
List.Show_LinkedList()
List.Delete_item(1)
List.Show_LinkedList()
for x in List:
    print(x,end=" ")