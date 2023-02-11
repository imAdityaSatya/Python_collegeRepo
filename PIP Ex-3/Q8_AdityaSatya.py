'''
Aditya Satya
Ques 8
Write a python program that plays the popular scissor-rock-paper game.
'''

import random 
scissor=0
rock=1
paper=2
you= int(input("scissor (0), rock (1), paper (2):"))
comp= random.randint(0,2)
if comp==0 and you==0:
   print("The computer is scissor. You are scissor too. It is a draw")
elif comp==1 and you==1:
   print("The computer is rock. You are rock too. It is a draw")
elif comp==2 and you==2:
   print("The computer is paper. You are paper too. It is a draw")
elif comp==0 and you==1:
   print("The computer is scissor. You are rock. You won")
elif comp==0 and you==2:
   print("The computer is scissor. You are paper. You lose")
elif comp==1 and you==0:
   print("The computer is rock. You are scissor. You lose")
elif comp==1 and you==2:
   print("The computer is rock. You are paper. You won")
elif comp==2 and you==0:
   print("The computer is paper. You are scissor. You won")
else:
   print("The computer is paper. You are rock. You lose")
    