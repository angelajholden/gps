# Explain how to create and cause an exception to occur while running your code. This exception should NOT be the result of such internal runtime errors such as dividing by zero, indexing out of bounds, and so forth.

def my_func()
  one()

def one():
  two()

def two():
  three()

def three():
  try:
    four()
  except MyException:
    # execute if the MyException message happened

def four()
  # processing code
  if something_special_happened:
    raise MyException

