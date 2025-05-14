""" Write a function called filter_even_numbers that takes a list of integers 
and returns a new list containing only the even numbers. """
def filter_even_numbers(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))           # Output: []





print("\n")
""" Write a function called merge_sorted_lists that takes two sorted lists and 
returns a new sorted list containing all elements from both lists. """
def merge_sorted_lists(list1, list2):
    SortedList = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            SortedList.append(list1[i])
            i += 1
        else:
            SortedList.append(list2[j])
            j += 1

    while i < len(list1):
        SortedList.append(list1[i])
        i += 1

    while j < len(list2):
        SortedList.append(list2[j])
        j += 1

    return SortedList

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  #Output: [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  #Output: [1, 2, 3, 4, 5, 6]





print("\n")
""" Write a function called generate_matrix that takes dimensions n and m, and returns an n×m matrix 
where each element at position (i,j) is calculated as i*j. """
def generate_matrix(n, m):
    matrix = [[i * j for j in range(m)] for i in range(n)]
    return '\n'.join(str(row) for row in matrix)

print(generate_matrix(3, 3))
# Output:
# [0, 0, 0]
# [0, 1, 2]
# [0, 2, 4]






print("\n")
""" Write a function called transpose_matrix that takes a matrix (list of lists) and returns its 
transpose (rows become columns and vice versa). """
def transpose_matrix(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    return '\n'.join(str(row) for row in transposed)


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))
# Output:
#   [1, 4]
#   [2, 5]
#   [3, 6]





print("\n")
""" Write a function called find_peaks that takes a list of numbers and returns the indices of 
all "peaks" (elements that are greater than both of their neighbors). """
def find_peaks(numbers):
    peaks = []
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            peaks.append(i)
    return peaks

print(find_peaks([1, 3, 2, 3, 5, 4, 3, 2, 3, 1]))  # Output: [1, 4, 8]






print("\n")
""" Implement a function called rotate_list that rotates a list to the right by k steps, without 
using built-in functions like slice assignment. """
def rotate_list(numbers, k):
    n = len(numbers)
    k = k % n  
    result = [0] * n

    for i in range(n):
        new_index = (i + k) % n
        result[new_index] = numbers[i]

    return result

print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3], 4))        # Output: [3, 1, 2]
