st = input()
k = 3

def encrypt_caesar (plaintext):
    ciphertext = ''
    for i in range(len(plaintext)):
        if (ord(plaintext[i]) >= ord('a')) and (ord(plaintext[i]) <= ord('z')):
            if ord(plaintext[i]) + k > ord('z'):
                ciphertext = ciphertext + chr(ord(plaintext[i]) + k - 26)
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + k)
        elif (ord(plaintext[i]) >= ord('A')) and (ord(plaintext[i]) <= ord('Z')):
            if ord(plaintext[i]) + k > ord('Z'):
                ciphertext = ciphertext + chr(ord(plaintext[i]) + k - 26)
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + k)
        else:
            ciphertext = ciphertext + plaintext[i]
    return ciphertext

def decrypt_caesar (ciphertext):
    plaintext = ''
    for i in range(len(ciphertext)):
        if (ord(ciphertext[i]) >= ord('a')) and (ord(ciphertext[i]) <= ord('z')):
            if ord(ciphertext[i]) - k < ord('a'):
                plaintext = plaintext + chr(ord(ciphertext[i]) - k + 26)
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - k)
        elif (ord(ciphertext[i]) >= ord('A')) and (ord(ciphertext[i]) <= ord('Z')):
            if ord(ciphertext[i]) - k < ord('A'):
                plaintext = plaintext + chr(ord(ciphertext[i]) - k + 26)
            else:
                plaintext = plaintext + chr(ord(otvet[i]) - k)
        else:
            plaintext = plaintext + otvet[i]
    return plaintext
