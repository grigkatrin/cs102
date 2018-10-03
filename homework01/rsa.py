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
