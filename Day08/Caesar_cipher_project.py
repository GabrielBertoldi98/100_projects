import string

alphabet =list(string.ascii_lowercase)

def caesar_cipher():
    answer = ""    
    while answer != "no":

        word = list(input("Type your phrase: ").lower())
        displacement = int(input("Type a number: "))
        encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        
        def encode(word, displacement):
                result = ""
                for letter in word:
                    if  letter in alphabet:
                        position = alphabet.index(letter)
                        new_position = position + displacement

                        #start the alphabet again
                        new_position = new_position % len(alphabet)

                        result += alphabet[new_position]
                    else:
                        result += letter
                print("Result encript: ", result)

        def decode(word,displacement):
                result = ""
                for letter in word:
                    if  letter in alphabet:
                        position = alphabet.index(letter)
                        new_position = position - displacement

                        #start the alphabet again
                        new_position = new_position % len(alphabet)

                        result += alphabet[new_position]
                    else:
                        result += letter

                print("Result decript: ", result)

        if encode_decode == "encode":
             encode(word, displacement)
        elif encode_decode == "decode":
             decode(word, displacement)
        answer = input("Do you want continue? yes/no: ")

caesar_cipher()