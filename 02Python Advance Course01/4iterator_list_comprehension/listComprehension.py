# You can either use loops:
squares = []

for x in range(10):
    squares.append(x ** 2)

print (squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Or you can use list comprehensions to get the same result:
squares = [x**2 for x in range(10)]

list1 = [3, 4, 5]

multiplied = [item * 3 for item in list1]

print (multiplied)
[9, 12, 15]

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print (numbers)
['1', '2', '3', '4', '5']

# List comprehensions also make it easy to work with
# multidimensional lists
multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print([col[1] for col in multiList])