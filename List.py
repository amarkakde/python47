# List Exercises

# 1.Write a Python program to sum all the items in a list.

def sum_of_all_elements_in_the_list(List: list[int]) -> int:
    if isinstance(List, list) and all(isinstance(item, int) for item in List):
        sum = 0

        for item in List:
            sum += item
        return sum
    else:
        raise ValueError('Input must be list of integer')

def sum_of_all_elements_in_the_list2(List):
    try:
        sum = 0

        for item in List:
            sum += item
    except TypeError:
        print(TypeError)
    else:
        return sum