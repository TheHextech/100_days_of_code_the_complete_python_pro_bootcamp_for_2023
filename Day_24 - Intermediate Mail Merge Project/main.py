PLACEHOLDER = "[name]"
BY = "Lele"

with open("Input/Names/invited_names.txt") as names:
    list_names = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_to_modify = letter.read()

    for name in list_names:
        stripped_name = name.strip()
        final_letter = letter_to_modify.replace(PLACEHOLDER, stripped_name).replace("Angela", BY)
        with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(final_letter)
