# =======================================================================
# == Написать функцию-декоратор, которая подносит к квадрату значения,===
# == которое возвращает функция, к которой декоратор применяется. =======
# =======================================================================
def pow(null):
    def sqare(func):
        def inner(x):
            var = func(x)
            return var ** null
        return inner
    return sqare


@pow(2)
def kv(x):
    return x


a = kv(11)
b = kv(123)
c = kv(99)


print('Квадрат числа а =', a)
print('Квадрат числа b =', b)
print('Квадрат числа c =', c)

# Вывод
# Квадрат числа а = 121
# Квадрат числа b = 15129
# Квадрат числа c = 9801

# =======================================================================
# ======= Реализовать декоратор подключения драйвера к принтеру =========
# =======================================================================


def connect(ip, port):
    def printer(func):
        def inner(doc):
            print(f"Подключение IP: {ip}:{port}")
            print(f"Принтер {func.__name__}")
            func(doc)
            print(f"Подключение завершено")
        return inner
    return printer


@connect(ip="11.11.11.11", port="7777")
def xerox(document):
    print(f"Печать документа: {document}")


@connect(ip="22.22.22.22", port="8888")
def hp(document):
    print(f"Печать документа: {document}")


xerox("Lesson_10.doc")
hp("Lesson_11.doc")

# Вывод
# Подключение IP: 11.11.11.11:7777
# Принтер xerox
# Печать документа: Lesson_10.doc
# Подключение завершено
# Подключение IP: 22.22.22.22:8888
# Принтер hp
# Печать документа: Lesson_11.doc
# Подключение завершено