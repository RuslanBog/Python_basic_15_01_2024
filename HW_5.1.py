
import string
import keyword
# дано:
some_val = "orjb2"

# условие:
# 1. не може починатися з цифри - startswith() - False
# 2. не може складатися тільки з цифр - .isnumeric() - False
# 3. не може містити великі літери - .isupper() - False
# 4. не може містити пропуск і знаки пунктуації - string.punctuation - False
# 5. "_" - можна
# 6. не може бути жодним із зареєстрованих слів - keyword.kwlist - False
a = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# for x in some_val:
#     if x is some_val.isupper():#цифри сприймає як велику літеру(
#         print(False)
#         break
print(not some_val.startswith(a)
      and not some_val.isnumeric()
      and not keyword.iskeyword(some_val))















