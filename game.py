
import time
import os
import random
import sys

print("I'll now show you a random number, remember it.")
time.sleep(1)
print("if you successfully rewrite it, then you win, else prepare for a consequence")
input("press enter to start")
os_platform = sys.platform
if os_platform.startswith('win'):
    print("Running on Windows.")
elif os_platform == 'linux':
    print("Running on Linux.")
elif os_platform == 'darwin':
    print("Running on macOS.")
else:
    print("Running on an unknown OS.Your OS may not be supported")
class level:
  def __init__(self,delay):
    self.delay=delay
  def play(self):
    random_int = random.randint(11111,1111111)
    print(random_int)
    time.sleep(self.delay)
    if os_platform.startswith('win'):
        os.system("cls")
    else:
        os.system("clear")
     

    answer=int(input("what was the number? \n"))
    if answer == random_int:
      print("hurray")
      time.sleep(2)
    else: 
        print("fuck youuuuuu")
        sys.exit()
        
print("level 1")
time.sleep(2)
level(2).play()
print("level 2")
time.sleep(2)
level(1).play()
print("level 3")
time.sleep(2)
level(1).play()

print("you have finished all rounds, congrats..\n")
time.sleep(1.5)
print("would you like to continue to a bonus round? :) (Y/N)")
answer2=input("")
if answer2 == "Y" or "y" or "yes" or "yup" or "yeah":
   print("hehehehe")
   level(0.150).play()
else:
   sys.exit()




