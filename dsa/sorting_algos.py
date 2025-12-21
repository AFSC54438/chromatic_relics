from random import randint 

# --------------------------------------------------------
# Bubble Sort
def bubble_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len):
        swapped = False
        for j in range(arr_len - i- 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if swapped == False:
            break
    
# --------------------------------------------------------
# Insertion Sort
def insertion_sort(arr):
    arr_len = len(arr)

    for i in range(1, arr_len):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# --------------------------------------------------------
# Testing
my_list = []

# Populating list
while len(my_list) < 10:
    num = randint(-50, 50)
    if num not in my_list:
        my_list.append(num)

print(f"Before sorted: {my_list}")
bubble_sort(my_list) # <-- choose which sorting algo to use
print(f"After sorted: {my_list}")
