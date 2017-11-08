import unittest


class TestA(unittest.TestCase):
    def test_one(self):
        a = B()
        self.assertEqual(a.value, 42)


class B():
    value = 42

    def get_value(self):
        return self.value


def get_sum(self, num):
    return self.get_value() + num


def get_string(self, string='Hello World!'):
        return string


if __name__ == '__main__':
    unittest.main()
