import unittest

class Test_TestIncrementDecrement(unit.Testcase):
    def test_increment(self):
        self.assertEqual(4,4)

    def test_decrement(self):
        self.assertEqual(3,4)

if __name == '__main__':
    unittest.main()
