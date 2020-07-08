import string
import random

# One TIme Pad Algorithm: An encoding which applies the key as a shift to the plaintext.
# For example, if the key is APPLES and the plaintext is SECRET, the ciphertext is {|`0=9
# One Time Pad is a perfect encryption if the key does not repeat itself and is truly random.
# Method:
    # 1. Generate a key, preferably random.
    # 2. Convert the key and plaintext to a set of numbers.
    # 3. Take the modular addition of the key and the plaintext to create the ciphertext.
    # 4. Subtract the key from the ciphertext to form the plaintext.

def oneTimePad(text, key_string, mode):
    new_string = ""
    num_chars = len(string.printable)
    chr_int = {c:i for (i, c) in enumerate(string.printable)}
    int_chr = {i:c for (i, c) in enumerate(string.printable)}
    for i in range(len(text)):
        text_ascii = chr_int[text[i]]
        key_ascii = chr_int[key_string[i]]
        if mode == "encode":
            enc = (text_ascii + key_ascii) % num_chars
        else:
            enc = (text_ascii - key_ascii) % num_chars
        new_string += str(int_chr[enc])
    return new_string

if __name__ == '__main__':
    text = "SECRET"
    key = "APPLES"
    cipher = oneTimePad(text, key, "encode")
    decoded = oneTimePad(cipher, key, "decode")
    print("Plaintext: " + text)
    print("Cipher: " + key)
    print("Ciphertext: " + cipher)
    print("Decoded Ciphertext: " + decoded)
