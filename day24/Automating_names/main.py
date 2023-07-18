
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open ("Input/Names/invited_names.txt") as names:
    invited_names = names.readlines() #invited_names is a list of all the names now

with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter_content = starting_letter.read()

for name in invited_names:
    stripped_name = name.strip()
    #note : this doesn't work if you do name.strip()
    with open(f"Output/ReadyToSend/{stripped_name}.txt","w") as new_letter:
        final_text = letter_content.replace(PLACEHOLDER,stripped_name)
        new_letter.write(final_text)


