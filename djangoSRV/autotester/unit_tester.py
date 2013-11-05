import sys
from types import ModuleType
import traceback
import unittest


# pass student code and unit test file
# def autotester(self, student_code, test_code):
def autotester(student_code, unit_test):

    # Changing the format such that you can put your own run code
    # test_code = '''
    # {testModule}.Tester = Tester
    # {testModule}.testResult=unittest.main(module={testModule}, exit=False, verbosity=3)
    # '''
    mockModule = 'm'
    #test_code = student_code + '\n' + unit_test + '\n' + test_code.format(testModule=mockModule)
    test_code = student_code + '\n' + unit_test.format(testModule=mockModule)
    envDict = {mockModule: ModuleType(mockModule)}
    try:
        exec test_code in envDict  #HACK SOLVED FOR NOW
    except:
        print traceback.format_exc()
        return [0,0,0]

    result = envDict['m'].testResult
    return [len(result.errors), len(result.failures), result.testsRun]

if __name__ == "__main__":
	autotester()
