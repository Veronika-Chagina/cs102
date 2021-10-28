import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for c in plaintext:
        if c.isupper():
            c_unicode = ord(c)
            c_num = ord(c) - ord("A")
            new_num = (c_num + shift) % 26
            new_unicode = new_num + ord("A")
            new_character = chr(new_unicode)
            ciphertext = ciphertext + new_character
        elif c.islower():
            c_unicode = ord(c)
            c_num = ord(c) - ord("a")
            new_num = (c_num + shift) % 26
            new_unicode = new_num + ord("a")
            new_character = chr(new_unicode)
            ciphertext = ciphertext + new_character
        else:
            ciphertext += c
    return ciphertext

    
def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord("A")
            c_og_pos = (c_index - shift) % 26 + ord("A")
            c_og = chr(c_og_pos)
            plaintext += c_og
        elif c.islower():
            c_index = ord(c) - ord("a")
            c_og_pos = (c_index - shift) % 26 + ord("a")
            c_og = chr(c_og_pos)
            plaintext += c_og
        else:
            plaintext += c
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
