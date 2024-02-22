# а) Створити список із ключів, які є в обох словниках.
# б) Створити список із ключів, які є у першому, але немає у другому словнику.
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

my_dict_1 = {1:10, 2:2}
my_dict_2 = {11:11, 2:22}

common_keys = list(set(my_dict_1).intersection(my_dict_2))
dif_keys = list(set(my_dict_1).difference(my_dict_2))
new_dict_values = my_dict_1
for key in dif_keys:
    new_dict_values[key] = my_dict_1[key]


un_dict = my_dict_1.copy()
for key in my_dict_2:
    if key in un_dict:
        un_dict[key] = [un_dict[key], my_dict_2[key]]
    else:
        un_dict[key] = my_dict_2[key]

print(f"Common keys is {common_keys} and different keys is {dif_keys}, new dict with values {new_dict_values}, new dict with rules {un_dict}")
