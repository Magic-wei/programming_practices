# /usr/bin/python3
# -*- code = utf-8 -*-

# class and instance

class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s\'s score is %.2f'%(self.name, self.score))

wang = Student('wang',90.0)
Lee = Student('Lee',75.0)

wang.print_score()
Lee.print_score()

# python class is dynamic, which means that you can add more attributes to its instance:

wang.age = 18
print(wang.age) # you can find age attribute, for you have just added it

print('you will receive an error under this line, it\'s OK.')
print(Lee.age) # you cannot find age attribute, because it is not a default attribute and you didn't add one.
