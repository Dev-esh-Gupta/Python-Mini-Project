# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing mode
# with open("my_file.txt", mode="w") as file:
#     file.write("New Text . ")

# Appending mode
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew Text . ")

# if we open file that doesn't exist the it will gonna create file freshly
# with open("new_file.txt", mode="a") as file:
#     file.write("New Text. ")

# with open("C:/Users/deves/OneDrive/Desktop/new_file.txt") as file:
#     content = file.read()
#     print(content)

with open("../../OneDrive/Desktop/new_file.txt") as file:
    content = file.read()
    print(content)