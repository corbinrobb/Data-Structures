class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next_node):
        self.next_node = new_next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)

        if not self.head and not self.tail:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None

        data = self.head.get_data()

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()

        return data

    # Return True or False depending on whether the list contains the data
    def contains(self, data):
        # If list empty return false
        if self.head == None:
            return False

        current_node = self.head

        contained = False

        # Start looping through list
        while current_node is not None:
            # if found return true and end loop
            if current_node.get_data() == data:
                contained = True
                break
            # set current to next node and restart loop
            current_node = current_node.get_next()

        return contained

    def get_max(self):
        if self.head is None:
            return None

        current_node = self.head
        max_num = current_node.get_data()

        while True:
            if current_node.get_data() > max_num:
                max_num = current_node.get_data()

            if current_node.get_next() == None:
                break

            current_node = current_node.get_next()

        return max_num
