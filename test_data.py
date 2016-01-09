import unittest

class TestCaseExample(unittest.TestCase):
    def test_speed(self):
        return True

    def test_failure(self):
        self.assertTrue(True)
