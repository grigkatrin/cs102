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
        if 'a' <= plaintext[i] <= 'z':
            t = (ord(keyword[j]) - ord('a')) % 26
            if ord(plaintext[i]) + t > ord('z'):
                ciphertext = ciphertext + chr(ord(plaintext[i]) + t - 26)
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + t)
        elif 'A' <= plaintext[i] <= 'Z':
            t = (ord(keyword[j]) - ord('A')) % 26
            if ord(plaintext[i]) + t > ord('Z'):
                ciphertext = ciphertext + chr(ord(plaintext[i]) + t - 26)
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + t)
        else:
            ciphertext = ciphertext + plaintext[i]
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
        if 'a' <= ciphertext[i] <= 'z':
            t = (ord(keyword[j]) - ord('a')) % 26
            if ord(ciphertext[i]) - t < ord('a'):
                plaintext = plaintext + chr(ord(ciphertext[i]) - t + 26)
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - t)
        elif 'A' <= ciphertext[i] <= 'Z':
            t = (ord(keyword[j]) - ord('A')) % 26
            if ord(ciphertext[i]) - t < ord('A'):
                plaintext = plaintext + chr(ord(ciphertext[i]) - t + 26)
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - t)
        else:
            plaintext = plaintext + ciphertext[i]
        if j >= (len(keyword) - 1):
            j = 0
        else:
            j += 1
    return plaintext
