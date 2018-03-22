class Animal:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def say_hello(self):
        print('{}: {}'.format(self.name, self.voice))


class Cat(Animal):
    def __init__(self, name, voice='Woof'):
        super().__init__(name, voice)

    def climb_tree(self):
        print('{} is climbing'.format(self.name))


class Dog(Animal):
    def __init__(self, name, voice='Miau'):
        super().__init__(name, voice)

    def walk_outside(self):
        print('{} is walking'.format(self.name))


mruczek = Cat('Murczek')
reksio = Dog('Reksio')

mruczek.say_hello()
mruczek.climb_tree()

reksio.say_hello()
reksio.walk_outside()
