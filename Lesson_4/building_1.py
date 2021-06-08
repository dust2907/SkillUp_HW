n = int(input('Введите целое трёхзначное число : '))
s = 0
m = 1
while n > 0:
    d = n % 10
    s = n + d
    m = n * d
    n = n // 10
print("Сумма:", s)
print("Произведение:", m)