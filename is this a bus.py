class vehicle:
    def _init_(self, name, max_speed mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class bus(vehicle):
        pass
school_bus = bus("school volvo", 180, 12)
print("vehicle name:", school_bus.name,"speed:", school_bus.max_screen)