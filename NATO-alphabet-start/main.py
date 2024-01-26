
#TODO 1. Create a dictionary in this format:
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}

# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Please Enter your name? : ").upper()
name_dict = [nato_dict[letter] for letter in name]
print(name_dict)

