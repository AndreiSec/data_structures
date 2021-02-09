"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   seca2560@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-10"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name = input("Name: ")
    origin = int(input("Origin: {}".format(Food.ORIGIN)))
    is_vegetarian = input("Vegetarian (Y/N): ")
    calories = int(input("Calories: "))
    if is_vegetarian == "Y":
        is_vegetarian = True
    else:
        is_vegetarian = False
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    linelist = line.split("|")
    #print(linelist)
    name = str(linelist[0])
    origin = int(linelist[1])
    is_vegetarian = str(linelist[2])
    if is_vegetarian == "True":
        is_vegetarian = True
    else:
        is_vegetarian = False
    calories = int(linelist[3])
    food = Food(name, origin, is_vegetarian, calories)
    return food

#print(read_food('Lasagna|7|False|135'))

def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_food(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - a file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    foodstr = str(file_variable.readline())
    food = read_food(foodstr)
    foods.append(food)
    while foodstr != "":
        food = read_food(foodstr)
        #print(food)
        foodstr = file_variable.readline()
        foods.append(food)
    del foods[0]

    return foods
# f = open("foods.txt", "r")
# foods = read_foods(f)
# for i in range(len(foods)):
#     print(foods[i])

def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(foods)):
        food = foods[i]
        #foodtoappend = str(foods[i])
        foodstr = "{}|{}|{}|{}\n".format(food.name, food.origin, food.is_vegetarian, food.calories)
        file_variable.write(foodstr)
    

    return
# new_foods = open("new_foods.txt", "w")
# foods = read_foods(f)
# write_foods(new_foods, foods)

def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []
    for i in range(len(foods)):
        food = foods[i]
        if food.is_vegetarian == True:
            veggies.append(food)
            

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = []
    for i in range(len(foods)):
        food = foods[i]
        if food.origin == origin:
            origins.append(food)
            


    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    summ = 0
    #avg = 0
    for i in range(len(foods)):
        food = foods[i]
        summ += food.calories
    avg = summ // len(foods)

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    summ = 0
    number = 0
    for i in range(len(foods)):
        food = foods[i]
        if food.origin == origin:
            summ += food.calories
            number += 1
    avg = summ // number

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    print("""Food                                Origin       Vegetarian Calories
----------------------------------- ------------ ---------- --------""")
    length = len("----------------------------------- ------------ ---------- --------")
    for i in range(len(foods)):
        food = foods[i]
        if food.is_vegetarian == True:
            truthvalue = "True"
        else:
            truthvalue = "False"
        origin = Food.ORIGIN[food.origin]
        print("{}".format(food.name),end="")
        print(" "* ((length - len(food.name))-33),"{}".format(origin),end="")
        print(" "* (length - len(truthvalue)- len(str(origin))-46),"{:^0}".format(truthvalue), end = "")
        print(" "* (length - len(str(food.calories)) - 60), "{}".format(food.calories))
        #print(" "* (length - len(str(food.calories)) - 56,"{:^0}".format(food.calories)
        #print(" "* ((length - len(food.name))-33),"{}".format(origin),end="")
        #print("""{} {:->14} {} {}""".format(food.name, food.origin, truthvalue, food.calories))
    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result = []
    veget_list = []
    veget_list.append(is_veg)
    origin_list = []
    origin_list.append(origin)
    if origin == -1:
        #print("O")
        origin_list.extend(list(range(30)))
    if max_cals == 0:
        max_cals = 10000000000
    if is_veg == False:
        veget_list.append(True)
        veget_list.append(False)
    for i in range(len(foods)):
        food = foods[i]
        if food.origin in origin_list and food.calories <= max_cals and food.is_vegetarian in veget_list:
            result.append(food)
    
    return result

# fv = open("foods.txt", "r")
# foods = read_foods(fv)
# origin = -1
# max_cals = 200
# is_veg = False
# results = food_search(foods,origin,max_cals,is_veg)
# for food in results:
#     print(food)