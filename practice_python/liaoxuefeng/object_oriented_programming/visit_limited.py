# /usr/bin/python3
# -*- code = utf-8 -*-

# visit limited
# add '__' before an attribute's name, like '__name', '__score', you cannot directly visit them
# but for forms like '_name' , you can still directly visit them, which is not recommended.

class Student:
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s\'s score is %.2f'%(self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            print('name must be string!')
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print('input out of range! score must in [0,100]')

Lee = Student('Lee',75.0)
# you cannot change the attribute '__name' directly, but if you do like this, it doesn't work: 
Lee.__name = "wang"
print(Lee.__name)
print(Lee.get_name())
