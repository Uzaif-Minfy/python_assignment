""" Write a function called swap_pairs that swaps adjacent elements in a tuple. If the tuple has an odd length, 
the last element should remain in place. """
def swap_pairs(numbers):
    result = []
    for i in range(0, len(numbers) - 1, 2):
        result.extend([numbers[i + 1], numbers[i]])
    if len(numbers) % 2 == 1:
        result.append(numbers[-1])
    return tuple(result)

print(swap_pairs((1, 2, 3, 4)))  # Output: (2, 1, 4, 3)
print(swap_pairs((1, 2, 3)))     # Output: (2, 1, 3)





print("\n")
""" Write a function called get_stats that takes a list of numbers and returns a tuple containing the minimum, maximum,
sum, and average of the numbers. """
def get_stats(numbers):
    """Return min, max, and average of a list of numbers."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)
print(get_stats([1, 2, 3, 4, 5]))  # Output: (1, 5, 15, 3.0)





print("\n")
""" Create a function called count_coordinate_occurrences that takes a list of (x, y) coordinate tuples and returns a 
dictionary mapping each coordinate to the number of times it appears in the list. """
def count_coordinate_occurrences(coords):
    result = {}
    for i in coords:
        result[i] = result.get(i, 0) + 1
    return result

coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))
# Output: {(1, 2): 3, (3, 4): 2, (5, 6): 1}





print("\n")
""" Create a named tuple called Student with fields for name, age, and grades (which should be a tuple of numbers). Then 
write a function called top_student that takes a list of Student tuples and returns the Student with the highest average grade. """
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grades"])

def average(student):
    return sum(student.grades) / len(student.grades)

def top_student(students):
    return max(students, key=average)

alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))
# Output: Student(name='Charlie', age=21, grades=(90, 92, 93))
