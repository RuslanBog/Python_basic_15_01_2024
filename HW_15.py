# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             new_width = self.width + other.width
#             new_height = self.height + other.height
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for +: Rectangle and {}".format(type(other)))
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_width = self.width * n
#             new_height = self.height * n
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for *: Rectangle and {}".format(type(n)))
#
#     def __str__(self):
#         return f'Rectangle: width={self.width}, height={self.height}'
#
#
# # Тестування
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
####################
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             new_width = self.width + other.width
#             new_height = self.height + other.height
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for +: Rectangle and {}".format(type(other)))
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_width = self.width * n
#             new_height = self.height * n
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for *: Rectangle and {}".format(type(n)))
#
#     def __str__(self):
#         return f'Rectangle: width={self.width}, height={self.height}'
#
#
# # Тестування
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
####
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             new_width = max(self.width, other.width)
#             new_height = self.height + other.height
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for +: Rectangle and {}".format(type(other)))
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_width = self.width * n
#             new_height = self.height * n
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for *: Rectangle and {}".format(type(n)))
#
#     def __str__(self):
#         return f'Rectangle: width={self.width}, height={self.height}'
#
#
# # Тестування
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'

# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'

############################################
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             new_width = max(self.width, other.width)
#             new_height = self.height + other.height
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for +: Rectangle and {}".format(type(other)))
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_width = self.width * n
#             new_height = self.height * n
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for *: Rectangle and {}".format(type(n)))
#
#     def __str__(self):
#         return f'Rectangle: width={self.width}, height={self.height}'
#
#
# # Тестування
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
# ################################

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             new_width = max(self.width, other.width)
#             new_height = self.height + other.height
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for +: Rectangle and {}".format(type(other)))
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_width = self.width * n
#             new_height = self.height * n
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for *: Rectangle and {}".format(type(n)))
#
#     def __str__(self):
#         return f'Rectangle: width={self.width}, height={self.height}'
#
#
# # Тестування
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 24, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
##################################
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             new_width = max(self.width, other.width)
#             new_height = self.height + other.height
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for +: Rectangle and {}".format(type(other)))
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_width = self.width * n
#             new_height = self.height * n
#             return Rectangle(new_width, new_height)
#         raise ValueError("Unsupported operand type for *: Rectangle and {}".format(type(n)))
#
#     def __str__(self):
#         return f'Rectangle: width={self.width}, height={self.height}'
#
#
# # Тестування
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 30, 'Test3'
#
# # r4 = r1 * 4
# # assert r4.get_square() == 32, 'Test4'
#

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            # return self.get_square() + other.get_square()
        # return False
            new_width = max(self.width, other.width)
            new_height = self.height + other.height
            return Rectangle(new_width, new_height)
        raise ValueError("Unsupported operand type for +: Rectangle and {}".format(type(other)))

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_width = self.width * n
            new_height = self.height * n
            return Rectangle(new_width, new_height)
        raise ValueError("Unsupported operand type for *: Rectangle and {}".format(type(n)))

    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'


# Тестування
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

print(r1)
print(r2)
print(r3)