def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if plaintext.islower():
        for i, letter in enumerate(plaintext):
            index = alphabet.index(letter)
            key_index = alphabet.index(keyword[i % len(keyword)])
            index = (index + key_index) % len(alphabet)
            ciphertext += alphabet[index]
    elif plaintext.isupper():
        for i, letter in enumerate(plaintext):
            index = alphabet2.index(letter)
            key_index = alphabet2.index(keyword[i % len(keyword)])
            index = (index + key_index) % len(alphabet2)
            ciphertext += alphabet2[index]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypt_text = ""

    if ciphertext.islower():
        for i, letter in enumerate(ciphertext):
            index = alphabet.index(letter)
            key_index = alphabet.index(keyword[i % len(keyword)])
            index = (index + key_index) % len(alphabet)
            encrypt_text += alphabet[index]
    elif ciphertext.isupper():
        for i, letter in enumerate(ciphertext):
            index = alphabet2.index(letter)
            key_index = alphabet2.index(keyword[i % len(keyword)])
            index = (index + key_index) % len(alphabet2)
            encrypt_text += alphabet2[index]
    return plaintext
