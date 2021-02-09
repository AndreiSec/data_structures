"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   seca2560@mylaurier.ca
__updated__ = "2020-03-17"
-------------------------------------------------------
"""
# from Food import Food
# from Food_utilities import read_foods
# fv = open("foods.txt", "r")

# foods = read_foods(fv)

# def hash_table(objects):
#     """
#     Prints out a table of values with hashes, slot and key.
#     """
#     a = 0
#     print("""Hashes
# Hash     Slot Key
# ======== ==== ====================""")
#     length = len("======== ==== ====================")
#     for i in objects:
#         h = hash(i)
#         slot = h % 7
#         print(" " * (length-len(str(h))-27), "{}".format(h), end="")
#         print(" "* (length - len(str(slot))-30), "{}".format(slot),end='')
#         print(" "*-1, "{}, {}".format(i.name, i.origin))



def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Use:
        hash_table(slots, values)
    Returns:
       None
    -------------------------------------------------------
    """
    print("{:8} {:4} {}".format("Hash", "Slot", "Key"))
    print("{} {} {}".format("-" * 8, "-" * 4, "-" * 20))

    for value in values:
        x = hash(value)
        y = x % slots
        print("{:8d} {:4d} {}".format(x, y, value.key()))
    return


# hash_table(foods)