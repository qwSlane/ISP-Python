import tests.data as data
import unittest
from parsers.core.dumper import Dumper

class TestDumper(unittest.TestCase):

    dmp = Dumper()

    def test_packing_for_functions(self):

        packed = self.dmp.pack(data.func_1)
        self.assertEqual(packed, data.packed_func_1)

    def test_packing_for_classes(self):

        packed = self.dmp.pack(data.Powerful)
        self.assertEqual(packed, data.packed_powerful)

    def test_packing_for_objects(self):

        packed = self.dmp.pack(data.Powerful(1,2))
        self.assertEqual(packed, data.packed_pwfullobj)

    def test_unpacking_for_function(self):

        unpacked = self.dmp.unpack(data.packed_func_1)
        self.assertEqual(unpacked(1,2), data.func_1(1,2))

    def test_unpacking_for_class(self):

        unpacked = self.dmp.unpack(data.packed_powerful)
        unpacked_obj = unpacked(1,2)
        initial_obj = data.Powerful(1,2)
        self.assertEqual(unpacked_obj.a, initial_obj.a)
        self.assertEqual(unpacked_obj.list, initial_obj.list)
        self.assertEqual(unpacked_obj.b, initial_obj.b)
        defierstring = unpacked_obj.defier()
        self.assertEqual(defierstring, 'this is Baza')

    def test_unpacking_for_object(self):

        unpacked = self.dmp.unpack(data.packed_pwfullobj)
        initial_obj = data.Powerful(1,2)

        self.assertEqual(unpacked.a, initial_obj.a)
        self.assertEqual(unpacked.list, initial_obj.list)
        self.assertEqual(unpacked.b, initial_obj.b)
        defierstring = unpacked.defier()
        self.assertEqual(defierstring, 'this is Baza')

# if __name__ == '__main__':
#     unittest.main()