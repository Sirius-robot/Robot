import threading
def work():
  print "Doing work!"
def printit():
  threading.Timer(0.04, work).start()
  threading.Timer(0.04, printit).start()

printit()

