from src.objective.cat import Cat
from src.objective.dog import Dog


class Student(object):
    age = "100岁"



    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)
bart.print_score()

cat = Cat()

s = Student('Bart Simpson', 59)
print(s.age)

print(Student.age)