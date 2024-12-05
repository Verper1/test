class Geom:
    name = 'Geom'

    def set_coords(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


    def draw(self):
        print('Рисование Geom')


class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    # def draw(self):
    #     print('Рисование прямоугольника')
    pass


g = Geom()
l = Line()
r = Rect()
# print(l.set_coords(1, 1, 3, 4))
# print(r.set_coords(2, 3, 1, 5))
l.draw()
r.draw()