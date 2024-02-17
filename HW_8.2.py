
def find_unique_value(some_list):
    for n in set(some_list):
        if some_list.count(n) == 1:
            return n

# some_list = [5, 5, 5, 2, 2, 0.5]
# print(find_unique_value(some_list))

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

# def find_unique_value(some_list):
#
#     counter = dict()
#
#     for n in some_list:
#         if str(n) in counter:
#             counter[str(n)] = counter[str(n)] + 1
#         else:
#             counter[str(n)] = 1
#
#     for (key, value) in counter.items():
#         if value == 1:
#             return key