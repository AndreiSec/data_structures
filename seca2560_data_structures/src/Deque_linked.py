"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   seca2560@mylaurier.ca
__updated__ = "2020-03-05"
-------------------------------------------------------
"""

# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
#         node = _Deque_Node(value, _prev, _next)
        newnode = _Deque_Node(value, None, self._front)
        if self._count > 0:
            self._count += 1
            self._front._prev = newnode
            self._front = newnode
        else:
            self._front = newnode
            self._rear = newnode
            self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        newnode = _Deque_Node(value, self._rear, None)
        if self._count > 0:
            self._count += 1
            self._rear._next = newnode
            self._rear = newnode
        else:
            self._front = newnode
            self._rear = newnode
            self._count += 1
            
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"
        
        if self._count == 1:
            value = deepcopy(self._front._value)
            self._front._next = None
            self._front._prev = None
            self._front = None
            self._rear = None
            self._count -=1
            
        else:
            value = deepcopy(self._front._value)
            temp = self._front._next
            self._front._next = None
            self._front._prev = None
            self._front = temp
            self._front._prev = None
            self._count -= 1
        
        
        
        
        
        
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        if self._count == 1:
            value = deepcopy(self._front._value)
            self._rear._next = None
            self._rear._prev = None
            self._front = None
            self._rear = None
            self._count -=1
            
        else:
            value = deepcopy(self._rear._value)
            temp = self._rear._prev
            self._rear._next = None
            self._rear._prev = None
            self._rear = temp
            self._rear._next = None
            
            self._count -= 1
        
        
        
        
        
        
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"
        if self._count > 0:
            value = deepcopy(self._front._value)
        else:
            value = None
        
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        if self._count > 0:
            value = deepcopy(self._rear._value)
        else:
            value = None
        
        return value
    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
        if self._count > 1:
            if l._next != r and l._prev != r:
                templnext = l._next
                templprev = l._prev
                together = False
            else:
                templnext = l._next
                templprev = l._prev
                together = True
            if l._next is None:
                l._prev._next = r
                self._rear = r
            if r._next is None:
                r._prev._next = l
                self._rear = l
            if l._prev is None:
                l._next._prev = r
                self._front = r
            if r._prev is None:
                r._next._prev = l
                self._front = l
             
            if together == True:
                if l._next == r:
                    if l._next is not None and l._prev is not None:
                        l._prev._next = r
                    if r._next is not None and r._prev is not None:
                        r._next._prev = l
                    r._prev = l._prev
                    l._next = r._next
                    r._next = l
                    l._prev = r
                elif l._prev == r:
                    if l._next is not None and l._prev is not None:
                        l._next._prev = r
                    if r._next is not None and r._prev is not None:
                        r._prev._next = l
                    l._next = r
                    l._prev = r._prev
                    r._next = templnext
                    r._prev = l
        
            elif together == False:
                if l._next is not None and l._prev is not None:
                    l._prev._next = r
                    l._next._prev = r
                if r._next is not None and r._prev is not None:
                    r._prev._next = l
                    r._next._prev = l
                l._next = r._next
                l._prev = r._prev
                r._next = templnext
                r._prev = templprev
        
        
        
        
        
        
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next