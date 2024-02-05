import string
some_str = "55"
new_name_val = ""

for name in some_str:
    if name.isnumeric():
        new_name_val = False
    elif name.isupper():
        new_name_val = False
    else:
        new_name_val = True
print(new_name_val)
    # if some_str.isnumeric():
    #     name_val = False
    # else:
    #     name_val = True
# for name in some_str:
#     if some_str.isnumeric():
#         print(False)
#         # break
#     elif some_str.isupper():
#         print(False)
        # break
    # else:
    #     print(True)
        # break



# for name in some_str:
#     if some_str.isupper():
#         name_val = False
#         break
# else:
#     name_val = True
# print(name_val)

