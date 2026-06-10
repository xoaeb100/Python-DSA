class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):
        slow= self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast= fast.next.next
        return slow
            
    def find_kth_from_end(ll, k):
        slow= ll.head
        fast=ll.head
        
        for _ in range(k):
            if fast is None:
                return False
            fast = fast.next
            
        while fast:
            slow= slow.next
            fast=fast.next
        return slow     
    
    def removeDuplicates(self): 
        current = self.head
        while current is not None:
            nextNode =  current
            while nextNode.next is not None:
                if nextNode.next.value == current.value:
                # Found a duplicate! Skip it.
                    nextNode.next = nextNode.next.next
                else:
                # Only move nextNode forward if we didn't delete a node
                    nextNode = nextNode .next
            current = current.next
            
    def binary_to_decimal(self):
        current= self.head
        result =0
        
        if current.next == None:
            return current.value
        while current is not None:
            result =result *2 + current.value
            current = current.next
        return result
    
    
    
    def partition_list(self, x):
        if not self.head:
            return None

        # Create two dummy nodes to start our two partitions
        dummy1 = Node(0)
        dummy2 = Node(0)
        
        # Pointers to the current end of each partition
        prev1 = dummy1
        prev2 = dummy2
        
        current = self.head
        
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            
            current = current.next
        
        # IMPORTANT: Prevent a cycle in the list
        prev2.next = None
        
        # Connect the end of the "less than" list to the start of the "greater than" list
        prev1.next = dummy2.next
        
        # Update the actual head of the original list
        self.head = dummy1.next


    def swap_pairs(self):
        if not self.head or not self.head.next:
            return self.head
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Swapping
            prev.next, first.next, second.next = second, second.next, first
            
            # Move prev two nodes ahead
            prev = first
        
        self.head = dummy.next

# [3, 2, 4, 5, 8, 10]
my_linked_list = LinkedList(3)

my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(8)

# my_linked_list.printList()

print(my_linked_list.partition_list(5))

# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
# my_linked_list.removeDuplicates()
# my_linked_list.printList()
# print( my_linked_list.find_middle_node().value )


# k = 5
# result = my_linked_list.find_kth_from_end( k)

# print(result.value) 




