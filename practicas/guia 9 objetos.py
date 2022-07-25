#%%
from random import random


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self,other):
        return abs(self.x - other.get_x()) + abs(self.y - other.get_y())
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_norm(self):
        return (self.x**2 + self.y**2)**0.5
        
    def __repr__(self) -> str:
        return f'Coordinate({self.x}, {self.y})'
    
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a)

    def get_area(self):
        pass

    def __lt__(self,other):
        if self.get_perimeter() > other.get_perimeter():
            return True
        return False
    
c1 = Coordinate(0,0)
c2 = Coordinate(0,0)
c3 = Coordinate(0,0)

triangle1 = Triangle(c1,c2,c3)
triangle1.get_area()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self):
        espacios = self.width -2
        print('*'+'-'*espacios+'*')
        for i in range(self.height-2):
            print('|'+' '*espacios+'|')
        print('*'+'-'*espacios+'*')
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)

    def __lt__(self,other):
        if self.get_perimeter() > other.get_perimeter():
            return True
        return False

    def __eq__(self,other):
        if isinstance(Rectangle,other) and other.get_area() == self.get_area() and other.get_perimeter() == self.get_perimeter():
            return True
        return False


class Interval:
    def __init__(self,start,end,step=1) -> None:
        self.start = start
        self.end = end
        self.step = step
        self.cursor = start

    def get_next(self):
        self.cursor += self.step
        return self.cursor

    def has_next(self):
        if self.cursor + self.step <= self.end:
            return True
        return False

    def set_step(self,step):
        self.step = step

#%%
import random

class Scissor:
    def __init__(self) -> None:
        pass
    def cmp(self,other):
        if isinstance(other,Scissor):
            return 0
        if isinstance(other,Paper):
            return 1
        if isinstance(other,Rock):
            return -1
        
class Rock:
    def __init__(self) -> None:
        pass        

    def cmp(self,other):
        if isinstance(other,Rock):
            return 0
        if isinstance(other,Scissor):
            return 1
        if isinstance(other,Paper):
            return -1

class Paper:
    def __init__(self) -> None:
        pass        
    
    def cmp(self,other):
        if isinstance(other,Paper):
            return 0
        if isinstance(other,Rock):
            return 1
        if isinstance(other,Scissor):
            return -1

def main():
    player = input('> ')
    computer = random.choice((Scissor,Rock,Paper))()
    dic = {'s':Scissor,'r':Rock,'p':Paper}
    player = dic[player]()
    return player.cmp(computer)
# %%


def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

print(rgb_to_hex(255, 165, 1))
