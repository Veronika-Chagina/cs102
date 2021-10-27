def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i, letter in enumerate(plaintext):    
        if letter.islower():
            index = alphabet.index(letter)
            key_index = alphabet.index(keyword[i % len(keyword)].lower())
            index = (index + key_index) % len(alphabet)
            ciphertext += alphabet[index]
        elif letter.isupper():
            index = alphabet2.index(letter)
            key_index = alphabet2.index(keyword[i % len(keyword)].upper())
            index = (index + key_index) % len(alphabet2)
            ciphertext += alphabet2[index]
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypt_text = ""

    
    for i, letter in enumerate(ciphertext):
        if letter.islower():
            index = alphabet.index(letter)
            key_index = alphabet.index(keyword[i % len(keyword)].lower())
            index = (index + key_index) % len(alphabet)
            encrypt_text += alphabet[index]
        elif letter.isupper():
            index = alphabet2.index(letter)
            key_index = alphabet2.index(keyword[i % len(keyword)].upper())
            index = (index + key_index) % len(alphabet2)
            encrypt_text += alphabet2[index]
        else:
            encrypt_text += letter
    return encrypt_text
