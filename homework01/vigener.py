st = input()
k = input()

def encrypt_vigener (plaintext, keyword):
    ciphertext = ''
    j = 0
    for i in range(len(plaintext)):
        if (ord(plaintext[i]) >= ord('a')) and (ord(plaintext[i]) <= ord('z')):
            if ord(plaintext[i]) + ((ord(keyword[j])-ord('a'))%26) > ord('z'):
                ciphertext = ciphertext + chr(ord(plaintext[i]) + ((ord(keyword[j])-ord('a'))%26) - 26)
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + ((ord(keyword[j])-ord('a'))%26))
        elif ((ord(plaintext[i]) >= ord('A')) and (ord(plaintext[i]) <= ord('Z'))):
            if ord(plaintext[i]) + ((ord(keyword[j])-ord('A'))%26) > ord('Z'):
                ciphertext = ciphertext + chr(ord(plaintext[i]) + ((ord(keyword[j])-ord('A'))%26) - 26)
            else:
                ciphertext = ciphertext + chr(ord(plaintext[i]) + ((ord(keyword[j])-ord('A'))%26))
        else:
            ciphertext = ciphertext + plaintext[i]
        if j >= (len(keyword)-1):
            j = 0
        else:
            j += 1
    return ciphertext

otvet = encrypt_vigener (st, k)
print(otvet)


def decrypt_vigener (ciphertext, keyword):
    plaintext = ''
    j = 0
    for i in range(len(ciphertext)):
        if (ord(ciphertext[i]) >= ord('a')) and (ord(ciphertext[i]) <= ord('z')):
            if ord(ciphertext[i]) - ((ord(keyword[j])-ord('a'))%26) < ord('a'):
                plaintext = plaintext + chr(ord(ciphertext[i]) - ((ord(keyword[j])-ord('a'))%26) + 26)
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - ((ord(keyword[j])-ord('a'))%26))
        elif ((ord(ciphertext[i]) >= ord('A')) and (ord(ciphertext[i]) <= ord('Z'))):
            if ord(ciphertext[i]) - ((ord(keyword[j])-ord('A'))%26) < ord('A'):
                plaintext = plaintext + chr(ord(ciphertext[i]) - ((ord(keyword[j])-ord('A'))%26) + 26)
            else:
                plaintext = plaintext + chr(ord(ciphertext[i]) - ((ord(keyword[j])-ord('A'))%26))
        else:
            plaintext = plaintext + ciphertext[i]
        if j >= (len(keyword)-1):
            j = 0
        else:
            j += 1
    return plaintext

otvet2 = decrypt_vigener(otvet,k)
print(otvet2)
