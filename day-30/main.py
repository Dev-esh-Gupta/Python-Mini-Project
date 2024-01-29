# File not found error
# with open("data.txt", 'r') as file:
#     data = file.read()

# Key Error
# dic = {"Key": "value", "Key2": "Value2"}
# val = dic["Key3"]

# Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# furit = fruit_list[5]

# Type Error
# text = "abc"
# print(text + 5)

# Handling above exception
# try:
#     file = open("a_file.txt")
#     dict = {"key" : "value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     print("There was an error")
# except KeyError as error_message:
#     print(f"That key {error_message} is not found")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File were closed!")
#     raise TypeError

# Crating your own error
height = float(input("Height : "))
weight = int(input("Weight : "))

if height > 3:
    raise ValueError("Human Height should not be greater than 3 meter")

bmi = weight / height ** 2
print(bmi)

