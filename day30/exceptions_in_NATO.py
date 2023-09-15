student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def get_word():
    word = input("Give me a word.").upper()
    try:
        output = [new_dict[letter] for letter in word]
    except KeyError:
        print("Please enter alphabets.")
        get_word()
    else:
        print(output)

get_word()
