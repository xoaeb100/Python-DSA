# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def printList(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp

#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp

#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False

#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             print("thik se likh")
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node = Node(value)
#         temp = self.get(index - 1)
#         new_node.next = temp.next
#         temp.next = new_node
#         self.length += 1
#         return True

#     def remove(self, index):
#         if index < 0 or index > self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == self.length:
#             return self.pop()
#         temp = self.get(index)
#         pre = self.get(index - 1)
#         pre.next = temp.next
#         temp.next = None
#         self.length -= 1
#         return temp
    
    
    
#     # VERY IMP ⭐⭐⭐⭐💫
#     def reverse(self):
#         temp= self.head
#         before= None
#         after= temp.next
#         self.head= self.tail
#         self.tail= temp
#         for i in range(self.length):
#             after= temp.next
#             temp.next=before
#             before= temp
#             temp=after


# myLinkedList = LinkedList(5)
# myLinkedList.append(9)
# myLinkedList.append(39)

# # myLinkedList.printList()
# # myLinkedList.pop()
# # myLinkedList.printList()

# myLinkedList.prepend(1)
# myLinkedList.printList()
# # popped_node = myLinkedList.pop_first()
# # print("Popped value:", popped_node.value)

# # print(myLinkedList.get(2))

# # myLinkedList.set_value(2, 69)
# # myLinkedList.remove(2)
# # myLinkedList.insert(2, 25)

# myLinkedList.reverse()
# print("****new list***")
# myLinkedList.printList()

# create ll
# print ll
# append
# prepend
# pop
# pop_first


# print, append, prepend, pop, popfirst, get, set, remove

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length= 1
        
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def appendToList(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length+=1
        
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length+=1
        
    def pop(self):
        if(self.length == 0):
            return None
        elif(self.length ==1):
            return self.head.value
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp= temp.next
        pre.next = None
        self.tail = pre
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def popFirst(self):
        if(self.length == 0):
            return None
        elif(self.length ==1):
            return self.head.value
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def get(self, index):
        if(index< 0 or index >=self.length):
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
       
        temp = self.get(index)  
        if temp:
            temp.value = value
            return True 
        
    def insert(self, index, value):
        if(index< 0 or index >=self.length):
            return None
        elif (index == self.length):
            return self.appendToList(value)
        elif(index == 0):
            return self.prepend(value)
        temp = self.get(index)
        pre = self.get(index-1)
        new_node = Node(value)
        pre.next = new_node
        new_node.next = temp
        self.length +1
        return True

    def remove (self,index):
        if(index< 0 or index >=self.length):
            return None
        elif (index == self.length):
            return self.pop(index)
        elif(index == 0):
            return self.popFirst(index)
        temp = self.get(index)
        pre = self.get(index-1)
        pre.next = temp.next
        temp.next = None
        self.length-=1
        return True
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        before = None
    
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        



        
myLL = LinkedList(1)
myLL.prepend(-1)
myLL.appendToList(3)
myLL.appendToList(5)
myLL.appendToList(7)
myLL.appendToList(9)



# myLL.printList()
# print(myLL.get(4))
myLL.set(4, 69)
myLL.insert(2, 9)
myLL.remove(5)

myLL.printList()
myLL.reverse()

myLL.printList()