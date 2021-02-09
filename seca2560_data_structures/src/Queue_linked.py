"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   seca2560@mylaurier.ca
__updated__ = "2020-03-05"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        newnode = _Queue_Node(value, None)
        if self._count == 0:
            self._front = newnode
            self._rear = newnode
            self._count += 1
        else:
            self._rear._next = newnode
            self._rear = newnode
            self._count += 1
        
        
        
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"
        if self._count != 0:
            temp = self._front 
            self._front = self._front._next
            temp._next = None
            value = deepcopy(temp._value)
            self._count -= 1
        else:
            value = None
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"
        
        if self._count != 0:
            value = deepcopy(self._front._value)
        else:
            value = None

        return value

    def _move_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"
        if self._count != 0:
            source.insert(deepcopy(self.remove()))
        
        
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
        assert source._front is not None, "Cannot append an empty queue"

        # your code here
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
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
#                 self.insert(source1.remove())
#                 self.insert(source2.remove())
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based queue (Queue)
            source2 - an array-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        
        target1 = Queue()
        target2 = Queue()
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
            
        return target1, target2
        

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (recursive algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        # your code here
        return

    def is_identical(self, other):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        if self._count == other._count != 0:
            identical = True
            current1 = self._front
            current2 = other._front
            while identical == True and current1 is not None and current2 is not None:
                if current1._value != current2._value:
                    identical = False
                else:
                    current1 = current1._next
                    current2 = current2._next
        else:
            identical = False
        if self._count == other._count == 0:
            identical = True

        return identical

    def is_identical_r(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Entries of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (recursive algorithm)
        Use: b = source.is_identical_r(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next