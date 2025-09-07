import time
import os
import random
import sys

print("I'll now show you a random number, remember it.")
time.sleep(1)
print("if you successfully rewrite it, then you win, else prepare for a consequence")
input("press enter to start")
class level:
  def __init__(self,delay):
    self.delay=delay
  def play(self):
    random_int = random.randint(11111,1111111)
    print(random_int)
    time.sleep(self.delay)
    os.system("clear")
    answer=int(input("what was the number? \n"))
    if answer == random_int:
      print("hurray")
      time.sleep(2)
    else: print("fuck youuuuuu")
    sys.exit()
    end
print("level 1")
time.sleep(2)
level(2).play()
print("level 2")
time.sleep(2)
level(1).play()
print("level 3")
time.sleep(2)
level(0.4).play()

