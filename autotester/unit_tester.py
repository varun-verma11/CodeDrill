import sys
from StringIO import StringIO
import unittest

#pass student code and unit test file
#def autotester(self, student_code, test_code):
def autotester():

  student_code = '''
def from1to5():
    ret = []
    for i in range(6):
        ret.append(i)

    return ret
    '''
    
  unit_test = '''
import unittest
class Tester(unittest.TestCase):
    def test_1to5(self):
        stud_output = from1to5()
        self.assertListEqual(stud_output, [0, 1, 2, 3, 4, 5])

#unittest.main()
'''
  test_code = student_code+unit_test
  #exec student_code 
  print test_code
  test_output = StringIO()
  sys.stdout = test_output
  exec test_code in globals() #THIS HACK NEEDS SERIOUS CONSIDERATION
  sys.stdout = sys.__stdout__
  print test_output.getvalue()
  
  # test_code is just the expected output
  failed = "FAILED"
  if (failed in test_output.getvalue()):
    print ("FAIL")
  else:
    print ("PASS")


if __name__ == "__main__":
	autotester()
