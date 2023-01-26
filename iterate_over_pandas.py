import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# looping through a dictionary:
# for (key, val) in student_dict.items():
#     print(key)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through a DataFrame:
# for (key, val) in student_data_frame.items():
#     print(val)

## Pandas has an inbuild loop, called iterrows (loops through each of the ROW, not column, so it returns pandas series objects)
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
