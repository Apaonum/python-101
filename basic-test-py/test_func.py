import unittest


def squarefunction(x):
    return x**2


class Testsquarefunc(unittest.TestCase):

    def test_squarefunc(self):
        self.assertEqual(squarefunction(5), 25)
        self.assertEqual(squarefunction(-2), 4)
        self.assertEqual(squarefunction(0), 0)


if __name__ == '__main__':
    unittest.main()

print(squarefunction(15))
