# ZOE
# ENGEL
# CLASS 1

# Example
'''ages = [12, 34, 20, 21,31,54]
ages= list(map(lambda x: x + 2, ages))
print(ages)'''

# Exercise 1
# grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
# Task:
# Filter the grades to only display everyone above (and including) 70%

grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
passing_grade = list(filter(lambda x: x >= 70,grades))

print(passing_grade)

# Exercise 2
# dog_ages = [12, 8, 4, 1, 2, 6, 4, 4, 5]
# Task:
# Convert the ages into "dog years" (x7)

dog_ages = [12, 8, 4, 1, 2, 6, 4, 4, 5]
dog_ages = list(map(lambda x: x * 7, dog_ages))
print(dog_ages)

# Exercise 3
# transactions = [51.0, 49.99, 80.99, 67.99, 120.52, 23.4]
# Task:
# Convert the transactions to a single total

from functools import reduce
transactions = [51.0, 8, 4, 1, 2, 6, 4, 4, 5]
transactions = reduce(lambda a, b: a + b, transactions)
print(transactions)

