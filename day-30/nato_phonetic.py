
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}

def generate_phonetic():
    name = input("Please Enter your name? : ").upper()
    try:
        name_dict = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters int he alphabet please.")
        generate_phonetic()
    else:
        print(name_dict)

generate_phonetic()

# for letter in name:
#     try:
#         val = nato_dict[letter]
#     except KeyError:
#         pass
#     else:
#         name_dict.append(nato_dict[letter])
# print(name_dict)

