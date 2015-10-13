__author__ = 'ibrahimelnahal'

import unittest
import Main.PMi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Main.PMi.sizelist([2,3,4]), 3)


if __name__ == '__main__':
    unittest.main()
