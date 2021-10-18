def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = input()
    key = input()
    encrypt_text = str()

    if text.islower():
        for i, letter in enumerate(text):
            index = alphabet.index(letter)
            key_index = alphabet.index(key[i % len(key)])
            index = (index + key_index) % len(alphabet)
            encrypt_text += alphabet[index]
    elif text.isupper():
        for i, letter in enumerate(text):
            index = alphabet2.index(letter)
            key_index = alphabet2.index(key[i % len(key)])
            index = (index + key_index) % len(alphabet2)
            encrypt_text += alphabet2[index]
    print(encrypt_text)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = input()
    key = input()
    encrypt_text = str()

    if text.islower():
        for i, letter in enumerate(text):
            index = alphabet.index(letter)
            key_index = alphabet.index(key[i % len(key)])
            index = (index + key_index) % len(alphabet)
            encrypt_text += alphabet[index]
    elif text.isupper():
        for i, letter in enumerate(text):
            index = alphabet2.index(letter)
            key_index = alphabet2.index(key[i % len(key)])
            index = (index + key_index) % len(alphabet2)
            encrypt_text += alphabet2[index]
    print(encrypt_text)
    return plaintext
