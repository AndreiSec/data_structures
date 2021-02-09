"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   seca2560@mylaurier.ca
__updated__ = "2020-03-05"
-------------------------------------------------------
"""
from copy import deepcopy


class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """

        # Your code here

        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """

        # Your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        if self._count > 0:
            if value >= self._rear._value:
                self._rear._next = end =_PQ_Node(value, None)
                self._rear = end
                self._count += 1
            elif value <= self._front._value:
                self._front = _PQ_Node(value, self._front)
                self._count += 1
            else:
                current = self._front
                placed = False
                while current is not None and placed != True:
                    if current._value <= value and value <= current._next._value:
                        v = current._next
                        current._next = kl =_PQ_Node(value, current._next._next)
                        kl._next = v
                        self._count += 1
                        placed = True
                    current = current._next
        else:
            self._front = _PQ_Node(value, None)
            self._rear = self._front
            self._count += 1
        
        # your code here
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"

        value = deepcopy(self._front._value)
        self._front = self._front._next
        self._count -= 1

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"


        # Your code here

        return deepcopy(self._front._value)

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """

        target1 = Priority_Queue()
        target2 = Priority_Queue()
        if self._count > 0:
            current = self._front
            oe = 0
            while self._count != 0:
                if oe == 0:
                    if target1._count == 0:
                        target1._front = self._front 
                        target1._rear = self._front
                        self._front = self._front._next
                        target1._front._next = None
                        target1._count += 1
                        self._count -= 1
                    else:
                        temp = self._front
                        target1._rear._next = self._front
                        target1._rear = self._front
                        self._front = self._front._next
                        temp._next = None
                        target1._count += 1
                        self._count -= 1
                    oe += 1
                elif oe == 1:
                    if target2._count == 0:
                        target2._front = self._front 
                        target2._rear = self._front
                        self._front = self._front._next
                        target2._front._next = None
                        target2._count += 1
                        self._count -= 1
                    else:
                        temp = self._front
                        target2._rear._next = self._front
                        target2._rear = self._front
                        self._front = self._front._next
                        temp._next = None
                        target2._count += 1
                        self._count -= 1
                    oe -= 1
        self._front = None
        self._rear = None
        self._count = 0   
        return target1, target2


    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """

        target1 = Priority_Queue()
        target2 = Priority_Queue()
        if self._count > 0:
            current = self._front
            if current._value < key:
                oe = 0
            elif current._value >= key:
                oe = 1
            while self._count != 0:
                if oe == 0:
                    if target1._count == 0:
                        target1._front = self._front 
                        target1._rear = self._front
                        self._front = self._front._next
                        target1._front._next = None
                        target1._count += 1
                        self._count -= 1
                    else:
                        temp = self._front
                        target1._rear._next = self._front
                        target1._rear = self._front
                        self._front = self._front._next
                        temp._next = None
                        target1._count += 1
                        self._count -= 1
                    oe += 1
                elif oe == 1:
                    if target2._count == 0:
                        target2._front = self._front 
                        target2._rear = self._front
                        self._front = self._front._next
                        target2._front._next = None
                        target2._count += 1
                        self._count -= 1
                    else:
                        temp = self._front
                        target2._rear._next = self._front
                        target2._rear = self._front
                        self._front = self._front._next
                        temp._next = None
                        target2._count += 1
                        self._count -= 1
                    oe -= 1
                current = self._front
                if current is not None:
                    if current._value < key:
                        oe = 0
                    elif current._value >= key:
                        oe = 1
        self._front = None
        self._rear = None
        self._count = 0   
        return target1, target2

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        while source1._count != 0 or source2._count != 0:
            if source1._count == 0:
                while source2._count != 0:
                    if self._count == 0:
                        self._front = source2._front 
                        self._rear = source2._front
                        source2._front = source2._front._next
                        self._front._next = None
                        self._count += 1
                        source2._count -= 1
                    else:
                        temp = source2._front
                        self._rear._next = source2._front
                        self._rear = source2._front
                        source2._front = source2._front._next
                        temp._next = None
                        self._count += 1
                        source2._count -= 1
#                     self.insert(source2.remove())
            elif source2._count == 0:
                while source1._count != 0:
                    if self._count == 0:
                        self._front = source1._front 
                        self._rear = source1._front
                        source1._front = source1._front._next
                        self._front._next = None
                        self._count += 1
                        source1._count -= 1
                    else:
                        temp = source1._front
                        self._rear._next = source1._front
                        self._rear = source1._front
                        source1._front = source1._front._next
                        temp._next = None
                        self._count += 1
                        source1._count -= 1
#                     self.insert(source1.remove())
            else:
                if self._count == 0:
                    self._front = source1._front 
                    self._rear = source1._front
                    source1._front = source1._front._next
                    self._front._next = None
                    self._count += 1
                    source1._count -= 1
                    temp = source2._front
                    self._rear._next = source2._front
                    self._rear = source2._front
                    source2._front = source2._front._next
                    temp._next = None
                    self._count += 1
                    source2._count -= 1
                    
                else:
                    temp = source1._front
                    self._rear._next = source1._front
                    self._rear = source1._front
                    source1._front = source1._front._next
                    temp._next = None
                    self._count += 1
                    source1._count -= 1
                    temp = source2._front
                    self._rear._next = source2._front
                    self._rear = source2._front
                    source2._front = source2._front._next
                    temp._next = None
                    self._count += 1
                    source2._count -= 1
        
        source1._rear = None  
        source2._rear = None
        source2._front = None
        source1._front = None
        source1._count = 0
        source2._count = 0
        
        
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"


        # Your code here

        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"


        # Your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next