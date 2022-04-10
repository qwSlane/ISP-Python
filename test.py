from encodings import utf_8
from importlib import import_module
import inspect
import types

from json_serializer import JsonSerializer
from pprint import pprint

c = 12

class A():

    b =12

class Test():
    lolich = 10
    def __init__(self):
        print('AWAKE!')

class BC(Test):
     
    def adasd(self, a, b):
        return math.sin(a+b+c)


ser = JsonSerializer()

a = ser.load('tt.json')

b = a()
print(b.adasd(1,2))

