# class Book:
#     def get_info(self):
#         title = input()
#         author = input()
#         year = int(input())
#         return print(f'Название книги: {title}, Автор: {author}, Год издания: {year}')
#
#
# pt = Book()
# pt.get_info()
#
# --------------------------------------------------------------------------------------------------------------------

class Circle:
    def __init__(self):
        self.radius = int(input('__init__: '))

    def get_radius(self):
        print('get_radius: ' + str(self.radius))
        return self.radius

    def set_radius(self):
        new_radius = int(input('set_radius: '))
        self.radius = new_radius
        print('set_radius: ' + str(self.radius))


lp = Circle()

lp.get_radius()
lp.set_radius()
