
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}


name = input("Please Enter your name? : ").upper()
name_dict = [nato_dict[letter] for letter in name]
print(name_dict)

