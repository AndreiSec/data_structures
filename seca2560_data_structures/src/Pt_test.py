"""
-------------------------------------------------------
Popularity Tree class.
-------------------------------------------------------
Author:  David Brown
ID:
Email:   dbrown@wlu.ca
__updated__ = "2018-07-27"
-------------------------------------------------------
Linked class version of the Popularity_Tree ADT.
-------------------------------------------------------
"""
from copy import deepcopy


class _PT_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a node containing value.
        Use: node = _PT_Node( value, priority )
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            Initializes an Popularity_Tree node containing value. Child
            pointers are None, rcount is 0.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        # New node is initially added at a leaf.
        self._count = 1  # Retrieval count
        self._left = None
        self._right = None
        self._height = 1
        return

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's (up to) two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return
    
    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)

class Popularity_Tree:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an is_empty Popularity_Tree.
        Use: pt = Popularity_Tree()
        -------------------------------------------------------
        Returns:
          Initializes an is_empty pt.
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if pt is is_empty.
        Use: b = pt.is_empty()
        -------------------------------------------------------
        Returns:
          Returns True if pt is is_empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of elements in the Popularity_Tree tree.
        Use: n = len( pt )
        -------------------------------------------------------
        Returns:
          Returns the number of values in the Popularity_Tree tree.
        -------------------------------------------------------
        """
        return self._count

    def height(self):
        return self._root._height

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            returns
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        self._root = self._insert_aux(self._root, value)
        return

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of _value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BSTNode)
            value - data to be inserted into the node (?)
        Returns:
            returns
            node - the current node (_BSTNode)
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            node = _PT_Node(value)
            self._count += 1
        elif node._value > value:
            node._left = self._insert_aux(node._left, value)

            if node._count < node._left._count:
                node = self._rotate_right(node)
            node._update_height()
        elif node._value < value:
            node._right = self._insert_aux(node._right, value)

            if node._count < node._right._count:
                node = self._rotate_left(node)
            node._update_height()
        else:
            node._count += 1
        return node

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            returns
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def _rotate_left(self, node):
        """
        -------------------------------------------------------
        Rotates the pivot to its left around its right child.
        Updates the heights of the rotated nodes.
        Private recursive operation called on rebalancing.
        Use: node = self._rotate_left(node)
        -------------------------------------------------------
        Parameters:
            node - the pivot node to rotate around (_PT_Node)
        Returns:
            node - the node that replaces the pivot node (_PT_Node)
        -------------------------------------------------------
        """
        temp = node._right
        node._right = temp._left
        temp._left = node
        node._update_height()
        return temp

    def _rotate_right(self, node):
        """
        -------------------------------------------------------
        Rotates the pivot to its right around its left child.
        Updates the heights of the rotated nodes.
        Private recursive operation called on rebalancing.
        Use: node = self._rotate_right(node)
        -------------------------------------------------------
        Parameters:
            node - the pivot node to rotate around (_PT_Node)
        Returns:
            node - the node that replaces the pivot node (_PT_Node)
        -------------------------------------------------------
        """
        temp = node._left
        node._left = temp._right
        temp._right = node
        node._update_height()
        return temp

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Popularity_Tree contains key.
        Use: b = key in pt
        -------------------------------------------------------
        Parameters:
          key - a comparable data element (?)
        Returns:
          Returns True if pt contains key, False otherwise.
        -------------------------------------------------------
        """
        value = self.retrieve(key)
        return value is not None

    def inorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in inorder order.
        -------------------------------------------------------
        Returns:
          The contents of the tree are printed inorder.
        -------------------------------------------------------
        """
        self._inorder_aux(self._root)
        return

    def _inorder_aux(self, node):
        """
        ---------------------------------------------------------
        Traverses node subtree in inorder.
        ---------------------------------------------------------
        Parameters:
          node - a tree node (_PT_Node)
        Returns:
          Returns the the total number of nodes in the tree.
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left)
            print(node._value)
            self._inorder_aux(node._right)
        return

    def postorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in postorder order.
        -------------------------------------------------------
        Returns:
          The contents of the tree are printed postorder.
        -------------------------------------------------------
        """
        self._postorder_aux(self._root)
        return

    def _postorder_aux(self, node):
        """
        ---------------------------------------------------------
        Traverses node subtree in postorder.
        ---------------------------------------------------------
        Parameters:
          node - a tree node (_PT_Node)
        Returns:
          Returns the the total number of nodes in the tree.
        ---------------------------------------------------------
        """
        if node is not None:
            self._postorder_aux(node._left)
            self._postorder_aux(node._right)
            print(node._value)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in preorder order.
        -------------------------------------------------------
        Returns:
          The contents of the tree are printed preorder.
        -------------------------------------------------------
        """
        self._preorder_aux(self._root)
        return

    def _preorder_aux(self, node):
        """
        ---------------------------------------------------------
        Traverses node subtree in preorder.
        ---------------------------------------------------------
        Parameters:
          node - a tree node (_PT_Node)
        Returns:
          Returns the the total number of nodes in the tree.
        ---------------------------------------------------------
        """
        if node is not None:
            #            print(node._value)
            print(node)
            self._preorder_aux(node._left)
            self._preorder_aux(node._right)
        return

    def levelorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in levelorder order.
        Use: avl.levelorder()
        -------------------------------------------------------
        Returns:
          The contents of the tree are printed levelorder.
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a list.
            this_level = list()
            this_level.append(self._root)

            while this_level != []:
                # Create a list for the children of this node.
                next_level = list()

                for node in this_level:
                    print(node._value, end=',')

                    if node._left is not None:
                        next_level.append(node._left)
                    if node._right is not None:
                        next_level.append(node._right)
                print()
                # Process the next level.
                this_level = next_level
        return

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if pt is valid.
        Use: b = pt.is_valid()
        ---------------------------------------------------------
        Returns:
            returns:
            valid - True if the tree is a Popularity_Tree, False otherwise.
        ---------------------------------------------------------
        """
        valid = self._is_valid_aux(self._root)
        return valid

    def _is_valid_aux(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the Popularity_Tree validity of node.
        Private operation called only by is_valid.
        Use: b = self._is_valid_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to check the validity of (_PT_Node)
        Returns:
            returns:
            result - True if node is a Popularity_Tree, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if node is None:
            result = True
        elif (node._left is not None and node._left._count > node._count) \
                or (node._right is not None and node._right._count > node._count):
            print("Popularity Violation at: {}".format(node._value))
            result = False
        elif (node._left is not None and node._left._value > node._value) \
                or (node._right is not None and node._right._value < node._value):
            print("Binary Tree Violation at {}".format(node._value))
            result = False
        else:
            result = self._is_valid_aux(node._left) and \
                self._is_valid_aux(node._right)
        return result

    def traverse(self):
        """
        ---------------------------------------------------------
        Returns the contents of pt in an array in sorted order
        by value.
        Use: a = pt.traverse()
        ---------------------------------------------------------
        Returns:
          Returns:
          a - an array containing the contents of pt in sorted order.
        ---------------------------------------------------------
        """
        a = []
        self._traverse_aux(self._root, a)
        return a

    def _traverse_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverse the node's subtree in preorder, adding the contents of
        each node to an array.
        Private recursive operation called only by traverse.
        Use: self._traverse_aux(node, a)
        ---------------------------------------------------------
        Returns:
          returns:
          a contains the contents of node and its children in sorted order.
        ---------------------------------------------------------
        """
        if node is not None:
            self._traverse_aux(node._left, a)
            a.append((node._count, node._value))
            self._traverse_aux(node._right, a)
        return


# SEP = "-" * 60
# pt = Popularity_Tree()
# letters = "abcdefghijklmnopqrstuvwxyz"
#
# for letter in letters:
#     pt.insert(letter)
#
# fp = open('otoos610.txt', 'r', encoding='utf-8')
#
# for line in fp:
#     for c in line:
#         if c.isalpha():
#             pt.insert(c.lower())
# fp.close()
#
# pt.levelorder()
# print()
# print(SEP)
