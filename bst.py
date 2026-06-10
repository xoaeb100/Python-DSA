# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None



# class  BinarySearchTree:
#     def __init__(self):
#         self.root = None
        
        
#     def insert(self, value):
#         new_node = Node(value)
        
#         if self.root  == None:
#             self.root =new_node
#             return True
#         temp = self.root
#         while (True):
#             if new_node.value == temp.value :
#                 return False
#             if new_node.value < temp.value:
#                 if temp.left  == None:
#                     temp.left = new_node
#                     return True
#                 temp = temp.left
#             else: 
#                 if temp.right  == None:
#                     temp.right = new_node
#                     return True
#                 temp = temp.right                 
        
#     def contains(self, value):
#         temp = self.root
#         while temp is not None:
#             if (value < temp.value):
#                 temp = temp.left
                
#             elif (value > temp.value):
#                 temp = temp.right
#             else:
#                 return True
#         return False
    
# # simplified by ChatGPT
# # def contains(self, value):
# #     temp = self.root
# #     while temp:
# #         if value == temp.value:
# #             return True
# #         temp = temp.left if value < temp.value else temp.right
# #     return False

        
# myTree = BinarySearchTree()
# myTree.insert(2)
# myTree.insert(1)
# myTree.insert(3)
# myTree.insert(2)
# myTree.insert(6)

# print(myTree.contains(0))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Bst:
    def __init__(self):
        self.root  = None
    def insert(self, value):
            new_node = Node(value)
            if self.root is None:
                self.root = new_node
                return True
            
            temp = self.root
            while True:
                # Handle duplicates
                if new_node.value == temp.value:
                    return False
                
                # Navigate Left
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                
                # Navigate Right
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right
                    
        
    def contains(self, value):
        temp = self.root
        while temp is not None:
            
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True 
        return False

                
        
        
        
        
        
        
myTree = Bst()
myTree.insert(2)
myTree.insert(1)
myTree.insert(3)
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
print(myTree.contains(21 ))
