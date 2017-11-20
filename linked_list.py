class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        
        #start iterating at the beginning of LL
        current_node = self.head
        counter = 0
        #iterate through list until LL ends
        while current_node is not None:
            #count node
            counter += 1
            #move to next node in LL
            current_node = current_node.next
        return counter
        
        

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""

        #create a new node
        new_node = Node(item)
        #if LL is empty
        if self.is_empty():
        #set both head and tail pointer to new node
            self.head = new_node
            self.tail = self.head
        else:
        #set tail pointer to new node
            self.tail.next = new_node
        #set new node as the tail
        self.tail = new_node

    def prepend(self, item):
         """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        
        #initiaize new node with the inputed data
        new_node = Node(item)

        #if LL is empty, set the tail and head pointer to the new node 
        if self.is_empty():
            self.tail  = new_node
            self.head = self.tail

        #if LL is not empty, the new node next pointer to the current head
        else:
            new_node.next = self.head
        #point the head pointer at the new node
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""

        #start traversing at the head
        current_node = self.head
        item = None

        while current_node is not None:
            #if the item in the list matches the item that we're looking for
            #get nodes data and store it in the item variable
            if quality(current_node.data):
                item = current_node.data
                return item
            #keep traversing through the list until we find the 
            #node with correct data 
            else:
                current_node = current_node.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""

        #if there no item in the list to delete
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        #using lamba and find method to match inputed item to item in list   
        search_item = self.find(lambda item_: item_ == item) 

        #if the item inputed does not exist in the list, raise ValueError
        if search_item is None:
            raise ValueError('Item not found: {}'.format(item))
        
        previous_node = None
        current_node = self.head
        #while we are not at the end of the lsit
        while current_node is not None:
            if current_node.data != item:
                #if we havent found the item, move to the next item
                #save last node in previous_node variable to keep track of node before current
                previous_node = current_node
                current_node = current_node.next
                #traversing through LL

            #if we have found the item
            elif current_node.data == item:
                #if the node we want to delete is the head
                if current_node == self.head:
                    #set the next node in list as the head, losing pointer deletes node
                    self.head = current_node.next
                    #if the node we want to delete is the tail    
                    if current_node == self.tail:
                        #set the previous node equal to the tail, losing pointer deletes the node
                        self.tail = previous_node
                    break
                #if we found the item and it is not the head nor the tail, point the
                #previous nodes pointer to the one after the current node
                #losing pointer deletes the node
                previous_node.next = current_node.next
                if current_node == self.tail:
                    self.tail = previous_node
                break
            
def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()