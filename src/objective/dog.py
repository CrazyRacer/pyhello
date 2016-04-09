from src.objective.animal import Animal


class Dog(Animal):
    def run(self):
        print('Dog is running....')

    def __init__(self):
        print('Dog is init....')
