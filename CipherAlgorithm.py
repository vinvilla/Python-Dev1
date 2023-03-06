# CEASAR CIPHER
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '^', '&',
            '*', '(', ')', ' ']

flag = False

def encrypt(text, shift):
    inputList = [x for x in text]
    cipher_text = ""
    #  print(inputList)
    for i in range(0, len(inputList)):
        # print(alphabet.index(inputList[i]))
        # encryptedText.append(alphabet[alphabet.index(inputList[i])+shift])
        if ((alphabet.index(inputList[i]) + shift) >= len(alphabet) - 1):
            cipher_text += alphabet[alphabet.index(inputList[i]) + shift - len(alphabet)]
        else:
            cipher_text += alphabet[alphabet.index(inputList[i]) + shift]
    print(f"The encoded text is {cipher_text}")


def decrypt(text, shift):
    inputList = [x for x in text]
    cipher_text = ""
    for i in range(0, len(inputList)):
        if ((alphabet.index(inputList[i]) + shift) >= len(alphabet) - 1):
            cipher_text += alphabet[alphabet.index(inputList[i]) - shift - len(alphabet)]
        else:
            cipher_text += alphabet[alphabet.index(inputList[i]) - shift]
    print(f"The encoded text is {cipher_text}")


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")


while (flag == False):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to Exit:\n")
    if (direction != "encode") and (direction != "decode"):
        flag = True
        print("Thank you! Good Bye!")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)
        elif direction == "exit":
            flag = True
        else:
            print("Invalid Entry! Try again")
