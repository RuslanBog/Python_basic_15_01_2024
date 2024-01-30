my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
search_val = 0
for search_val in my_list:
    my_list.remove(0)
    my_list.append(0)
print(my_list)