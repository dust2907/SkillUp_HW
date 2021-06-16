A = {7, "File", 15, "с"}
print(A)
B = {"Island", 14, "a", 234}
print(B)
C = {678, "b", 19, "Weather", 1999}
print(C)

# Разные элементы для A и B
print (A|B)

# Одинаковые элементы для A и C
print(A&C)

# Объединение 3х множеств
print(A^B^C)