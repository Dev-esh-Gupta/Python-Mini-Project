student_dict = {
    "student": ["Devesh", "Seema", "Sakshi"],
    "score": [95, 88, 76]
}

for(key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)