"""
-------------------------------------------------------
[Set ADT - midterm practice]
-------------------------------------------------------
Author: redacted
ID: redacted
Email: redacted@mylaurier.ca
__updated__ = "2021-03-01"
-------------------------------------------------------
"""

from copy import deepcopy

class Set:
    """
    --------------------------------------------------------
    Data structure that contains a set of unique values,
        i.e no values are repeated in a Set.
    Values stored in a fixed-lenth Python list like in the Circular Queue.
        Do not use Python list methods that change the length of the list:
        append, insert, remove, pop, extend
    Empty slots contain None.
    --------------------------------------------------------
    Examples of Set attributes:
        _values = [None, None, None, None], _max_size = 4, _count = 0, _next = 0
        _values = [1, 4, 9, 3],             _max_size = 4, _count = 4, _next = None
        _values = [1, None, 9, 3],          _max_size = 4, _count = 3, _next = 1
        _values = [1, None, 9, None],       _max_size = 4, _count = 2, _next = 1
    --------------------------------------------------------
    """
    #default maximum size when max_size parameter is not provided
    DEFAULT_SIZE = 10

    def __init__(self, _max_size = DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty Set.
        Use: s = Set()
        -------------------------------------------------------
        Returns:
            Initializes an empty set.
        -------------------------------------------------------
        """
        #maximum size of python list to store data
        self._max_size = _max_size
        #python list that stores data - initialized to list of None
        self._values = [None] * self._max_size 
        #first availiable index for adding values - if None, Set if full
        self._next = 0
        #number of unique values in set, cannot exceed _max_size
        self._count = 0

        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the set is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the set is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the set.
        Use: n = len(s)
        -------------------------------------------------------
        Returns:
            the number of values in the set.
        -------------------------------------------------------
        """
        return len(self._values)

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the set.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the set, -1 if key is not found (int)
        -------------------------------------------------------
        """
        # your code here
        if self._count > 0:
            i = 0
            n = len(self._values)
            
            while i < n and self._values[i] != key:
                i += 1
            
            if i == n and self._values[i-1] != key:
                i = -1
        else:
            i = -1

        return i

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the set.
        Use: b = s.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            inserted - True if the value was inserted at i, False otherwise.
                value is inserted at position i or appended to the end of the set
                if i > len(s) only if value is unique in the set (boolean)
        -------------------------------------------------------
        """
        # your code here
        inserted = False 
        
        location = self._linear_search(value)
            
        if location == -1:
            self._values[i] = value
            inserted = True
            self._count += 1
            
        return inserted

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the set that matches key.
        Use: value = s.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        i = self._linear_search(key)
        if i != -1:
            value = self._values[i]
            
            self._values[i] = None
            
            self._count -= 1
            
        else:
            value = None

        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in the set that matches key.
        Use: value = s.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find in an empty set"
        # your code here
        i = self._linear_search(key)
        
        value = self._values[i]

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the set (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty set"
        # your code here
        value  = deepcopy(self._values[0])

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in the set.
        Use: n = s.index( key )
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the full value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        # your code here
        
        i = self._linear_search(key)

        return i


    def _valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(set) to len(set) - 1
        Use: assert self._valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = len(self._values)
        
        return -n <= i < n
    
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns:
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
    
    