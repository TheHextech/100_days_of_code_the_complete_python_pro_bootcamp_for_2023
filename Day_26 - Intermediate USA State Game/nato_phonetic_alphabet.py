# TODO 1. Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}

import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dictionary = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output = [alphabet_dictionary[letter] for letter in user_input]

print(output)
