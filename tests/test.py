import unittest


class FoobarTest(unittest.TestCase):

    def setUp(self):
        self.foo = 'foo'

    def test_foobar_success(self):
        self.assertEqual(self.foo, 'foo')


if __name__ == '__main__':
    unittest.main()
