python.py

class Animal:
    def __init__(self,age,gender):
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"An animal {age}, {gender}"

class Llama (Animal):
    def __init__(self, height, is_domesticated):
        super(Animal, self).__init__(age, gender)
        self.height = height
        self.is_domesticated = is_domesticated

    def __str__(self):
        return f"{super()}"


L = Llama(15, "male", "5cm", True)