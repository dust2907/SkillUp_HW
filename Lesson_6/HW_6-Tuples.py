tuple_1 = (3, 9, 18, 13)
tuple_2 = (4, 10, 16, 13)
tuple_3 = (2, 8, 17, 2233)
print(tuple_1)
print(tuple_2)
print(tuple_3)


# Элементы, которые есть во всех кортежах
a = list(set(tuple_1) & set(tuple_2) & set(tuple_3))
print(a)

# Элементы, уникальные для каждого списка
u_numbers_1 = set(tuple_1) - set(tuple_2) - set(tuple_3)
u_numbers_2 = set(tuple_2) - set(tuple_1) - set(tuple_3)
u_numbers_3 = set(tuple_3) - set(tuple_2) - set(tuple_1)
print(u_numbers_1, u_numbers_2, u_numbers_3)

# Элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции
print(tuples_1[4])
print(tuples_2[4])
print(tuples_3[4])