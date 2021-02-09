"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2020-01-16"
-------------------------------------------------------
"""
from copy import deepcopy

class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _List_Node(value, self._front)
        self._front = new_node
        self._count += 1
        if self._count == 1:
            self._rear = self._front
        
        
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        
        new_node = _List_Node(value, None)
        
        if self._count == 0:
            self._front = new_node
            self._rear = new_node
            self._count += 1
        else:
            
            self._rear._next = new_node
            self._rear = new_node
            self._count += 1
        
        
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if i < -self._count or i == 0:
            self.prepend(value)
        elif i > self._count - 1:
            self.append(value)
        else:
            curcount = 0
            curnode = self._front
            if i < 0:
                i = self._count + i
            while curcount != i-1:
                curnode = curnode._next
                curcount += 1
            secnode = curnode._next
            curnode._next = _List_Node(value, secnode)
            self._count += 1
        
        
        
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        if self._count == 0:
            previous = None
            current = None
            index = -1
        elif self._count == 1:
            previous = None
            if self._front._value == key:
                current = self._front
                index = 0
        else:
            current = self._front
            previous = None
            index = 0
            while current is not None and current._value != key:
                if current._value != key:
                    previous = current
                    current = current._next
                    index += 1
            if current is not None:
                if current._value == key:
                    current = current
            else:
                current = None
                index = -1
        
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        
        previous, current, index = self._linear_search(key)
        
        if index != -1:
            if index == 0:
                value = deepcopy(current._value)
                self._front = current._next
                self._count -= 1
                current = None
            elif index == self._count - 1:
                value = deepcopy(current._value)
                self._rear = previous
                self._rear._next = None
                self._count -= 1
                
                current = None
            else:
                previous._next = current._next
                value = deepcopy(current._value)
                self._count -= 1
                current = None
        else:
            value = None
        if self._count == 0:
            self._front = None
            self._rear = None
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        current = self._front
        value = deepcopy(current._value)
        self._front = current._next
        self._count -= 1
        current = None
        if self._count == 0:
            self._rear = None
        
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        count = self.count(key)
        if count > 0:
            removed = 0
            while removed <= count:
                self.remove(key)
                removed += 1
        
        
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        if self._count == 0:
            value = None
        else:
            previous, current, index = self._linear_search(key)
            if current != None:
                value = current._value
        
        return deepcopy(value)

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        
        
        
        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        
        previous, current, index = self._linear_search(key)
        
        if index == None:
            index = -1
        
        
        return deepcopy(index)

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        value = None
        index = 0
        current = self._front
        
        if i < 0:
            i = self._count + i
        while index != i + 1:
            value = current._value
            current = current._next
            index += 1
            
        
        return deepcopy(value)

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        index = 0
        current = self._front
        if i < 0:
            i = self._count + i
        while index != i:
            current = current._next
            index += 1
        if current != None:
            existing_value = deepcopy(current._value)
            current._value = deepcopy(value)
        
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)
        
        return current != None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        curmax = current._value
        index = 1
        if self._count != 0:
            while index != self._count + 1:
                if index == self._count:
                    index += 1
                else:
                    index += 1
                    if curmax < current._next._value:
                        curmax = current._next._value
                    current = current._next
        
        return deepcopy(curmax)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        curmin = current._value
        index = 1
        if self._count != 0:
            while index != self._count + 1:
                if index == self._count:
                    index += 1
                else:
                    index += 1
                    if curmin > current._next._value:
                        curmin = current._next._value
                    current = current._next
        
        return deepcopy(curmin)

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        index = 1
        number = 0
        if self._count != 0:
            current = self._front
            while index != self._count + 1:
                if index == self._count:
                    index += 1
                    if current._value == key:
                        number += 1
                else:
                    index += 1
                    if current._value == key:
                        number += 1
                    current = current._next
            
        
        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._rear = self._front
        previous = None
        current = self._front

        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp

        self._front = previous
        
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._rear = self._front
        previous = None
        current = self._front
        self, current, previous = self.reverse_r_aux(current, previous)
        
        self._front = previous
        
        return
    
    
    def reverse_r_aux(self, current, previous):
        
        if current is not None:
            temp = current._next
            current._next = previous
            self, current, previous = self.reverse_r_aux(temp, current)
        return self, current, previous

    
    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        if self._count > 0:
            current = second = self._front
            while current is not None:
                while second._next is not None:   
                    if second._next._value == current._value:
                        second._next = second._next._next   # cut second.next out of the list
                    else:
                        second = second._next   # put this line in an else, to avoid skipping items
                current = second = current._next
            self._count = 0
            current = self._front
            while current is not None:
                self._count += 1
                current = current._next
#             index1 = 0
#             index2 = 0
#             current1 = self._front
#             while index1 != self._count + 1:
#                 data = current1._value
#                 current2 = current1._next
#                 while index2 != self._count + 1:
#                     if current2._value == data:
#                         self.remove(current2)
#                     current2 = current2._next
#                     index2 += 1
#                 current1 = current1._next
#                 index1 += 1
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return


    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (iterative version)
        Use: b = lst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
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
    
    
    def identical_r_aux(self, current1, current2):
        """
        Private helper for identical_r
        """
        identical = True
        if current1 == None and current2 == None:
            identical = True
        else:
            if current1 == current2:
                identical = self.identical_r_aux(current1._next, current2._next)
        return identical
    
    
    def is_identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count == other._count:
            current1 = self._front
            current2 = other._front
            identical = self.identical_r_aux(current1, current2)
        else:
            identical = False
        
        
        return identical

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        if self._count > 0:
#             current = self._front
#             halflist = (self._count // 2)
#             if self._count % 2 == 0:
#                 halflist -=1
#             index = 0
#             while index != halflist:
#                 target1.append(self.remove_front())
#                 index += 1
#             while current is not None:
#                 target2.append(self.remove_front())
            
            l1 = []
            current = self._front
            while current is not None:
                l1.append(deepcopy(current._value))
                current = current._next
             
            
             
            halflist = (len(l1) // 2) 
            if len(l1) % 2 == 0:
                    halflist -= 1
            l2 = l1[:halflist+1]
            l3 = l1[halflist+1:]
            for x in l2:
                target1.append(deepcopy(x))
            for y in l3:
                target2.append(deepcopy(y))
        self._count = 0
        self._front = None
        self._rear = None
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        if self._count > 0:
              
            l1 = []
            current = self._front
            while current is not None:
                l1.append(deepcopy(current._value))
                current = current._next
             
            l2 = []
            l3 = []
             
            while len(l1) != 0:
                l2.append(deepcopy(l1[0]))
                del l1[0]
                if len(l1) != 0:
                    l3.append(deepcopy(l1[0]))
                    del l1[0]
            for x in l2:
                target1.append(deepcopy(x))
            for y in l3:
                target2.append(deepcopy(y))
        self._count = 0
        self._front = None
        self._rear = None
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        
        target1 = List()
        target2 = List()
        
        
        target1, target2 = self.split_alt_r_aux(target1, target2, self._front)
        self._count = 0
        self._front = None
        self._rear = None
        return target1, target2
    
    
    def split_alt_r_aux(self, target1, target2, current = None, oe = 0):
        
        ## oe is whether its odd or even
        if current is not None:
            if oe == 0:
                if target1._count == 0:
                        target1._front = current
                        target1._rear = current
                        target1._count += 1
                else:
            
                        target1._rear._next = current
                        target1._rear = current
                        target1._count += 1
                target1, target2 = self.split_alt_r_aux(target1, target2, current._next, 1)
            elif oe == 1:
                if target2._count == 0:
                        target2._front = current
                        target2._rear = current
                        target2._count += 1
                else:
            
                        target2._rear._next = current
                        target2._rear = current
                        target2._count += 1
                target1, target2 = self.split_alt_r_aux(target1, target2, current._next, 0)
        else:
            if target1._count > 1:
                target1._rear._next = None
            if target2._count > 1:
                target2._rear._next = None
        return target1, target2
    
    
    def _linear_search_r_aux(self, previous, current, index, key):
        """
        Auxiliary helper for recursive linear search
        """
        if current is None:
            current = None
            index = -1
        elif current._value == key:
            previous = previous
        else:
            previous, current, index = self._linear_search_r_aux(current, current._next, index+1, key)
        return previous, current, index
    
    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        index = 0
        
        previous, current, index = self._linear_search_r_aux(previous, current, index, key)
                
        
        
        
        
        
        return previous, current, index

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        current1 = source1._front
        current2 = source2._front
        l1 = []
        l2 = []
        
        while current1 is not None:
            l1.append(deepcopy(current1._value))
            current1 = current1._next
        while current2 is not None:
            l2.append(deepcopy(current2._value))
            current2 = current2._next
        
        l3 = []
        for i in l1:
            if i in l2 and i not in l3:
                l3.append(deepcopy(i))
        for x in l3:
            self.append(x)
        
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        
        if source1._count > 0 and source2._count > 0:
            self = self.intersection_r_aux(source1._front, source2)
        
        
        
        
        return
    
    
    def intersection_r_aux(self, current1, source2):
        if current1 is not None:
            _, current, _ = source2._linear_search_r(current1._value)
            if current is not None:
                _, curself, _ = self._linear_search_r(current._value)
                if curself is None:
                    curtoadd = deepcopy(current1)
                    curtoadd._next = None
                    if self._count == 0:
                            self._front = curtoadd
                            self._rear = curtoadd
                            self._count += 1
                    else:
                
                            self._rear._next = curtoadd
                            self._rear = curtoadd
                            self._count += 1
            self = self.intersection_r_aux(current1._next, source2)
        else:
            return self
        
        


    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        current1 = source1._front
        current2 = source2._front
        l1 = []
        l2 = []
        
        while current1 is not None:
            l1.append(deepcopy(current1._value))
            current1 = current1._next
        while current2 is not None:
            l2.append(deepcopy(current2._value))
            current2 = current2._next
        
        l3 = []
        for i in l1:
            if i not in l3:
                l3.append(deepcopy(i))
        for i in l2:
            if i not in l3:
                l3.append(deepcopy(i))
        for x in l3:
            self.append(x)
        
        
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        current1 = None
        current2 = None
        if source1 is not None and source1._count > 0:
            current1 = source1._front
        if source2 is not None and source2._count > 0:
            current2 = source2._front
        
        
        
        self = self.union_r_aux(current1)
        self = self.union_r_aux(current2)
        
        
        
        return


#     def union_r_aux(self, current):
#         if current is not None:
#             _, currentself, _ = self._linear_search_r(current._value)
#             if currentself is None:
#                 curtoadd = deepcopy(current)
#                 curtoadd._next = None
#                 if self._count == 0:
#                     self._front = curtoadd
#                     self._rear = curtoadd
#                     self._count += 1
#                 else:
#                     self._count += 1
#                     self._rear._next = curtoadd
#                     self._rear = curtoadd
#             return self.union_r_aux(current._next)
#         else:
#             return self
            
                





    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = lst.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        
        
        
        return deepcopy(self)

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        # your code here
        return

    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs List to the front
        of the current List. Private helper method.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the rs List and
            its count is updated. The rs List front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
#         while source1._count != 0 or source2._count != 0:
#             if source1._count == 0:
#                 while source2._count != 0:
#                     self.append(source2._front._value)
#                     source2.remove(source2._front._value)
#             elif source2._count == 0:
#                 while source1._count != 0:
#                     self.append(source1._front._value)
#                     source1.remove(source1._front._value)
#             else:
#                 self.append(source1._front._value)
#                 source1.remove(source1._front._value)
#                 self.append(source2._front._value)
#                 source2.remove(source2._front._value)
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

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next