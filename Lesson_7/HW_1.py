def multiply(a):
    b = 1
    for c in a:
        if c != 0:
            b *= c

    return b


e = [1, 2, 3, 4, 5]
print(multiply(e))


# Вывод
# 120