PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Output/ReadyToSend/example.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        strinpped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,strinpped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{strinpped_name}.txt", mode="w")\
            as completed_letter:
            completed_letter.write(new_letter)
# with open("./Output/ReadyToSend/example.txt", mode='r+') as file:
#     file.readline().replace(name)
    
