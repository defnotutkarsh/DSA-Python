class Car :
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Electric(Car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery = battery
my_newcar = Electric("tesla","X","10000000kw")
print(my_newcar.battery)

my_car = Car("maruti","alto")
print(my_car.model)
print(my_car.full_name())
