
import string
import keyword

# # умова:
# # 1. не може починатися з цифри - startswith() - False
# # 2. не може складатися тільки з цифр - .isnumeric() - False
# # 3. не може містити великі літери - .isupper() - False
# # 4. не може містити пропуск і знаки пунктуації - string.punctuation - False
# # 5. "_" - можна
# # 6. не може бути жодним із зареєстрованих слів - keyword.kwlist - False


# some_str = '_'  # Вивід: True
# some_str = 'x'  # Вивід: True
# some_str = 'get_value'  # Вивід: True
# some_str = 'get value'  # Вивід: False
# some_str = 'get!value'  # Вивід: False
# some_str = 'some_super_puper_value'  # Вивід: True
# some_str = 'Get_value'  # Вивід: False
# some_str = 'get_Value'  # Вивід: False
# some_str = 'getValue'  # Вивід: False
# some_str = '3m'  # Вивід: False
some_str = 'm3'  # Вивід: True

new_str = True
a = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

if some_str.startswith(a) or some_str in keyword.kwlist:
    new_str = False

for name in some_str:
    if not new_str:
        break
    elif name == "_":
        continue
    elif name.isupper() or name in string.punctuation or name.isspace():
        new_str = False
        break

print(new_str)












