
my_list = [12, 3, 4, 10, 8]
if len(my_list) >= 1:
    short_list = my_list[0:-1]
    first_value = my_list[-1]
    first_value = [first_value]
    new_list = first_value + short_list
    print(new_list)
else:
    my_list = my_list
