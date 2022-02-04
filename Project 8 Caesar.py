from Project8Art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
PG = "yes"


def caesar(t, s):
    ed = ''
    for letter in t:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                np = position + s
                if np > 25:
                    np %= 26
                ed += alphabet[np]
            else:
                np = position - s
                if np < -25:
                    np %= 26
                ed += alphabet[np]
        else:
            ed += letter
    print(ed)


while PG == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(t=text, s=shift)
    PG = input('Would you like to try again? Enter yes or no. ')
