from logo_of_caesar import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(direction,start_text,shift_amount):
    end_text=""
    if direction=="decode":
        shift_amount=shift_amount*(-1)
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=letter
    print(f"your {direction}d result : {end_text}")
reply=True
while reply:
        
    directions=input("Type encode to encrypt, decode to decrypt.\n").lower()
    text=input("Type your message.\n").lower()
    shift=int(input("Type shift number: "))
    shift=shift%26
    caesar(direction=directions,start_text=text,shift_amount=shift)
    restart=input("Tpye 'yes' for again go otherwise 'no'.\n").lower()
    if restart=="no":
        reply=False