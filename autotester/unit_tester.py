import sys
# from StringIO import StringIO
from types import ModuleType
import unittest


# pass student code and unit test file
# def autotester(self, student_code, test_code):
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
'''

    #Assumes the testing class to be called tester. for now
    test_code = '''
{testModule}.Tester = Tester
{testModule}.testResult=unittest.main(module={testModule}, exit=False, verbosity=3)
'''
    mockModule = 'm'
    test_code = student_code + unit_test + test_code.format(testModule=mockModule)
    # exec student_code 
    # print test_code
    # test_output = StringIO()
    # sys.stdout = test_output
    envDict = {mockModule: ModuleType(mockModule)}
    try:
        exec test_code in envDict  #HACK SOLVED FOR NOW
    except:
        print "Something wrong happened while executing the test code"

    result = envDict['m'].testResult.result
    print [len(result.errors), len(result.failures), result.testsRun]
    # sys.stdout = sys.__stdout__
    # print test_output.getvalue()
  
    # test_code is just the expected output
    # ifailed = "FAILED"
    # if (failed in test_output.getvalue()):
    #     print ("FAIL")
    # else:
    #     print ("PASS")


if __name__ == "__main__":
	autotester()
