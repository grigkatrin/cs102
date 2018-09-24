
'''
    Форматированный ввод/вывод данных
'''
m = 10
pi = 3.1415927
print("m = ",m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {}, pi = {}".format(m,pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")
'''
code = input("Enter your position number in group: ")
n1, n2 = input("Enter two numbers splitted by space:").split()
d, m, y = input("Enter three numbers splitted by\'.\': ").split('.')
print("{} + {} = {}".format(n1,n2,float(n1)+float(n2)))
print("Your birthday is %s.%s.%s and you are %d in the group list" % (d,m,y,int(code)))
'''

print('m = %4d;' % m, 'pi = %.3f' % pi)
print("\n")

print("m = {}; pi = {}".format(m,pi))
print("\n")

year = 1
print('year: ', year)
print("\n")
'''
r1, m1, p1 = input('Enter your EGE scores for russian language, mathematics, informatics splitted by comma: ').split(',')
print('r1 = {}; m1 = {}; p1 = {}'.format(r1,m1,p1))
print("\n")


base = (4%8+2) # 4 - день рождения
a = int(input('Enter a number with 12 digits in {} scale of notation: '.format(base)))
ans = 0
for i in range(12):
    j = a%10
    ans += j*(base**i)
    a = a//10
print('Your number in 10 scale of notation ',ans)
print("\n")
'''
n = int(input('Enter a number: '))
print('n * 2: ', n<<1)
print('n / 2: ', n>>1)