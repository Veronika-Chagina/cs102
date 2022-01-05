import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for character in plaintext:
        if character.isupper():
            new_num = (ord(character) - ord("A") + shift) % 26
            new_unicode = new_num + ord("A")
            new_character = chr(new_unicode)
            ciphertext += new_character
        elif character.islower():
            new_num = (ord(character) - ord("a") + shift) % 26
            new_unicode = new_num + ord("a")
            new_character = chr(new_unicode)
            ciphertext += new_character
        else:
            ciphertext += character
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for character in ciphertext:
        if character.isupper():
            c_og_pos = (ord(character) - ord("A") - shift) % 26 + ord("A")
            c_og = chr(c_og_pos)
            plaintext += c_og
        elif character.islower():
            c_og_pos = (ord(character) - ord("a") - shift) % 26 + ord("a")
            c_og = chr(c_og_pos)
            plaintext += c_og
        else:
            plaintext += character
    return plaintext
