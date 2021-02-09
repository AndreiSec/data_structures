"""
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   seca2560@mylaurier.ca
Section: CP164 A
__updated__ = "2019-09-07"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:
    #items = []
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an is_empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the stack is empty, False otherwise
        -------------------------------------------------------
        """
        
        return self._values == []
        # Your code here
    
    def reverse(self):
        """
        Reverses a stack.
        Use: s.reverse()
        """
        self._values = self._values[::-1]
        
        return
        
    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        # Your code here

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"
        return self._values.pop()
        # Your code here

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"
        return deepcopy(self._values[-1])
        # Your code here


    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
            
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        #print(len(self._values))
        target1 = Stack()
        target2 = Stack()
        while len(self._values) != 0:
            target1._values.append(deepcopy(self._values[-1]))
            del self._values[-1]
            if len(self._values) != 0:
                target2._values.append(deepcopy(self._values[-1]))
                del self._values[-1]
        return target1, target2
    
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        while len(source1._values) != 0 or len(source2._values) != 0:
            if len(source1._values) == 0:
                while len(source2._values) != 0:
                    self._values.append(deepcopy(source2._values[-1]))
                    del source2._values[-1]
            elif len(source2._values) == 0:
                while len(source1._values) != 0:
                    self._values.append(deepcopy(source1._values[-1]))
                    del source1._values[-1]
            else:
                self._values.append(deepcopy(source1._values[-1]))
                del source1._values[-1]
                self._values.append(deepcopy(source2._values[-1]))
                del source2._values[-1]
        return
                