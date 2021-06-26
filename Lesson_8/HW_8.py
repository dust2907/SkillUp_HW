# ==================================================================
# == Функция, которая отображает на экран форматированный текст ==
# ==================================================================

def task1():
    text = '''“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself."
                                                
                                    Bill Gates'''
    print(text)

task1()

# Вывод
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
#
#                                     Bill Gates

# ========================================================================================================
# == Функция, которая принимает два числа в качестве параметра и отображает все четные числа между ними ==
# ========================================================================================================

def task_2 (a, b):
    for i in range (a, b):
        if i % 2 == 0:
            print(i)

task_2 (a=11, b=33)

# Вывод
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28
# 30
# 32

# ========================================================================================================
# == функция, которая отображает пустой или заполненный квадрат из некоторого символа. ===================
# ========================================================================================================

def task_3 (side, sign, fill):
    if fill:
        for i in range (side):
            print(sign*side)
    else:
        pass

task_3(side=10, sign='*', fill=True)

# Вывод
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********

# ========================================================================================================
# ==================== Функция, которая возвращает минимальное из пяти чисел. ============================
# ========================================================================================================

def task_4(z, x, c, v, b):
    print (min(z, x, c, v, b))

task_4(122, 333, 9867, 23, 435)

# Вывод
# 23

# ========================================================================================================
# =========== Функцию, которая возвращает произведение чисел в указанном диапазоне.=======================
# ========================================================================================================

def task_5(c, e):
    if c == e:
        return "Диапазон введен неверно"
    if c > e:
        c, e = e, c
    pro = 1
    for i in range (c, e):
        pro *= i
    return pro

print("Произведение чисел от 30 до 40 =", task_5(30, 40 +1))

# Вывод
# Произведение чисел от 30 до 40 = 92279715720192000

# ========================================================================================================
# ====================== Функция, которая считает количество цифр в числе ================================
# ========================================================================================================


def task_6(d):
    kol = 0
    for i in range(len(str(d))):
        kol += 1
        return kol

print("Количество цифр в числе 3 =", task_6(3))

# Вывод
# Количество цифр в числе 3 = 1

# ========================================================================================================
# ====================== Функция, функцию, которая проверяет является ли число палиндромом ===============
# ========================================================================================================

def task_7(num):
    text = str(num)
    if len(text) % 2 != 0:
        return False
    first_part = text[:len(text) // 2]
    second_part = text[len(text) // 2:]
    result = first_part == second_part[::-1]
    return result

task_7(123321)
print(result)