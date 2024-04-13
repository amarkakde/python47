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
    
def sum_of_all_elements_in_the_list3(List):
    try:
        sum = sum(List)
    except TypeError:
        print(TypeError)
    else:
        return sum


# 2. Write a Python program to multiply all the items in a list.

def multiply_all_item_in_list(List, multiplyer) -> list:
    return list(map(lambda x: x * multiplyer, List ))

def multiply_all_item_in_list2(List, multiplyer) -> list:
    newlist = []

    for item in List:
        newlist.append(item * multiplyer)

    return newlist


# 3. Write a Python program to find the largest number in a list.

def find_larget_element_from_list(List) -> int:
    return max(List)

def find_larget_element_from_list2(List):
    if List:
        largest_element = List[0]

        for item in List:
            if largest_element < item:
                largest_element = item
        return largest_element
    else:
        return None