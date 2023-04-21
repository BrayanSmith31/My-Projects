class Node:
    def __init__(self,data, ref = None):
        self.data = data
        self.ref = ref
class LinkedList:
    def __init__(self):
        self.head = None   # The head contains the reference of the first node

    #Method to travel the linked list, it basically print the list values
    def print_linkedListValues(self):
        if self.head is None:
            print("Linked List is empty, has no values")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    #Method to Insert an element at the beggining of the link list
    def add_begin(self, data):
        # 1. We need to create a new node
        new_node = Node(data)
        
        # 2. Now the reference of the new node is None, so we need to change it to be the head
        new_node.ref = self.head

        # 3. We need to set the head as the reference and be pointed at the new node, this is the new head
        self.head = new_node
    
    #Method to Insert an element at the end of the link list
    def add_end(self, data):
        # 1. We need to create de node
        new_node = Node(data)
        # 2. We need to checkt if the link list is empty
        if self.head is None:
            #3. If link list is empty we set the head as a reference
            self.head = new_node
        else:
            # 4. If it's not empty then we loop until the last node
            n = self.head
            while n.ref is not None:
                n = n.ref
            # 5. When we get the last node,we assign that  last reference to pointed at the new node
            n.ref = new_node

    #Method to add between nodes, especifically AFTER a node
    def add_after_node(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x :
                break
            n = n.ref
        if n is None:
            print("There is not a value f{x} in the LinkedList")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    #Method to add between nodes, especifically BEFORE a node
    def add_before_node(self, data, x):
        if self.head is None:
            print("The linked list is empty!!")
            return # This will allow us to not execute the next if statement and get out of the function
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("There is no data f{x} in the Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node 
#Así se crea una lista utilizando las dos clases

LL = LinkedList()
LL.add_end(8)
LL.add_begin(70)
LL.add_begin(5)
LL.add_after_node(20,70)
LL.add_before_node(55,20)
LL.print_linkedListValues()
