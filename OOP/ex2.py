class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        print("init " + str(self))
        self.x = x
        self.y = y

    def __del__(self):
        print("fin " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 5)
print(pt.__dict__)
