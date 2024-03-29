import sys
from StringIO import StringIO

def autotester(student_code, test_code):
  student_output = StringIO()
  sys.stdout = student_output
  exec student_code
  sys.stdout = sys.__stdout__
  
  
  test_output = StringIO()
  sys.stdout = test_output
  exec test_code
  sys.stdout = sys.__stdout__
  
  print student_output.getvalue()
  print test_output.getvalue()
  # test_code is just the expected output
  if (student_output.getvalue()==test_output.getvalue()):
     return True
  return False