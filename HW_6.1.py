# list_min_age = наймолодша людина
# longer_name = найдовше імя
# middle_age = середній вік усіх людей з початкового списку

# дано список в якому лежать дікти

list_1 = [
    {'name': 'John', 'age': 15},
    {'name': 'Brad', 'age': 35},
    {'name': 'Jack', 'age': 45},
    {'name': 'Brandon', 'age': 15},
    {'name': 'Rock', 'age': 5},
]

longer_name = []
max_len_name = 0
list_min_age = []
min_age = 100
mid_age = 0

for element in list_1:
    list_name = len(element.get("name"))
    if list_name == max_len_name:
        longer_name.append(element.get("name"))
    elif list_name > max_len_name:
        longer_name.clear()
        longer_name.append(element.get("name"))
        max_len_name = list_name

for num in list_1:
    list_age = num.get('age')
    if list_age == min_age:
        list_min_age.append(num.get('age'))
    elif list_age < min_age:
        list_min_age.clear()
        list_min_age.append(num.get('age'))
        min_age = list_age
    # print(list_age)
for obj in list_1:
    age = obj.get('age')
    mid_age += age
    middle_age = mid_age/len(list_1)


print(f'The longer name is {longer_name}',
      f'\nThe younger person is {list_min_age}',
      f'\nThe middle age is {middle_age}')




