import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dictionary = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}

def generate_phonetics():

    """This function was generated in lesson 30, updating the code developed in lesson 26. This version
    also provide a repeat in case the user entered a null value."""

    user_input = input("\nEnter a word: ").upper()

    if user_input == '':
        print("Insert at least one letter please.\n")
        return generate_phonetics()

    else:

        try:
            output = [alphabet_dictionary[letter] for letter in user_input]

        except KeyError:
            print("Sorry, only letters in the alphabet please.\n")
            generate_phonetics()

        else:
            print(output)

generate_phonetics()