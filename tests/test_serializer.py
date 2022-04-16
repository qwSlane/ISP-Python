import unittest
import os
from dump_service import dump, dumps, load, loads
from tests.data import Powerful

class TestSerializer(unittest.TestCase):

    def test_json_dump(self):
        dump('json',Powerful, 'tt.json')
        unpacked = load('json', 'tt.json')
        obj = unpacked(5,5)
        initial = Powerful(5,5)
        self.assertEqual(obj.a, initial.a)
        self.assertEqual(obj.pull(3), initial.pull(3))
        os.remove('tt.json')

    def test_toml_dump(self):
        dump('toml',Powerful, 'tt.toml')
        unpacked = load('toml', 'tt.toml')
        obj = unpacked(5,5)
        initial = Powerful(5,5)
        self.assertEqual(obj.a, initial.a)
        self.assertEqual(obj.pull(3), initial.pull(3))
        os.remove('tt.toml')

    def test_yaml_dump(self):
        dump('yaml', Powerful, 'tt.yaml')
        unpacked = load('yaml', 'tt.yaml')
        obj = unpacked(5,5)
        initial = Powerful(5,5)
        self.assertEqual(obj.a, initial.a)
        self.assertEqual(obj.pull(3), initial.pull(3))
        os.remove('tt.yaml')

    def test_json_tostring(self):    
        string = dumps('json', Powerful)
        unpacked = loads('json', string)
        obj = unpacked(5,5)
        initial = Powerful(5,5)
        self.assertEqual(obj.a, initial.a)
        self.assertEqual(obj.pull(3), initial.pull(3))

    def test_toml_tostring(self):    
        string = dumps('toml', Powerful)
        unpacked = loads('toml', string)
        obj = unpacked(5,5)
        initial = Powerful(5,5)
        self.assertEqual(obj.a, initial.a)
        self.assertEqual(obj.pull(3), initial.pull(3))

    def test_json_tostring(self):    
        string = dumps('yaml', Powerful)
        unpacked = loads('yaml', string)
        obj = unpacked(5,5)
        initial = Powerful(5,5)
        self.assertEqual(obj.a, initial.a)
        self.assertEqual(obj.pull(3), initial.pull(3))

# if __name__ == '__main__':
#     unittest.main()
