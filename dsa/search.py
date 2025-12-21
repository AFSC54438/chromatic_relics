from random import randint
from cs50 import get_int


# ------------------------------------------------------------------------
# Linear Search
def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True


# ------------------------------------------------------------------------
# Recursive Binary Search
def recursive_binary_search(arr, target):
    arr_len = len(arr)

    if arr_len == 0:
        return False

    mid_index = arr_len // 2
    mid = arr[mid_index]

    if mid == target:
        return True

    elif mid < target:
        return recursive_binary_search(arr[mid_index + 1 :], target)
    else:
        return recursive_binary_search(arr[:mid_index], target)


# ------------------------------------------------------------------------
# Iterative Binary Search
def iterative_binary_search(arr, target):
    low_bound = 0
    up_bound = len(arr) - 1

    while low_bound <= up_bound:
        mid_index = (low_bound + up_bound) // 2
        mid = arr[mid_index]

        if mid == target:
            return True
        elif mid < target:
            low_bound = mid_index + 1
        else:
            up_bound = mid_index - 1

    return False


# ------------------------------------------------------------------------
# Testing
my_list = []

# Populating array
while len(my_list) < 10:
    num = randint(-50, 50)
    if num not in my_list:
        my_list.append(num)

my_list = sorted(my_list)

print(f"List: {my_list}")

# Selecting a search target
this_target = get_int("Choose a target to search: ")

if iterative_binary_search(
    my_list, this_target
):  # <--- choose which search algo you wanna use
    print(f"Target {this_target} found")
else:
    print(f"Target {this_target} NOT found")
