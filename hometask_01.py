import random
import string

# Задание 1
print('Input string: ', end='')
a = input()
L = a.__len__()
N = int(a.__len__()//5)
n = 0

def foo(d):
    m = 0
    print(d)
    for k in d:
        for p in k:
            if 'A' <= p <= 'Z':
                m = m + 1
        if m > 0:
            print(k)
        m = 0

for e in range(0, 5):
    n = n + N
    b = a[0:n]
    c = a[n:]
    a = b + '_' + c

a = a.split('_')
print(a)
foo(a)

# Задание 2
s = ''
print("Input N=", end='')
J = int(input())

for e in range(1, J):
    s = s + random.choice(string.ascii_letters + string.digits)
    if random.randint(0, 5) > 3:
        s = s + '_'

s = s.split('_')
print(s)

foo(s)