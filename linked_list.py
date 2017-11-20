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
        # TODO: Loop through all nodes and count one for each
        
        #optimized working code
        
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

        #optimized code
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
        new_node = Node(item)

        if self.is_empty():
            self.tail  = new_node
        else:
            new_node.next = self.head
        self.head = new_node


        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        current_node = self.head
        item = None
        while current_node is not None:
            if quality(current_node.data):
                item = current_node.data
                return item
            else:
                current_node = current_node.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""

        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        search_item = self.find(lambda item_: item_ == item) 
        if search_item is None:
            raise ValueError('Item not found: {}'.format(item))
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if current_node.data != item:
                previous_node = current_node
                current_node = current_node.next
                #traversing through LL
            elif current_node.data == item:
                if current_node == self.head:
                    self.head = current_node.next    
                    if current_node == self.tail:
                        self.tail = previous_node
                    break
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