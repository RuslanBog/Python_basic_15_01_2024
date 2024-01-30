my_list = [1, 3, 5]
if len(my_list) == 0:
    print(0)
else:
    new_list = sum(my_list[0::2])
    last_int = my_list[-1]
    res = new_list * last_int
    print(res)
