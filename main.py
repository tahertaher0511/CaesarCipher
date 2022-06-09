from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
play_game = True


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if shift > 26:
        shift_amount = shift % 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")


while play_game:
    direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n").lower()
    text = input("Type your massage:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
    ask_users = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
    if ask_users == 'yes':
        play_game = True
    else:
        play_game = False
        print('BYE.')
