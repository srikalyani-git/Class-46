from abc import ABC, abstractmethod
class c1(ABC):
    def move(self):
        pass

class human(c1):
    def move(self):
        print("I am a human")

class snake(c1):
    def move(self):
        print("I am a snake")

class bird(c1):
    def move(self):
        print("I am a bird")

class dog(c1):
    def move(self):
        print("i am a dog")

obh = human()
obs = snake()
obb = bird()
obd = dog()
obh.move()
obs.move()
obb.move()
obd.move()