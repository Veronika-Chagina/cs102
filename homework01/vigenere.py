import string


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabet1 = string.ascii_lowercase
    alphabet2 = string.ascii_uppercase

    for i, letter in enumerate(plaintext):
        if letter.islower():
            index = alphabet1.index(letter)
            key_index = alphabet1.index(keyword[i % len(keyword)].lower())
            index = (index + key_index) % len(alphabet1)
            ciphertext += alphabet1[index]
        elif letter.isupper():
            index = alphabet2.index(letter)
            key_index = alphabet2.index(keyword[i % len(keyword)].upper())
            index = (index + key_index) % len(alphabet2)
            ciphertext += alphabet2[index]
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    alphabet1 = string.ascii_lowercase
    alphabet2 = string.ascii_uppercase
    encrypt_text = ""

    for i, letter in enumerate(ciphertext):
        if letter.islower():
            index = alphabet1.index(letter)
            key_index = alphabet1.index(keyword[i % len(keyword)].lower())
            index = (index - key_index) % len(alphabet1)
            encrypt_text += alphabet1[index]
        elif letter.isupper():
            index = alphabet2.index(letter)
            key_index = alphabet2.index(keyword[i % len(keyword)].upper())
            index = (index - key_index) % len(alphabet2)
            encrypt_text += alphabet2[index]
        else:
            encrypt_text += letter
    return encrypt_text
