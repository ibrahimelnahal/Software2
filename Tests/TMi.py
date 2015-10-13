__author__ = 'brahimel-nahal'

import unittest
import Main.PMi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Main.PMi.sizelist([1,2,3]), 3)


if __name__ == '__main__':
    unittest.main()
