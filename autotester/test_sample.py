import student_prog
import unittest
'''
	A simple unit test that verifies if the student manage to add the first
	six natural numbers into an array
'''

class Tester(unittest.TestCase):
    def test_1to5(self):
        student_output = student_prog.from1to5()
        self.assertListEqual(student_output, [0, 1, 2, 3, 4, 5])

if __name__ == "__main__":
	unittest.main()