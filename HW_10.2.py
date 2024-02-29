# Ваша функція is_even повинна повертати True якщо число парне,
# і False якщо число непарне.
# Вхідні дані: Ціле число.
# Вихідні дані: Логічний тип.

def is_even(digit):
    """ Перевірка чи є парним число """

    x = digit
    if x % 2 == 0:
        res = True
    else:
        res = False

    return res
# digit = 2
# print(is_even(2))

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')