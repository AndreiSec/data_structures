"""
-------------------------------------------------------
Linked version of the Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B, C
__updated__ = "2020-04-20"
-------------------------------------------------------
"""
# Imports

from copy import deepcopy 


class _Set_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a Set node that contains a copy of value
        and a link to another Set node.
        Use: node = _Set_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Set node (_Set_Node)
        Returns:
            a new _Set_Node object (_Set_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Set.
        Use: set = Set()
        -------------------------------------------------------
        Returns:
            A new Set object (Set)
        -------------------------------------------------------
        """
        self._front = None
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Set.
        Use: n = len(set)
        -------------------------------------------------------
        Returns:
            the number of values in the Set (int)
        -------------------------------------------------------
        """
        # your code here
        current = self._front
        n = 0
        while current._next is not None:
            n += 1 
            current = current._next
        return n

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Set is empty.
        Use: b = set.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front == None

    def add(self, value):
        """
        ---------------------------------------------------------
        Adds value to the end of the Set, allows only one copy of value.
        Use: inserted = set.add(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            True if value is inserted, False otherwise (boolean)
        -------------------------------------------------------
        """
        inserted = False
        currentnode = self._front
        
        if self._front == None:
            inserted = True
            node = _Set_Node(value, None)
            self._front = node
            
        else:
            if currentnode and currentnode._value != value:
                node = _Set_Node(value, None)
                while currentnode._next is not None and currentnode._next._value != value:
                    currentnode = currentnode._next
                
                if currentnode._next is None:
                    currentnode._next = node

        return inserted

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in set.
        Private helper method.
        Use: prev, curr = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            prev - pointer to the node prev to the node containing key (_setNode)
            curr - pointer to the node containing key (_setNode)
        -------------------------------------------------------
        """
        prev = None
        currentnode = self._front
        if currentnode is None:
            prev = None
            currentnode = None
        else:
            while key != currentnode._value and currentnode._next is not None:
                prev = currentnode
                currentnode = currentnode._next
                
            if currentnode._next is None and currentnode._value != key:
                prev = currentnode
                currentnode = None
                
        return prev, currentnode

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in set that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        _, current = self._linear_search(key)
        if current is not None:
            value = deepcopy(current._value)
            
        else:
            value = None
            
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in set that matches key.
        Returns None if no matching value.
        Use: value = set.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        prev, currentnode = self._linear_search(key)
        
        if currentnode is not None and prev is not None:
            value = deepcopy(currentnode._value)
            prev._next = currentnode._next
            currentnode = currentnode._next
            
        elif currentnode == self._front:
            value = deepcopy(currentnode._value)
            self._front = self._front._next
            
        else:
            value = None
            
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Set contains key.
        Use: b = key in set
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Set contains key, False otherwise.
        -------------------------------------------------------
        """
        currentnode = self._front
        b = False
        while key != currentnode._value and currentnode._next is not None:
            current = currentnode._next
        if key == current._value:
            b = True
        return b

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in set.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        prev = None
        current = self._front
        while current is not None:
            next = current._next 
            current._next = prev
            prev = current
            current = next 
        self._front = prev
        
        return 

    def split_th(self):
        """
        -------------------------------------------------------
        Splits source into two parts. target1 contains the first half,
        target2 the second half. curr set becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = source.split_th()
        -------------------------------------------------------
        Returns:
            target1 - a new set with >= 50% of the original set (Set)
            target2 - a new set with <= 50% of the original set (Set)
        -------------------------------------------------------
        """
        target1 = Set()
        target2 = Set()
        
        if self._front is None:
            target1._front = None
            target2._front = None
        else:
            target1._front = self._front
            tortoise = self._front
            hare = self._front._next
            
            while hare is not None and hare._next is not None:
                tortoise = tortoise._next
                hare = hare._next._next
            target2._front = tortoise._next
            tortoise._next = None
            self._front = None
            
        return target1, target2
    
            
            
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source sets into the curr target set.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked set (Set)
            source2 - an linked set (Set)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        curr1 = source1._front
        curr2 = source2._front
        left = True
        while curr1 is not None and curr2 is not None:
            if left:
                value = source1.remove(curr1._value)
                self.add(value)
                curr1 = curr1._next
            else:
                value = source2.remove(curr2._value)
                self.add(value)
                curr2 = curr2._next
            left = not left
        while curr1 is not None:
                value = source1.remove(curr1._value)
                self.add(value)
                curr1 = curr1._next
        while curr2 is not None:
                value = source2.remove(curr2._value)
                self.add(value)
                curr2 = curr2._next
        
        return 
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the set
        from first to last items.
        Use: for v in set:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the set (?)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next
