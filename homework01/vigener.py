def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    j = 0
    for i in range(len(plaintext)):
        if ('a' <= plaintext[i] <= 'z') or ('A' <= plaintext[i] <= 'Z'):
            if keyword[j].isupper():
                t = (ord(keyword[j].lower()) - ord('a')) % 26
            else:
                t = (ord(keyword[j]) - ord('a')) % 26
            if plaintext[i].isupper():
                if ord(plaintext[i].lower()) + t > ord('z'):
                    ciphertext += chr(ord(plaintext[i].lower()) + t - 26).upper()
                else:
                    ciphertext += chr(ord(plaintext[i].lower()) + t).upper()
            else:
                if ord(plaintext[i]) + t > ord('z'):
                    ciphertext += chr(ord(plaintext[i]) + t - 26)
                else:
                    ciphertext += chr(ord(plaintext[i]) + t)
        else:
            ciphertext += plaintext[i]
        if j >= (len(keyword) - 1):
            j = 0
        else:
            j += 1
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    j = 0
    for i in range(len(ciphertext)):
        if ('a' <= ciphertext[i] <= 'z') or ('A' <= ciphertext[i] <= 'Z'):
            if keyword[j].isupper():
                t = (ord(keyword[j].lower()) - ord('a')) % 26
            else:
                t = (ord(keyword[j]) - ord('a')) % 26
            if ciphertext[i].isupper():
                if ord(ciphertext[i].lower()) - t < ord('a'):
                    plaintext += chr(ord(ciphertext[i].lower()) - t + 26).upper()
                else:
                    plaintext += chr(ord(ciphertext[i].lower()) - t).upper()
            else:
                if ord(ciphertext[i]) - t < ord('a'):
                    plaintext += chr(ord(ciphertext[i]) - t + 26)
                else:
                    plaintext += chr(ord(ciphertext[i]) - t)

        else:
            plaintext += ciphertext[i]
        if j >= (len(keyword) - 1):
            j = 0
        else:
            j += 1
    return plaintext
