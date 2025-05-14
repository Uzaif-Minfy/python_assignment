""" Write a function called calculate_average that takes
a list of numbers as input and returns their average. 
If the list is empty, it should return 0."""
def calculate_average(Numbers):
    if not Numbers:
        return 0
    else:
        return sum(Numbers)/len(Numbers)
    
print(calculate_average([5, 10, 15, 20]))  # Output: 12.5
print(calculate_average([]))  # Output: 0




print("\n")
"""" Write a function called greet_user that takes a name and a greeting message. 
The greeting message should default to "Hello" if not provided."""
def greet_user(name, greetingMsg="Hello" ):
    return f"{greetingMsg}, {name}!"

print(greet_user("Alice"))  # Output: Hello, Alice!
print(greet_user("Bob", "Hi"))  # Output: Hi, Bob!




print("\n")
"""Create a function called calculate_total that calculates the total cost of items with
 a variable number of prices and an optional discount percentage. """
def calculate_total(*prices, discount=0):
    amount = sum(prices)
    total = amount - amount * (discount / 100)
    return int(total)

print(calculate_total(10, 20, 30))  # Output: 60
print(calculate_total(10, 20, 30, discount=10))  # Output: 54 




print("\n")
""" Create a function called create_multiplier that takes a number and returns a function 
that multiplies any input by that number. """
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15




print("\n")
""" Implement a recursive function called power that calculates x^n (x raised to the power of n) 
without using the built-in power operator or function. Your function should have O(log n) time complexity. """
def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)

    half = power(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half

print(power(2, 10))  # Output: 1024
print(power(3, 4))   # Output: 81
