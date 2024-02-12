#
# def correct_sentence(my_str):
#     capt = my_str.capitalize()
#     return capt
# str = "ka"
# my_str = str
# print(correct_sentence(my_str))
def correct_sentence(my_text):
    my_text = my_text[0].upper() + my_text[1:]
    return my_text
    dot = my_str.find(".")
    if dot == -1:
        res = my_str + str_dot
        return res
    # else:
    #     res = my_str + dot_str
    #     return res


    # dot = my_str[:-1]
    # if my_str[:-1] == ".":
    #     return my_str
    # else:
    #     res = my_str + str_dot
    #     return res

text = "greetings, friends"
my_text = text
print(correct_sentence(my_text))


# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')