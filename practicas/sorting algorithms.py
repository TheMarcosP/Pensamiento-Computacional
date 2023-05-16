#%%

def bubbleSort(arr):
	n = len(arr)

	for i in range(n-1):
		for j in range(n-i-1):
                        
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr

arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)


# %%

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# make random list 10 elements long
import random 
list = [random.randint(0, 100) for i in range(10)]
# sort de list using merge sort and print it
merge_sort(list)
print(list)
# %%

def selection_sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
# %%


def insertion_sort(arr):
    for current_index in range(1, len(arr)):
        current_value = arr[current_index]
        compare_index = current_index - 1
        
        while compare_index >= 0 and current_value < arr[compare_index]:
            arr[compare_index + 1] = arr[compare_index] # Muevo los elementos mayores hacia la derecha
            compare_index -= 1
        
        # Inserta el elemento en su posición adecuada
        arr[compare_index + 1] = current_value
    
    return arr


import random
list = [random.randint(0, 100) for i in range(10)]
# sort de list using merge sort and print it
insertion_sort(list)
print(list)


# %%

