class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
print(th2.id, th1.id)
th2.id = 3
print(th2.id, th1.id)
print(th1.__dict__, th2.__dict__)
th1.attr_new = 'new attr'
print(th1.__dict__, th2.__dict__)

# Паттерн Моносостояния. Когда все объекты связаны друг с дургом. изменение в одном и
# значит изменения будут в другом объекте
