#Chapter 4 Assignment

#4.1
def loop_over_list():
    """Loop over a list of fruits and print each one"""
    pcc_4_list = ['apple', 'banana', 'carrot', 'date']
    [print(list)for list in pcc_4_list]
    

#4.2
def loop_over_list_and_capitalize():
    """Loop over a list of fruits and print the index and the element capitalized
    Ex: 0: Apple
        1: Banana ..."""
    #Remember to use the variable name my_list
    my_list = ["apple", "banana", "carrot", "date"]
    for i, fruit in enumerate(my_list):
        print(F"{i}: {fruit.title()}")
loop_over_list_and_capitalize

#4.3
def print_numbers_1_to_10():
    """Print the numbers 1 to 10 using a for loop"""
    for i in range (1,11):
        print(i)

    
#4.4
def print_numbers_1_to_n():
    """Print the numbers 1 to n"""
    n = 15

    for i in range(1,n+1):
        print(i)

#4.5
def create_list_of_numbers(n: int) -> list:
    """Create a list of numbers from 1 to n
    return the list"""
    #Remember to use the variable name n
    lst = []
    for i in range(1,n+1):
        lst.append(i)
    return lst
    

#4.6
def create_list_of_even_numbers(n: int) -> list:
    """Create a list of even numbers from 1 to n
    return the list"""
    #Remember to use the variable name n
    return list(range(2,n+1,2))
    
#4.7
def create_list_of_first_ten_cube_numbers() -> list:
    """Create a list of the first ten square numbers
    return the list"""
    lst = []
    for i in range(1, 11):
        lst.append(i**3)

    return lst
    
#4.8
def create_list_comprehension_of_first_ten_cube_numbers() -> list:
    """Create a list of the first ten square numbers
    using list comprehension
    return the list"""
    return [i**3 for i in range(1,11)]
    
#4.9
def copy_list_and_append_11(my_list: list) -> list:
    """Copy the list and append the number 11 to the end
    return the new list
    Make sure not to modify the original list"""
    #Remember to use the variable name my_list
    
    copy_list = my_list[:]
    copy_list.append(11)

    return copy_list
    
#4.10
def return_first_index_of_tuple(my_tuple: tuple) -> int:
    """Return the first index of the tuple
    return the first index
    Remember that a tuple is like a list but immutable"""
    #Remember to use the variable name my_tuple
    return my_tuple[0]

        
    
#4.11
def loop_over_tuple():
    """Loop over the tuple and print each item"""
    #Remember to use the variable name my_tuple
    my_tuple = (1, 2, 3, 4, 5)
    for num in my_tuple:
        print(num)
    