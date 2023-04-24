import random

# Функция поиска наибольшего общего делителя (Алгоритм Евклида)
def gcd(b, a):
    while b > 0:
        t = b
        b = a % b
        a = t
    return a

# Функция генерации простых чисел до m
def generate_prime(m):
    is_prime = {}
    for i in range(1, m):
        is_prime[i] = True
    is_prime[1] = False
    res = []
    for i in range(2, m):
        if is_prime[i]:
            res.append(i)
            j = i + i
            while j <= m:
                is_prime[j] = False
                j = j + i
    return res

# Тест Рабина-Миллера
def RabinMiller(n, r):
    b = n - 1
    k = -1
    B = []
    k += 1
    B.append(b % 2)  
    b = b // 2
    while b > 0:
        k += 1
        B.append(b % 2)
        b = b // 2
 
    for j in range(1, r + 1):
        a = random.randrange(2, n)
        if gcd(a, n) > 1:
          return False
        d = 1
    for i in range(k, -1, -1):
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return False
        if B[i] == 1:
            d = (d * a) % n
    if d != 1:
        return False
    return True

# Функция генерации большого простого числа (используется проверка на простое число тестом Рабина-Миллера)
def generate_prime_number():
    while(True):
        res = random.randint(100000000, 10**100)
        for el in prime:
            if res == el:
                return res
            if res % el == 0:
                continue
        if RabinMiller(res, 64):
            return res

# Бинарное возведение в степень
def modExp(v, st, mod):
    if st == 0:
        return 1
    if st == 1:
        return v
    if st % 2 == 0:
        cur = modExp(v, st // 2, mod)
        cur %= mod
        cur = cur * cur % mod
        return cur
    else:
        cur = modExp(v, st // 2, mod)
        cur %= mod
        cur = cur * cur * v % mod
        return cur

def DiffieHellman(g, x, p, q):
    new_x = x % q
    X = modExp(g, new_x, p)
    return X

def generate_g(N):
    q = generate_prime_number()
    flag_prime = True
    while(flag_prime):
        n = random.randrange(2, N)
        p = n * q + 1
        for el in prime:
            if p == el:
                flag_prime = False
            if p % el == 0:
                continue
        if RabinMiller(p, 64):
            flag_prime = False
    g = 1
    while g == 1:
        a = random.randrange(2, p-1)
        g = modExp(a, n, p)

    print("p: ", p)
    print("g: ", g)
    return (g, q, p)

N = 1000000

prime = generate_prime(N)

g, q, p = generate_g(N)
x = random.randrange(1, p-1)
y = random.randrange(1, p-1)
X = DiffieHellman(g, x, p, q)
Y = DiffieHellman(g, y, p, q)

print("Пользователь А сгенерировал случайное число x: ", x)
print("Пользователь А отправляет Пользователю В X: ", X)
print("Пользователь В сгенерировал случайное число y: ", y)
print("Пользователь В отправляет Пользователю А Y: ", Y)

key = modExp(Y, x, p)
key2 = modExp(X, y, p)

if (key == key2 == modExp(g, x*y, p)):
    print("Общий ключ: ", key)
else:
    print("Что-то пошло не так")

