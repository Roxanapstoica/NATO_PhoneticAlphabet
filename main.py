# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.

# Obtin o lista de int list1
with open("file1.txt") as file1:
    list1 = file1.readlines()
    #list1 = [int(item) for item in list1] (daca nu am ENTER la sfarsitul fisierului)

# Obtin o lista de int list2
with open("file2.txt") as file2:
    list2 = file2.readlines()
    #list2 = [int(item) for item in list2] (daca nu am ENTER la sfarsitul fisierului)

result = [int(item) for item in list1 if item in list2]
print(result)