import random
p = int(input('Введите 1-ое простое число: '))
q = int(input('Введите 2-ое простое число: '))

def is_prime(n):
    k = 0
    for i in range(n):
        if n % (i+1) == 0:
            k += 1
    if (k == 2)or(n == 1):
        bool = True
    else:
        bool = False
    return bool


def gcd(a, b):
    while a!= b:
        if a > b:
            a = a % b
        elif a < b:
            b = b % a
    return a


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    A = phi
    B = e
    k = 0
    list = [[A, B, A % B, A // B]]
    while A % B != 0:
        k += 1
        C = A % B
        A = B
        B = C
        list.append([A, B, A % B, A // B])

    x = 0
    y = 1
    for i in range(k + 1):
        list[k - i].append(x)
        list[k - i].append(y)
        x0 = x
        y0 = y
        x = y0
        y = x0 - y0 * (int(list[k - i - 1][3]))

    d = list[0][5] % phi
    return d

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

