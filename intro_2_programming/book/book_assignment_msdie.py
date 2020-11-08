# msdie.py
# class definition for an n-sided die

# import from library
from random import randrange

# create class msdie
class MSDie:

# create definition
# first parameter should always be called self i.e status quo.
# 
def __init__(self,sides):
    self.sides = sides
    self.value = 1

def roll(self):
    self.value = randrange(1,self.sides+1)

def getValue(self):
    return self.value

def setValue(self,value):
    self.value = value