class Car:
  total_car = 0


  def __init__(self,brand,model):
   self.__brand=brand
   self.model=model
   Car.total_car+=1

  def  get_brand(self):
   return self.__brand + "!"

  def full_name(self):
   return f"{self.__brand} {self.model}"

  def fuel_type(self):
   return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
      super().__init__(brand,model)
      self.battery_size = battery_size 
    def fuel_type(self):
       return "Electric charge"



my_tesla =ElectricCar("Tesla","model S","85kwh")
#print(my_tesla.__brand)
print(my_tesla.fuel_type())

safari= Car("Tata","Safari")
safariThree=Car("Tata",'Nexon')
print(safari.fuel_type())
print(Car.total_car)

#my_car = Car("Toyota","Corolla")
#print(my_car.brand)
#print(my_car.model)
#print(my_car.full_name())

#my_new_car =Car("Tata","Safari")
#print(my_new_car.model)
#print(my_new_car.brand)

#research a bit about self keyword and init()
#take care of indenattions
#inheritance
#super keyword
#encapsulation 
#__ makes priavte outsie the class
#getter
#setter
#polymorphism