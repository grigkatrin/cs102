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
        if ('a' <= plaintext[i] <= 'z') or ('A' <= plaintext[i] <= 'Z'):
            if plaintext[i].isupper():
                if ord(plaintext[i].lower()) + k > ord('z'):
                    ciphertext += chr(ord(plaintext[i].lower()) + k - 26).upper()
                else:
                    ciphertext += chr(ord(plaintext[i].lower()) + k).upper()
            else:
                if ord(plaintext[i]) + k > ord('z'):
                    ciphertext += chr(ord(plaintext[i]) + k - 26)
                else:
                    ciphertext += chr(ord(plaintext[i]) + k)
        else:
            ciphertext += plaintext[i]
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
        if ('a' <= ciphertext[i] <= 'z') or ('A' <= ciphertext[i] <= 'Z'):
            if ciphertext[i].isupper():
                if ord(ciphertext[i].lower()) - k < ord('a'):
                    plaintext += chr(ord(ciphertext[i].lower()) - k + 26).upper()
                else:
                    plaintext += chr(ord(ciphertext[i].lower()) - k).upper()
            else:
                if ord(ciphertext[i]) - k < ord('a'):
                    plaintext += chr(ord(ciphertext[i]) - k + 26)
                else:
                    plaintext += chr(ord(ciphertext[i]) - k)
        else:
            plaintext += ciphertext[i]
    return plaintext
