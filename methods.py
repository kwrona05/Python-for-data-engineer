class Car:
    def __init__(self, brand, model, course):
        self.brand = brand
        self.model = model
        self.course = course

    def course_add(self, km):
        self.course += km

    def show_info(self):
        return print(f"{self.brand} {self.model} {self.course}")


auto = Car('Toyota', 'Corolla', 100)
auto.show_info()

auto.course_add(150)
auto.show_info()
