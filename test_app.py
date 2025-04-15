# test_app

import unittest
from app import add,sub

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,4),7)
        self.assertEqual(add(0,0),0)

    def test_sub(self):
        self.assertEqual(sub(-1,-1),0)
        self.assertEqual(sub(2,1),1)

if __name__=="__main__":
    unittest.main()