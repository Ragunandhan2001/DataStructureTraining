'''x='AABCAAADA'
x1=[]
k=3
m=0
for i in range(len(x)//k):
    x1.append(x[m:m+k])
    m+=k
for v in x1:
    # print(list(v))
    # print(dict.fromkeys(list(v)))
    # print(dict.fromkeys(list(v)).keys())
    # # print(list(dict.fromkeys(list(v)).keys()))
    print(''.join(list(dict.fromkeys(list(v)).keys())))'''
#---------------------------------------------------------------------------
'''keys=['ragu','nandhan','ram']
values=['Python','Java','JS']
data=dict(zip(keys,values))
print(data.fromkeys(values,1))'''
#---------------------------------------------------------------------------
#Linear Search
'''from array import *
arr=array('i',[1,2,3,4,5])
n=int(input("Enter the element to be search:"))
for i in range(len(arr)):
    if arr[i]==n:
        print("The element found at index",i)
        break'''
#---------------------------------------------------------------------------
#bubble sort
'''lst=[1,4,10,7,6,2]
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]<=lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)'''
#---------------------------------------------------------------------------
'''arr=[3,7,9,12,24,33,46,56,88]
key=int(input("Enter the key:"))
l=0
h=len(arr)-1

while l<h:
    m=(l+h)//2
    if arr[m]==key:
        print("The value is found at index",m)
    else:
        if arr[m]<key:
            l=m+1
        else:
            h=m-1
print("The element found at index",l)'''
#---------------------------------------------------------------------------
'''s="NetSetOs is online educational platform"
res=[]
# print(s[len(s)-1])
for i in range(len(s)-1,-1,-1):
    res.append(s[i])

print("".join(res))'''
#---------------------------------------------------------------------------
'''s=input().split()
print(" ".join(s[::-1]))'''
#---------------------------------------------------------------------------
'''str_r=input()
count=0
val=[]
for i in range(len(str_r)):
    count=0
    for j in range(len(str_r)):
        if str_r[i]==str_r[j]:
            count+=1
    if count==1:
        print(str_r[i])
        break'''
#---------------------------------------------------------------------------
# list_one=[40,50,60,80]
# list_two=[50,100,150,200]
# for i in list_two:
#     for j in list_two:
#         if i==j:
#             print(i)
#         break
#---------------------------------------------------------------------------
# arr=[1,2,3,4,5,6]
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i])
#--------------------------------------------------------------------
# class Bank_Account:
#     def __init__(self,customer_name,balance,account_number):
#         self.customer_name = customer_name
#         self.__balance = balance
#         self.__account_number= account_number
#
#     def __del__(self):
#         print("This is destructor")
#
#     def getter(self):
#         return self.__balance
#
#     def setter(self,account_num):
#         self.__account_number = account_num
#
#     def getter1(self):
#         return self.__account_number
#
#
# obj1 = Bank_Account("Ragunandhan",1000000.0,12345678990)
# print("Customer name : ", obj1.customer_name)
# print("Balance : ", obj1.getter())
# obj1.setter(7653689999)
# print("account num : ",obj1.getter1())
# #print("Account number : ",)

# obj2 = Bank_Account("Balaji",12997652389,987654334)
# obj2.display()
# class Car:
#     def __init__(self,no_of_wheels,no_of_airbags,mileage):
#         self.no_of_wheels = no_of_wheels
#         self.__no_of_airbags = no_of_airbags
#         self.mileage = mileage
#
#     def getter(self,no_of_airbags):
#         return self.__no_of_airbags = no_of_airbags
#
#     def __del__(self):
#         print("this is destructor")
#
# customer1 = Car(4,5,25.6)
# print(customer1.no_of_wheels,customer1.no_of_airbags,customer1.mileage)
# string='ragunandhan'
# result=""
# for i in range(len(string)):
#     if ord(string[i]) >= 97 or ord(string[i]) <=122:
#         result+=chr(ord(string[i])-32)
# print(result)
# string = "ragu"
# result=""
# for i in range(len(string)-1,-1,-1):
#     result+=string[i]
# print(result)





# class Node:
#
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.List=[]
#
#     def print_LL(self):
#         if self.List is None:
#             print("Linked list is empty")
#         else:
#             while self.List is not None:
#                 print(self.List)
#                 self.List=self.List
#                 break
#
#     def addingTheElement(self,elements):
#         self.List.append(elements)
#
#     def inertingTheElements(self,indexes,values):
#         self.List.insert(indexes,values)
#
#     def deletingTheElements(self,val):
#         self.List.remove(val)


# LL = LinkedList()

# LL.addingTheElement("1")
# LL.addingTheElement("2")
# LL.addingTheElement("3")
# LL.deletingTheElements("2")
# LL.inertingTheElements(0,"Ragu")
# LL.print_LL()

# LL.addingTheElement("1")
# LL.addingTheElement("2")
# LL.addingTheElement("3")
# LL.addingTheElement("Ragu")
# LL.deletingTheElements("2")
# LL.inertingTheElements(0,"nandhan")
# LL.print_LL()
# LL.addingTheElement("2")
# LL.addingTheElement("3")
# LL.addingTheElement("Ragu")
# LL.deletingTheElements("2")
# LL.inertingTheElements(0,"ram")
# LL.print_LL()

# class Stack:
#
#     def __init__(self):
#         self.List = []
#
#     def push(self,element):
#         self.List.append(element)
#
#     def pop(self):
#         if self.List is not None:
#             self.List.pop()
#         else:
#             print("Nothing is there to delete")
#
#     def peek(self):
#         if self.List:
#             print(self.List[-1])
#         else:
#             print("Nothing to show")
#
#     def size(self):
#         if self.List:
#             print(len(self.List))
#         else:
#             print("Nothing to calculate")
#
#     def is_empty(self):
#         if self.List:
#             print(False)
#         else:
#             print(True)
#
# stack = Stack()
# stack.push("1")
# stack.push("2")
# stack.push("3")
# stack.push("Ragu")
# stack.push(56)
# stack.size()
# stack.pop()
# stack.size()
# stack.peek()
# stack.is_empty()
# stack.List.clear()
# stack.is_empty()
# stack.size()
# stack.peek()

# import collections
# def breadthfirst(d,val):
#     visited=set()
#     queue = collections.deque([val])
#     while queue:
#         vertex=queue.popleft()
#         visited.add(vertex)
#         for i in d[vertex]:
#             if i not in visited:
#                 queue.append(i)
#             else:
#                 visited.add(i)
#     print(visited)
#
# d={0:[1,2,3],1:[0,2],2:[0,1,4],3:[0],4:[2]}  d={'name':'ragu'}
# breadthfirst(d,0)
# class Stack:
#
#     def __init__(self):
#         self.List=[]
#
#     def push(self,elements):
#         self.List.append(elements)
#
#     def pop(self):
#         if self.List:
#             self.List.pop()
#         else:
#             print("Nothing to delete")
#
#     def peek(self):
#         if self.List:
#             print(self.List[-1])
#         else:
#             print("Nothing to show")
#
#     def size(self):
#         if self.List:
#             print(len(self.List))
#         else:
#             print("Nothing to calculate")
#
#     def is_empty(self):
#         if self.List:
#             print(False)
#         else:
#             print(True)
#
# stack = Stack()
# stack.push("1")
# stack.push("2")
# stack.push(3)
# stack.push("ragu")
# stack.pop()
# stack.peek()
# stack.size()
# stack.is_empty()
# stack.List.clear()
# stack.is_empty()
# stack.pop()
# stack.peek()


# class Queue:
#
#     def __init__(self):
#         self.List=[]
#
#     def enqueue(self,elements):
#         self.List.append(elements)
#
#     def dequeue(self):
#         if self.List:
#             self.List.pop(0)
#         else:
#             print("Nothing to delete")
#
#     def size(self):
#         if self.List:
#             print(len(self.List))
#         else:
#             print("nothing to calculate")
#
#     def is_empty(self):
#         if self.List:
#             print(False)
#         else:
#             print(True)
#
# queue = Queue()
# queue.enqueue("12")
# queue.enqueue(45)
# queue.enqueue("ragu")
# queue.enqueue("nandhan")
# queue.enqueue("90")
# queue.enqueue("54")
# queue.size()
# queue.dequeue()
# queue.size()
# queue.List.clear()
# queue.size()
# queue.is_empty()
#
# output:
# 6
# 5
# nothing to calculate
# True



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.pointer=None
# class LinkedList:
#
#     def __init__(self):
#         self.head=None
#     def add(self,data):
#         New_Node=Node(data)
#         if self.head is None:
#             self.head=New_Node
#         else:
#             cur=self.head
#             while(cur.pointer is not None):
#                 cur=cur.pointer
#             cur.pointer = New_Node
# obj=LinkedList()
# obj.add(5)



# list1 = [1,2,3,4]
# # print(id(list1))
# for i in list1:
#     print(id(i))

# d={"ragu":[1,2,3,4],(1,"ragu",7):(6,"hello",89)}
#
# print(d)



class HashMap:

    def __init__(self,size):
        self.size=size
        self.HashList=[None]*self.size

    def get(self,key):
        return hash(key) % self.size


    def __setitem__(self, key, value):
        index=self.get(key)
        if self.HashList[index] is None:
            self.HashList[index]=[[key,value]]
            print(self.HashList)
        else:
            self.HashList.append([key,value])

    def __getitem__(self,key):
        index=self.get(key)
        if self.HashList[index] is not None:
            sublist=self.HashList[index]
            for pair in sublist:
                if pair[0]==key:
                    return pair[1]

    def __delitem__(self, key):
        index=self.get(key)
        if self.HashList[index] is not None:
            sublist=self.HashList[index]
            for i,pair in enumerate(sublist):
                if pair[i]==key:
                    del sublist[i]



h=HashMap(10)
h["name"]="mukil"
h["age"]=90

print(h["name"])
print(h["age"])



# class HashMap:
#
#     def __init__(self):
#         self.size = 10
#         self.hashlist = [None]*self.size
#
#     def GetIndex(self,key):
#         index=hash(key) % self.size
#         return index
#
#     def __setitem__(self, key, value):
#         Index = self.GetIndex(key)
#
#         if self.hashlist[Index] is None:
#             self.hashlist[Index] = [[key,value]]
#         else:
#             # if self.hashlist[Index]  is not None:
#             self.hashlist.append([key,value])
#
#     def __getitem__(self, key):
#         Index=self.GetIndex(key)
#         if self.hashlist[Index] is not None:
#             sublist = self.hashlist[Index]
#             for pair in sublist:
#                 if pair[0] == key:
#                     return pair[1]
#
#     def __delitem__(self, key):
#         Index = self.GetIndex(key)
#
#         if self.hashlist[Index] is not None:
#             sublist = self.hashlist[Index]
#             for i,pair in enumerate(sublist):
#                 if pair[i] == key:
#                     del sublist[i]
# hm=HashMap()
# hm['name'] = "mani"
# hm["age"] =100
# del hm["name"]
# print(hm.hashlist)










