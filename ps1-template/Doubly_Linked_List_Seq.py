class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    # returns i_th node from current node
    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        # create node with item x
        x = Doubly_Linked_List_Node(x)

        # if list is empty, add x as only element
        if self.head is None:
            self.head = x
            self.tail = x
            return

        # get the first element and connect it to x
        first = self.head
        first.prev = x

        # connect x to first
        x.next = first

        # set x as the head
        self.head = x

    def insert_last(self, x):
        # create node with item x
        x = Doubly_Linked_List_Node(x)

        # if list is empty add, x as the only element
        if self.tail is None:
            self.tail = x
            self.head = x

        # get the last element and connect it to x
        last = self.tail
        last.next = x

        # connect x to last element
        x.prev = last

        # set x as the tail
        self.tail = x

    def delete_first(self):
        # get first two elements
        first = self.head
        second = first.next

        # set second element as head ot the list
        second.prev = None
        self.head = second
        return first.item

    def delete_last(self):
        # get last two elements
        last = self.tail
        second_last = last.prev

        # set second last element as tail of the list
        second_last.next = None
        self.tail = second_last
        return last.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()

        # Neither x1 nor x2 is the head or tail
        if x1.prev is not None and x2.next is not None:
            # connect the element before x1 to the element after x2
            x1.prev.next = x2.next
            x2.next.prev = x1.prev
        # if x1 is the head but x2 is not tail
        elif x1.prev is None and x2.next is not None:
            # disconnect elements x1 to x2 from the list
            self.head = x2.next
            self.head.prev = None
        # if x2 is the tail but x1 is not head
        elif x2.next is None and x1.prev is not None:
            # disconnect elements from x1 to x2 from the list
            self.tail = x1.prev
            self.tail.next = None
        # x1 is head and x2 is tail
        else:
            self.head = None
            self.tail = None

        # disconnect the links to any element before x1 and any elment
        x1.prev = None
        x2.next = None

        # set the head and tail of L2
        L2.head = x1
        L2.tail = x2
        return L2

    def splice(self, x, L2):
        # if L2 is empty, return None
        if L2.head is None:
            return
        
        # get the element after x
        x_next = x.next

        # connect x to head of L2
        x.next = L2.head
        L2.head.prev = x

        # there was an element after x, connect it to tail of L2
        if x_next is not None:
            x_next.prev = L2.tail
            L2.tail.next = x_next

        # set the tail of current list as tail of L2
        self.tail = L2.tail

        # remove all elements from L2
        L2.head = None
        L2.tail = None
