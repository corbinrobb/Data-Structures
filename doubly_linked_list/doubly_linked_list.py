"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.head:
            new_node = ListNode(value, None, self.head)
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return new_node
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.head is self.tail:
            removed = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed
        else:
            new_head = self.head.next
            removed = self.head.value
            self.head.delete()
            self.head = new_head
            self.length -= 1
            return removed

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.tail:
            new_node = ListNode(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return new_node
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.head is self.tail:
            removed = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed
        else:
            new_tail = self.tail.prev
            removed = self.tail.value
            self.tail.delete()
            self.tail = new_tail
            self.length -= 1
            return removed

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        prev_head = self.head

        if node is self.tail:
            self.tail = node.prev

        node.delete()
        self.head = node
        self.head.next = prev_head
        self.head.next.prev = node
        self.head.prev = None

        if self.head.next.next is None:
            self.tail = prev_head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        prev_tail = self.tail

        if node is self.head:
            self.head = node.next

        node.delete()
        self.tail = node
        self.tail.prev = prev_tail
        self.tail.prev.next = self.tail
        self.tail.next = None

        if self.tail.prev.prev is None:
            self.head = prev_tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        if node == self.head:
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
        elif node == self.tail:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
        else:
            node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        current_node = self.head
        highest = current_node.value
        while current_node is not None:
            if current_node.value > highest:
                highest = current_node.value
            current_node = current_node.next
        return highest
