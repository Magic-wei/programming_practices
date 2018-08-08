# /usr/bin/python3
# -*- code = utf-8 -*-

# Inheritance_and_polymorphism
## Chinese name: 继承和多态

class Animal(object):
    def run(self):
        print('animal is running!')

class Dog(Animal):
    def run(self):
        print('dog is running!')

class Cat(Animal):
    pass

animal = Animal()
animal.run()
dog = Dog()
dog.run()
cat = Cat() # the same as class Animal, because it doesn't rewrite run() function
cat.run()

# you can use isinstance to verify whether a object is a specific class type:
print(isinstance(dog,Dog))
print(isinstance(dog,Animal)) # dog is from Dog class, also from Animal class!

# for dynamic language, like python, you don't need to import Animal class or its derived class, just import one that have run() method.
def twice_run(animal):
    print('twice_run function is invoked: ')
    animal.run()
    animal.run()

class Timer(object):
    def run(self):
        print('timer start ...')

timer = Timer()
twice_run(timer)

twice_run(dog)
