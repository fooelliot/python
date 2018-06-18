

class CarStore(object):
    def __init__(self):
        self.factory = Factory()
    def order(self, tpye):
        return self.factory.select_car_by_car_type(type)
    def __del__(self):
        print("del")
    def __str__(self):
        print("str 对象的描述信息")
    def __new__(cls):
        print(id(cls))
        print("--new method--")
        return object.__new__(cls)


class Factory(object):
    def select_car_by_car_type(self,car_type):
            if car_type == "qiche":
                return Car()
            elif car_type == "benci":
                return Benci()
            elif car_type == "baoma":
                return Baoma()

class Car(object):
    def music(self):
        print("music")
    def stop(self):
        print("stop")
    def move(self):
        print("move")

class Benci(Car):
    pass

class Baoma(Car):
    pass


car_store = CarStore()
# car = car_store.order("baoma")
# car.move()
# car.music()
# car.stop()


print(id(CarStore))










