import unittest
from models.base import Base

class TestBaseInstantiation(unittest.TestCase):
    """The Unittests for testing instantiation of the Base class."""

    def test_without_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_the_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_of_id_passed(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_under_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_with_id_or_none(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public_getter(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_under_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_under_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_in_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_in_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_in_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_for_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_with_the_ava_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_in_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_in_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_with_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_under_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearr_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_in_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_under_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_under_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_between_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == '__main__':
    unittest.main()

