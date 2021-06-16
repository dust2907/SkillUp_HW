tuples_1 = (3, 9, 18, 13)
tuples_2 = (4, 10, 16, 13)
tuples_3 = (2, 8, 17, 2233)
print(tuples_1)
print(tuples_2)
print(tuples_3)


# Элементы, которые есть во всех кортежах
a = list(set(tuples_1) & set(tuples_2) & set(tuples_3))
print(a)

# Элементы, уникальные для каждого списка
u_numbers_1 = set(tuples_1) - set(tuples_2) - set(tuples_3)
u_numbers_2 = set(tuples_2) - set(tuples_1) - set(tuples_3)
u_numbers_3 = set(tuples_3) - set(tuples_2) - set(tuples_1)
print(u_numbers_1, u_numbers_2, u_numbers_3)

# Элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции
print(tuples_1[4])
print(tuples_2[4])
print(tuples_3[4])