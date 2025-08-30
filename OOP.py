# -----------------

# Q1. Create a class representing anything you like (a Laptop, Book, or even a Superhero!).
#     Add attributes and methods to bring the class to life!
class Laptop:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery 
    
    def run_program(self, program):
        print(f"💻 Running {program} on {self.brand} {self.model}...")
    
    def recharge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"🔋 {self.model} battery recharged to {self.battery}%")


# Q2. Use constructors to initialize each object with unique values.
laptop1 = Laptop("Dell", "XPS 15", 45)
laptop2 = Laptop("HP", "Spectre x360", 25)

laptop1.run_program("Python")
laptop2.recharge(60)


# Q3. Add an inheritance layer to explore polymorphism or encapsulation.
class Gadget:
    def __init__(self, brand):
        self.brand = brand
    
    def turn_on(self):
        print(f"⚡ {self.brand} gadget is powering up.")
    
    def turn_off(self):
        print(f"{self.brand} gadget is shutting down.")


class Laptop(Gadget):  # Inheriting from Gadget
    def __init__(self, brand, model, battery):
        super().__init__(brand)   # call parent constructor
        self.model = model
        self.__battery = battery  # private attribute (encapsulation)
    
    def run_program(self, program):
        print(f"🖥️ {self.brand} {self.model} is opening {program}...")
    
    def recharge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"🔌 Charging {self.model}... Battery at {self.__battery}%")


# Test Laptop with inheritance
laptop3 = Laptop("Apple", "MacBook Pro", 35)
laptop3.turn_on()

laptop3.run_program("Xcode")
laptop3.recharge(50)
laptop3.turn_off()



# Q4. Create a program that includes animals with the same action (move()).
#     Each animal should define move() differently with meaningful actions.
class Animal:
    def move(self):
        print("The animal is moving...")


class Cat(Animal):
    def move(self):
        print("🐈 Cat is gracefully walking on the roof.")


class Horse(Animal):
    def move(self):
        print("🐎 Horse is galloping across the field.")


class Snake(Animal):
    def move(self):
        print("🐍 Snake is slithering silently through the grass.")


# Test polymorphism with animals
animals = [Cat(), Horse(), Snake()]
for a in animals:
    a.move()


# Expected Output:
# 💻 Running Python on Dell XPS 15...
# 🔋 Spectre x360 battery recharged to 85%
# ⚡ Apple gadget is powering up.
# 🖥️ Apple MacBook Pro is opening Xcode...
# 🔌 Charging MacBook Pro... Battery at 85%
# Apple gadget is shutting down.
# 🐈 Cat is gracefully walking on the roof.
# 🐎 Horse is galloping across the field.
# 🐍 Snake is slithering silently through the grass.
