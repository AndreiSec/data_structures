"""
-------------------------------------------------------
Utilities
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   seca2560@mylaurier.ca
__updated__ = "2020-01-14"
-------------------------------------------------------
"""
from Stack_array import Stack
from List_array import List
from Food import Food
# from Food_utilities import read_foods
from copy import deepcopy

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    #assert (source == []) == True, "Source is empty"
    while source != []:
        #value = deepcopy(source.pop())
        stack.push(deepcopy(source.pop()))
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(stack) != 0:
        #value = deepcopy(stack.pop())
        #target.append(value)
        #print(value)
        target.insert(0, deepcopy(stack.pop()))
    return

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    s.is_empty()
    s.push(source)
    s.is_empty()
    s.peek()
    s.is_empty()
    s.push(s.pop())
    return
    
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        #value = deepcopy(source.pop())
        queue.insert(deepcopy(source.pop(0)))
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while queue.is_empty() == False:
        #value = deepcopy(source.pop())
        target.append(queue.remove())
    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        #value = deepcopy(source.pop())
        pq.insert(deepcopy(source.pop(0)))
    return



def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while pq.is_empty() == False:
        #value = deepcopy(source.pop())
        target.append(pq.remove())
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    
    q.is_empty()
#     q.insert(a)
    array_to_queue(q,a)
    q.is_empty()
    q.peek()
    q.remove(a)
    q.is_empty()
    q.peek()
    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    pq.is_empty()
    pq.insert(a)
    pq.is_empty()
    pq.peek()
    pq.remove(a)
    pq.is_empty()
    pq.peek()

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contents of source to list. At finish, source is empty.
    Last element in source is at rear of list,
    first element in source is at front of list.
    Use: array_to_list(list, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    if len(source) != 0:
        for i in range(len(source)):
            llist.append(deepcopy(source.pop(0)))
    
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    if len(llist) != 0:
        for i in range(len(llist)):
            target.append(deepcopy(llist.pop(0)))
    
    return

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    print(lst.is_empty())
    print(lst.insert(0, source[0]))
    print(lst.remove(source[0]))
    print(lst.count(source[0]))
    print(lst.append(0))
    print(lst.index(0))
    print(lst.find(0))
    print(lst.max())
    print(lst.min())
    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    return

# fv = open('foods.txt', "r")
# foods = read_foods(fv)
# food_list = []
# stack_to_array(foods, food_list)
# list_test(food_list)