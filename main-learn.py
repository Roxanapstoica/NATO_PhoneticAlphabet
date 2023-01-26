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

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}