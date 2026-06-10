class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def left_child(self,index):
        return (index *2 )+1 
    
    def right_child(self,index):
        return (index *2 )+2
    
    def parent(self,index):
        return (index -1) //2
    
    def swap (self,index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2] , self.heap[index1]   
        
        
    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) -1
        
        while current >0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current,self.parent(current))
            current = self.parent(current)
            
my_heap = MaxHeap()
my_heap.insert(10)
my_heap.insert(20)
my_heap.insert(5)
print(my_heap.heap)