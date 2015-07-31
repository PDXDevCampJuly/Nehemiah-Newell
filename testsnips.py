def front_times(str, n):
  capturedString = list(str)[0:3]
  returnString = ""
  for thisCount in range(n):
    returnString += "".join(capturedString)
  return "".join(returnString)

def string_bits(str):
  capturedString = list(str)[::2]
  returnString = "".join(capturedString)
  return returnString

def string_splosion(str):
  capturedString = list(str)
  returnString = ""
  for idx, letter in enumerate(capturedString):
    returnString += "".join(capturedString[:idx])
  returnString +="".join(capturedString)
  return returnString

def a():
  print("this is a")

def b():
  print ("this is b")

lst = [a(), b()] 

print(lst)