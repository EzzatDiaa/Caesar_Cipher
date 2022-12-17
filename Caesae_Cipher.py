# caesar-cipher project
from caesar_logo import logo
print(logo)
print("Welcome to the Caesar Cipher")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(tex, shi, di):
    end_tex = ""
    if di == "decode":
        shi *= -1
    for char in tex:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shi
            end_tex += alphabet[new_position]
        else:
            end_tex += char
    print(f"The {di} text is {end_tex}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode'to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(tex=text, shi=shift, di=direction)
    restart = input("Type 'yes' if you want to go again, otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")
