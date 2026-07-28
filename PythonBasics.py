"""
Python Basics - Assignment
Pwskills
"""

# ---------------------------------------------------------------------------
# Question 1: What is Python and why is it widely used in Data Analytics?
# Mention any three reasons.
# ---------------------------------------------------------------------------
"""
Python is a high-level, interpreted, general-purpose programming language
known for its simple, readable syntax.

Three reasons it's widely used in Data Analytics:
1. Rich libraries - Pandas, NumPy, Matplotlib, and Seaborn make data
   manipulation, analysis, and visualization easy.
2. Easy to learn and read - Simple syntax lets analysts focus on logic
   rather than complex code structure.
3. Strong community and integration - Works well with SQL, big data tools
   (Spark), and machine learning frameworks (Scikit-learn, TensorFlow).
"""


# ---------------------------------------------------------------------------
# Question 2: Explain the difference between List and Tuple in Python.
# ---------------------------------------------------------------------------
"""
List: mutable (can be changed), defined with [ ], generally slower.
Tuple: immutable (cannot be changed), defined with ( ), generally faster.
"""

my_list = [1, 2, 3]
my_list[0] = 10          # Allowed - lists are mutable
print("Question 2 - List:", my_list)

my_tuple = (1, 2, 3)
# my_tuple[0] = 10       # Not allowed - would raise a TypeError
print("Question 2 - Tuple:", my_tuple)


# ---------------------------------------------------------------------------
# Question 3: What is a function in Python? Why are functions useful?
# ---------------------------------------------------------------------------
"""
A function is a reusable block of code that performs a specific task,
defined using the 'def' keyword.

Functions are useful because they:
- Avoid code repetition (write once, use many times)
- Make code more organized and readable
- Make debugging and testing easier
- Allow modular programming
"""

def greet():
    print("Hello, welcome!")

greet()


# ---------------------------------------------------------------------------
# Question 4: Write a Python program to take a user's name as input and
# print a greeting message.
# ---------------------------------------------------------------------------
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome!")


# ---------------------------------------------------------------------------
# Question 5: Write a Python program to check whether a number is even or
# odd using conditional statements.
# ---------------------------------------------------------------------------
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# ---------------------------------------------------------------------------
# Question 6: Write a program to print numbers from 1 to 10 using a loop.
# ---------------------------------------------------------------------------
for i in range(1, 11):
    print(i)


# ---------------------------------------------------------------------------
# Question 7: Create a list of five numbers and print the maximum number
# from the list.
# ---------------------------------------------------------------------------
numbers = [12, 45, 7, 89, 34]
print("Maximum number is:", max(numbers))


# ---------------------------------------------------------------------------
# Question 8: Write a Python program to remove duplicate values from a
# list using a set.
# ---------------------------------------------------------------------------
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers_with_duplicates))
print("List after removing duplicates:", unique_numbers)


# ---------------------------------------------------------------------------
# Question 9: Write a function that returns the square of a number.
# ---------------------------------------------------------------------------
def square(n):
    return n * n

result = square(5)
print("Square is:", result)


# ---------------------------------------------------------------------------
# Question 10: Write a Python program to count how many times a number
# appears in a list.
# Example List: [2,3,4,2,5,2]
# ---------------------------------------------------------------------------
example_list = [2, 3, 4, 2, 5, 2]
target = 2

# Method 1: using built-in count()
count_builtin = example_list.count(target)
print(f"{target} appears {count_builtin} times in the list (using count())")

# Method 2: using a loop (without built-in count())
count_loop = 0
for value in example_list:
    if value == target:
        count_loop += 1

print(f"{target} appears {count_loop} times in the list (using a loop)")