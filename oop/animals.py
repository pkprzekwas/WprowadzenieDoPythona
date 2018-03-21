class Animal:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting

    def greet(self):
        print('{} says: {}'.format(self.name, self.greeting))


class Dog(Animal):
    def __init__(self, name, greeting):
        super().__init__(name, greeting)

    def hates(self):
        print('{} hates cats.'.format(self.name))


class Cat(Animal):
    def __init__(self, name, greeting):
        super().__init__(name, greeting)

    def hates(self):
        print('{} hates dogs.'.format(self.name))


if __name__ == '__main__':
    max = Dog(name='Max', greeting='Woof')
    max.greet()
    max.hates()

    susie = Dog(name='Susie', greeting='Woofs, Woofs')
    susie.greet()
    susie.hates()

    arnold = Cat(name='Arnold', greeting='Meow')
    arnold.greet()
    arnold.hates()
