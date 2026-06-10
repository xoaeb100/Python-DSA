# class HashTable:
#     def __init__(self, size =7):
#         self.data_map = [None] * size
        
#     def __hash(self, key):
#         my_hash=0
#         for letter in key:
#             my_hash= (my_hash + ord(letter) *23) % len(self.data_map)
#         return my_hash
#     def printTable(self):
#         for i, val in enumerate(self.data_map):
#             print(i, ": ", val)
            
# my_hash_table = HashTable()
# my_hash_table.printTable()




class HashTable:
    def __init__(self, size =7):
        self.data_map  = [None] * size
    def __hash(self,key):
        my_hash =0
        for letter in key:
            my_hash = (my_hash + ord(letter) *31) % len (self.data_map)
        return my_hash
    
    def printTable(self):
        for i, value in enumerate(self.data_map):
            print(i, ':  ', value) 
            
    def setItem(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] ==None:
            self.data_map[index]  = []
        self.data_map[index].append([key,value])
        
        
    def getItem(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index] [i][0] == key:
                    return  self.data_map[index] [i][1]
        return None


def areItemsCommon(list1, list2):
    for i in list1:
        for j in list2:
            if i ==j:
                return True
    return False

def areItemsCommon2(list1, list2):
    my_dictionary = {}
    for i in list1:
        my_dictionary[i] = True
    for j in list2:
        if j in my_dictionary:
            return True
    return False
            
my_hashMap = HashTable()
my_hashMap.setItem("apple", '40')
my_hashMap.setItem("mango", '60')
my_hashMap.setItem("grapes", '30')
my_hashMap.setItem("pineapples", '70')

# my_hashMap.printTable()

# print(my_hashMap.getItem('grapes'))


print(areItemsCommon2([1,3,6,8,4,2],[9,9,6]))
