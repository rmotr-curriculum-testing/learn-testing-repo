import unittest


class FirstAssignmentTestCase(unittest.TestCase):
    def test_hello_world_function(self):
        "Should return the string 'Hello World'"
        self.assertEqual(hello_world(), "Hello World")
