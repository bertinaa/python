alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#note we type alphabets twice so it doesn't matter even if we give a word like xyz it will still work right
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#arguments
str_text = input("Type your message:\n").lower()
num_shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#parameters
def encrypt(text,shift):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    cipher_text += alphabet[new_position]
  print(cipher_text)
    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(str_text,num_shift)
