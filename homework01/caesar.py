def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    k = 3
    ciphertext = ''
    for i in range(len(plaintext)):
        if 'a' <= plaintext[i] <= 'z':
            if ord(plaintext[i]) + k > ord('z'):
                ciphertext = ciphertext + chr(ord(plaintext[i]) + k - 26)
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + k)
        elif 'A' <= plaintext[i] <= 'Z':
            if ord(plaintext[i]) + k > ord('Z'):
                ciphertext = ciphertext + chr(ord(plaintext[i]) + k - 26)
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + k)
        else:
            ciphertext = ciphertext + plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    k = 3
    plaintext = ''
    for i in range(len(ciphertext)):
        if 'a' <= ciphertext[i] <= 'z':
            if ord(ciphertext[i]) - k < ord('a'):
                plaintext = plaintext + chr(ord(ciphertext[i]) - k + 26)
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - k)
        elif 'A' <= ciphertext[i] <= 'Z':
            if ord(ciphertext[i]) - k < ord('A'):
                plaintext = plaintext + chr(ord(ciphertext[i]) - k + 26)
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - k)
        else:
            plaintext = plaintext + ciphertext[i]
    return plaintext