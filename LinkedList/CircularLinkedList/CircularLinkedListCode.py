class Node:
    def __init__(self,Data=None,Next=None):
        self.Data=Data
        self.Next=Next
class Cll:
    def __init__(self,Node=None):
        self.End=Node
    def is_empty(self):
        return self.End==None
    def Insert_At_Start(self,data):
        N=Node(data)
        if self.is_empty():
            self.End=N
            self.End.Next=self.End
        else:
            N.Next=self.End.Next
            self.End.Next=N
    def Insert_At_Last(self,data):
        N=Node(data)
        if self.is_empty():
            self.Insert_At_Start(data)
        else:
            N.Next=self.End.Next
            self.End.Next=N
            self.End=N
    def Search(self,data):
        if self.is_empty():
            print("List is empty")
            return
        temp=self.End.Next
        while True:
            if temp.Data==data:
                print("Data found ")
                return
            temp=temp.Next
            if temp==self.End.Next:
                break
        print("Data not found")
        return
    def Insert_After(self,data,Index_Data):
        N=Node(data)
        if self.is_empty():
            print("List is empty")
            return
        temp=self.End.Next
        while True:
            if temp.Data==Index_Data:
                N.Next=temp.Next
                temp.Next=N
                if temp==self.End:
                    self.End=N
                return
            temp=temp.Next
            if temp==self.End.Next:
                break
        print(f"Data {Index_Data} not found in the list")
    def Show_Cll(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.End==self.End.Next:
            print(self.End.Data)
            return
        temp=self.End.Next
        while True:
            print(temp.Data)
            temp=temp.Next
            if temp==self.End.Next:
                break
        print(" ")
        return
    def Delete_First(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.End==self.End.Next:
            self.End=None
            return
        self.End.Next=self.End.Next.Next
    def Delete_Last(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.End==self.End.Next:
            self.End=None
            return
        temp=self.End.Next
        while temp.Next!=self.End:
            temp=temp.Next
        temp.Next=self.End.Next
        self.End=temp
    def delete_item(self, data):
        if self.is_empty():
            print("List is empty")
            return
        if self.End.Next == self.End and self.End.data == data:
            self.End = None
            return
        temp = self.End.Next
        prev = self.End
        while True:
            if temp.Data == data:
                prev.Next = temp.Next
                if temp == self.End: 
                    self.End = prev
                return
            prev = temp
            temp = temp.Next
            if temp == self.End.Next:
                break
        print(f"Data {data} not found in the list")
        return
cll = Cll()
cll.Insert_At_Start(10)
cll.Insert_At_Start(20)
cll.Insert_At_Last(5)
cll.Insert_After(15, 10)
cll.Show_Cll() 
cll.delete_item(10)
cll.Show_Cll() 
cll.delete_item(5)
cll.Show_Cll()   
cll.delete_item(20)
cll.Show_Cll()   
        