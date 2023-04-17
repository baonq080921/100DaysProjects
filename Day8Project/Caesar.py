alphabet =['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

# #encode part:
# def encrypt(plain_text, shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)+shift_amount
#         while position >= len(alphabet)-1:
#             position-=len(alphabet)
#         cipher_text+=alphabet[position]
#     print(f"The encrypt text is : {cipher_text}")        
    
    


# # decrypt part:
# def decrypt(cipher_text,shift_amount):
#     plain_text=''
#     for letter in cipher_text:
#         position=alphabet.index(letter)-shift_amount
#         plain_text+=alphabet[position]
        
#     print(f"The decode text is {plain_text}")

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)

# Function that combine ecrypt() and decrypt() call caesar():
def caesar(start_text,shift_amount, cipher_direction):
    end_text=""
    if cipher_direction =='decode':
        shift_amount*=-1
    for letter in start_text:
        position=alphabet.index(letter)
        new_position= position+shift_amount
        end_text+=alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")
caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
        


