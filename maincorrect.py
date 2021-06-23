#maincode.py has some bugs so use this one this works fine everytime.
from random import *
from time import *
global pwin
global awin
pwin = False
awin = False
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
print("wlcome to tic-tac-toe (level : google impossible) made by an idiot")
print("choose a slot for eg. to enter a mark on s1 position type s1")
#move 1

while True:
    print(" s1 s2 s3 \n s4 s5 s6 \n s7 s8 s9 ")
    inp = input("enter slot")
    if inp == "s1" and s1 == 0:
        s1 = 1
        break
    elif inp == "s2" and s2 == 0:
        s2 = 1
        break
    elif inp == "s3" and s3 == 0:
        s3 = 1
        break
    elif inp == "s4" and s4 == 0:
        s4 = 1
        break
    elif inp == "s5" and s5 == 0:
        s5 = 1
        break
    elif inp == "s6" and s6 == 0:
        s6 = 1
        break
    elif inp == "s7" and s7 == 0:
        s7 = 1
        break
    elif inp == "s8" and s8 == 0:
        s8 = 1
        break
    elif inp == "s9" and s9 == 0:
        s9 = 1
        break
    else:
        print("invalid move pls try again")
print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)

#move 2
while True:
    if s5 == 0:
        s5 = 2
        break
    elif s5 == 1:
        s9 = 2
        break
    aimove = randrange(1,9)
    if aimove == 1 and s1 == 0:
        s1 = 2
        break
    elif aimove == 2 and s2 == 0:
        s2 = 2
        break
    elif aimove == 3 and s3 == 0:
        s3 = 2
        break
    elif aimove == 4 and s4 == 0:
        s4 = 2
        break
    elif aimove == 5 and s5 == 0:
        s5 = 2
        break
    elif aimove == 6 and s6 == 0:
        s6 = 2
        break
    elif aimove == 7 and s7 == 0:
        s7 = 2
        break
    elif aimove == 8 and s8 == 0:
        s8 = 2
        break
    elif aimove == 9 and s9 == 0:
        s9 = 2
        break
    else:
        continue
print("all slots having 1 are X and 2 are O,empty slots are represented by 0")
print("---------------")
#move 3
while True:
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
    inp = input("enter slot")
    if inp == "s1" and s1 == 0:
        s1 = 1
        break
    elif inp == "s2" and s2 == 0:
        s2 = 1
        break
    elif inp == "s3" and s3 == 0:
        s3 = 1
        break
    elif inp == "s4" and s4 == 0:
        s4 = 1
        break
    elif inp == "s5" and s5 == 0:
        s5 = 1
        break
    elif inp == "s6" and s6 == 0:
        s6 = 1
        break
    elif inp == "s7" and s7 == 0:
        s7 = 1
        break
    elif inp == "s8" and s8 == 0:
        s8 = 1
        break
    elif inp == "s9" and s9 == 0:
        s9 = 1
        break
    else:
        print("invalid move pls try again")
print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
#move 4
while True:
    if s5 == 1 and s9 == 2 and s1 == 1:
        s3 = 2
        break
    if s1 == 2 and s2 == 2 and s3 == 0:
        s3 = 2
        break
    elif s1 == 2 and s3 == 2 and s2 == 0:
        s2 = 2
        break
    elif s3 == 2 and s2 == 2 and s1 == 0:
        s1 = 2
        break
    elif s4 == 2 and s5 == 2 and s6 == 0:
        s6 = 2
        break
    elif s4 == 2 and s6 == 2 and s5 == 0:
        s5 = 2
        break
    elif s6 == 2 and s5 == 2 and s4 == 0:
        s4 = 2
        break
    elif s7 == 2 and s8 == 2 and s9 == 0:
        s9 = 2
        break
    elif s7 == 2 and s9 == 2 and s8 == 0:
        s8 = 2
        break
    elif s8 == 2 and s9 == 2 and s7 == 0:
        s7 = 2
        break
##########################################
    elif s1 == 2 and s4 == 2 and s7 == 0:
        s7 = 2
        break
    elif s1 == 2 and s7 == 2 and s4 == 0:
        s4 = 2
        break
    elif s4 == 2 and s7 == 2 and s1 == 0:
        s1 = 2
        break
    elif s2 == 2 and s5 == 2 and s8 == 0:
        s8 = 2
        break
    elif s2 == 2 and s8 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s8 == 2 and s2 == 0:
        s2 = 2
        break
    elif s3 == 2 and s6 == 2 and s9 == 0:
        s9 = 2
        break

    elif s3 == 2 and s9 == 2 and s6 == 0:
        s6 = 2
        break
    elif s6 == 2 and s9 == 2 and s3 == 0:
        s3 = 2
        break
#################################################
    elif s1 == 2 and s5 == 2 and s9 == 0:
        s9 = 2
        break
    elif s1 == 2 and s9 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s9 == 2 and s1 == 0:
        s1 = 2
        break
    elif s3 == 2 and s5 == 2 and s7 == 0:
        s7 = 2
        break
    elif s3 == 2 and s7 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s7 == 2 and s3 == 0:
        s3 = 2
        break
################################################################################################################################
    if s1 == 1 and s2 == 1 and s3 == 0:
        s3 = 2
        break
    elif s1 == 1 and s3 == 1 and s2 == 0:
        s2 = 2
        break
    elif s3 == 1 and s2 == 1 and s1 == 0:
        s1 = 2
        break
    elif s4 == 1 and s5 == 1 and s6 == 0:
        s6 = 2
        break
    elif s4 == 1 and s6 == 1 and s5 == 0:
        s5 = 2
        break
    elif s6 == 1 and s5 == 1 and s4 == 0:
        s4 = 2
        break
    elif s7 == 1 and s8 == 1 and s9 == 0:
        s9 = 2
        break
    elif s7 == 1 and s9 == 1 and s8 == 0:
        s8 = 2
        break
    elif s8 == 1 and s9 == 1 and s7 == 0:
        s7 = 2
        break
##########################################
    elif s1 == 1 and s4 == 1 and s7 == 0:
        s7 = 2
        break
    elif s1 == 1 and s7 == 1 and s4 == 0:
        s4 = 2
        break
    elif s4 == 1 and s7 == 1 and s1 == 0:
        s1 = 2
        break
    elif s2 == 1 and s5 == 1 and s8 == 0:
        s8 = 2
        break
    elif s2 == 1 and s8 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s8 == 1 and s2 == 0:
        s2 = 2
        break
    elif s3 == 1 and s6 == 1 and s9 == 0:
        s9 = 2
        break
    elif s3 == 1 and s9 == 1 and s6 == 0:
        s6 = 2
        break
    elif s6 == 1 and s9 == 1 and s3 == 0:
        s3 = 2
        break
#################################################
    elif s1 == 1 and s5 == 1 and s9 == 0:
        s9 = 2
        break
    elif s1 == 1 and s9 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s9 == 1 and s1 == 0:
        s1 = 2
        break
    elif s3 == 1 and s5 == 1 and s7 == 0:
        s7 = 2
        break
    elif s3 == 1 and s7 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s7 == 1 and s3 == 0:
        s3 = 2
        break

    aimove = randrange(1,9)
    if aimove == 1 and s1 == 0:
        s1 = 2
        break
    elif aimove == 2 and s2 == 0:
        s2 = 2
        break
    elif aimove == 3 and s3 == 0:
        s3 = 2
        break
    elif aimove == 4 and s4 == 0:
        s4 = 2
        break
    elif aimove == 5 and s5 == 0:
        s5 = 2
        break
    elif aimove == 6 and s6 == 0:
        s6 = 2
        break
    elif aimove == 7 and s7 == 0:
        s7 = 2
        break
    elif aimove == 8 and s8 == 0:
        s8 = 2
        break
    elif aimove == 9 and s9 == 0:
        s9 = 2
        break
    else:
        continue
print("---------------")
#move 5 
while True:

    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
    inp = input("enter slot")
    if inp == "s1" and s1 == 0:
        s1 = 1
        break
    elif inp == "s2" and s2 == 0:
        s2 = 1
        break
    elif inp == "s3" and s3 == 0:
        s3 = 1
        break
    elif inp == "s4" and s4 == 0:
        s4 = 1
        break
    elif inp == "s5" and s5 == 0:
        s5 = 1
        break
    elif inp == "s6" and s6 == 0:
        s6 = 1
        break
    elif inp == "s7" and s7 == 0:
        s7 = 1
        break
    elif inp == "s8" and s8 == 0:
        s8 = 1
        break
    elif inp == "s9" and s9 == 0:
        s9 = 1
        break
    else:
        print("invalid move pls try again")

if s1 == 1 and s2 == 1 and s3 == 1:

    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif s7 == 1 and s8 == 1 and s9 == 1:
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif s4 == 1 and s5 == 1 and s6 == 1:
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)

elif ((s1 == 1 and s4 == 1 and s7 == 1) or (s2 == 1 and s5 == 1 and s8 == 1) or (s3 == 1 and s6 == 1 and s9 == 1)):    
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif ((s1 == 1 and s5 == 1 and s9 == 1) or (s3 == 1 and s5 == 1 and s7 == 1)):   
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
else:
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)


#move 6
while pwin != True:
    if s1 == 2 and s2 == 2 and s3 == 0:
        s3 = 2
        break
    elif s1 == 2 and s3 == 2 and s2 == 0:
        s2 = 2
        break
    elif s3 == 2 and s2 == 2 and s1 == 0:
        s1 = 2
        break
    elif s4 == 2 and s5 == 2 and s6 == 0:
        s6 = 2
        break
    elif s4 == 2 and s6 == 2 and s5 == 0:
        s5 = 2
        break
    elif s6 == 2 and s5 == 2 and s4 == 0:
        s4 = 2
        break
    elif s7 == 2 and s8 == 2 and s9 == 0:
        s9 = 2
        break
    elif s7 == 2 and s9 == 2 and s8 == 0:
        s8 = 2
        break
    elif s8 == 2 and s9 == 2 and s7 == 0:
        s7 = 2
        break
##########################################
    elif s1 == 2 and s4 == 2 and s7 == 0:
        s7 = 2
        break
    elif s1 == 2 and s7 == 2 and s4 == 0:
        s4 = 2
        break
    elif s4 == 2 and s7 == 2 and s1 == 0:
        s1 = 2
        break
    elif s2 == 2 and s5 == 2 and s8 == 0:
        s8 = 2
        break
    elif s2 == 2 and s8 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s8 == 2 and s2 == 0:
        s2 = 2
        break
    elif s3 == 2 and s6 == 2 and s9 == 0:
        s9 = 2
        break
    elif s3 == 2 and s9 == 2 and s6 == 0:
        s6 = 2
        break
    elif s6 == 2 and s9 == 2 and s2 == 0:
        s2 = 2
        break
#################################################
    elif s1 == 2 and s5 == 2 and s9 == 0:
        s9 = 2
        break
    elif s1 == 2 and s9 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s9 == 2 and s1 == 0:
        s1 = 2
        break
    elif s3 == 2 and s5 == 2 and s7 == 0:
        s7 = 2
        break
    elif s3 == 2 and s7 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s7 == 2 and s3 == 0:
        s3 = 2
        break
############################################################
    if s1 == 1 and s2 == 1 and s3 == 0:
        s3 = 2
        break
    elif s1 == 1 and s3 == 1 and s2 == 0:
        s2 = 2
        break
    elif s3 == 1 and s2 == 1 and s1 == 0:
        s1 = 2
        break
    elif s4 == 1 and s5 == 1 and s6 == 0:
        s6 = 2
        break
    elif s4 == 1 and s6 == 1 and s5 == 0:
        s5 = 2
        break
    elif s6 == 1 and s5 == 1 and s4 == 0:
        s4 = 2
        break
    elif s7 == 1 and s8 == 1 and s9 == 0:
        s9 = 2
        break
    elif s7 == 1 and s9 == 1 and s8 == 0:
        s8 = 2
        break
    elif s8 == 1 and s9 == 1 and s7 == 0:
        s7 = 2
        break
##########################################
    elif s1 == 1 and s4 == 1 and s7 == 0:
        s7 = 2
        break
    elif s1 == 1 and s7 == 1 and s4 == 0:
        s4 = 2
        break
    elif s4 == 1 and s7 == 1 and s1 == 0:
        s1 = 2
        break
    elif s2 == 1 and s5 == 1 and s8 == 0:
        s8 = 2
        break
    elif s2 == 1 and s8 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s8 == 1 and s2 == 0:
        s2 = 2
        break
    elif s3 == 1 and s6 == 1 and s9 == 0:
        s9 = 2
        break
    elif s3 == 1 and s9 == 1 and s6 == 0:
        s6 = 2
        break
    elif s6 == 1 and s9 == 1 and s2 == 0:
        s2 = 2
        break
#################################################
    elif s1 == 1 and s5 == 1 and s9 == 0:
        s9 = 2
        break
    elif s1 == 1 and s9 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s9 == 1 and s1 == 0:
        s1 = 2
        break
    elif s3 == 1 and s5 == 1 and s7 == 0:
        s7 = 2
        break
    elif s3 == 1 and s7 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s7 == 1 and s3 == 0:
        s3 = 2
        break

    aimove = randrange(1,9)
    if aimove == 1 and s1 == 0:
        s1 = 2
        break
    elif aimove == 2 and s2 == 0:
        s2 = 2
        break
    elif aimove == 3 and s3 == 0:
        s3 = 2
        break
    elif aimove == 4 and s4 == 0:
        s4 = 2
        break
    elif aimove == 5 and s5 == 0:
        s5 = 2
        break
    elif aimove == 6 and s6 == 0:
        s6 = 2
        break
    elif aimove == 7 and s7 == 0:
        s7 = 2
        break
    elif aimove == 8 and s8 == 0:
        s8 = 2
        break
    elif aimove == 9 and s9 == 0:
        s9 = 2
        break
    else:
        continue
if pwin != True:
    print("----------------------------")


if (s1 == 2 and s2 == 2 and s3 == 2) or (s4 == 2 and s5 == 2 and s6 == 2) or (s7 == 2 and s8 == 2 and s9 == 2) and pwin != True:

    awin = True
    print("i win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif (s1== 2 and s4 == 2 and s7 == 2) or (s2 == 2 and s5 == 2 and s8 == 2) or (s3 == 2 and s6 == 2 and s9 == 2)and pwin != True:
    awin = True
    print("i win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif (s1 == 2 and s5 == 2 and s9 == 2) or (s3 == 2 and s5 == 2 and s7 == 2)and pwin != True:
    awin = True
    print("i win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)


#move 7
while awin != True and pwin != True:


    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
    inp = input("enter slot")
    if inp == "s1" and s1 == 0:
        s1 = 1
        break
    elif inp == "s2" and s2 == 0:
        s2 = 1
        break
    elif inp == "s3" and s3 == 0:
        s3 = 1
        break
    elif inp == "s4" and s4 == 0:
        s4 = 1
        break
    elif inp == "s5" and s5 == 0:
        s5 = 1
        break
    elif inp == "s6" and s6 == 0:
        s6 = 1
        break
    elif inp == "s7" and s7 == 0:
        s7 = 1
        break
    elif inp == "s8" and s8 == 0:
        s8 = 1
        break
    elif inp == "s9" and s9 == 0:
        s9 = 1
        break
    else:
        print("invalid move pls try again")


if s1 == 1 and s2 == 1 and s3 == 1 and pwin != True and awin != True:

    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)

elif s7 == 1 and s8 == 1 and s9 == 1 and pwin != True and awin != True:
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif s4 == 1 and s5 == 1 and s6 == 1 and pwin != True and awin != True:
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)



elif ((s1 == 1 and s4 == 1 and s7 == 1) or (s2 == 1 and s5 == 1 and s8 == 1) or (s3 == 1 and s6 == 1 and s9 == 1)) and pwin != True and awin != True:    
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif ((s1 == 1 and s5 == 1 and s9 == 1) or (s3 == 1 and s5 == 1 and s7 == 1)) and pwin != True and awin != True:   
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif pwin != True and awin != True:
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
    print("---------------------------")

#move 8
while pwin != True:
    if s1 == 2 and s2 == 2 and s3 == 0:
        s3 = 2
        break
    elif s1 == 2 and s3 == 2 and s2 == 0:
        s2 = 2
        break
    elif s3 == 2 and s2 == 2 and s1 == 0:
        s1 = 2
        break
    elif s4 == 2 and s5 == 2 and s6 == 0:
        s6 = 2
        break
    elif s4 == 2 and s6 == 2 and s5 == 0:
        s5 = 2
        break
    elif s6 == 2 and s5 == 2 and s4 == 0:
        s4 = 2
        break
    elif s7 == 2 and s8 == 2 and s9 == 0:
        s9 = 2
        break
    elif s7 == 2 and s9 == 2 and s8 == 0:
        s8 = 2
        break
    elif s8 == 2 and s9 == 2 and s7 == 0:
        s7 = 2
        break
##########################################
    elif s1 == 2 and s4 == 2 and s7 == 0:
        s7 = 2
        break
    elif s1 == 2 and s7 == 2 and s4 == 0:
        s4 = 2
        break
    elif s4 == 2 and s7 == 2 and s1 == 0:
        s1 = 2
        break
    elif s2 == 2 and s5 == 2 and s8 == 0:
        s8 = 2
        break
    elif s2 == 2 and s8 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s8 == 2 and s2 == 0:
        s2 = 2
        break
    elif s3 == 2 and s6 == 2 and s9 == 0:
        s9 = 2
        break
    elif s3 == 2 and s9 == 2 and s6 == 0:
        s6 = 2
        break
    elif s6 == 2 and s9 == 2 and s3 == 0:
        s3 = 2
        break
#################################################
    elif s1 == 2 and s5 == 2 and s9 == 0:
        s9 = 2
        break
    elif s1 == 2 and s9 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s9 == 2 and s1 == 0:
        s1 = 2
        break
    elif s3 == 2 and s5 == 2 and s7 == 0:
        s7 = 2
        break
    elif s3 == 2 and s7 == 2 and s5 == 0:
        s5 = 2
        break
    elif s5 == 2 and s7 == 2 and s3 == 0:
        s3 = 2
        break
#######################################################################################
    if s1 == 1 and s2 == 1 and s3 == 0:
        s3 = 2
        break
    elif s1 == 1 and s3 == 1 and s2 == 0:
        s2 = 2
        break
    elif s3 == 1 and s2 == 1 and s1 == 0:
        s1 = 2
        break
    elif s4 == 1 and s5 == 1 and s6 == 0:
        s6 = 2
        break
    elif s4 == 1 and s6 == 1 and s5 == 0:
        s5 = 2
        break
    elif s6 == 1 and s5 == 1 and s4 == 0:
        s4 = 2
        break
    elif s7 == 1 and s8 == 1 and s9 == 0:
        s9 = 2
        break
    elif s7 == 1 and s9 == 1 and s8 == 0:
        s8 = 2
        break
    elif s8 == 1 and s9 == 1 and s7 == 0:
        s7 = 2
        break
##########################################
    elif s1 == 1 and s4 == 1 and s7 == 0:
        s7 = 2
        break
    elif s1 == 1 and s7 == 1 and s4 == 0:
        s4 = 2
        break
    elif s4 == 1 and s7 == 1 and s1 == 0:
        s1 = 2
        break
    elif s2 == 1 and s5 == 1 and s8 == 0:
        s8 = 2
        break
    elif s2 == 1 and s8 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s8 == 1 and s2 == 0:
        s2 = 2
        break
    elif s3 == 1 and s6 == 1 and s9 == 0:
        s9 = 2
        break
    elif s3 == 1 and s9 == 1 and s6 == 0:
        s6 = 2
        break
    elif s6 == 1 and s9 == 1 and s2 == 0:
        s2 = 2
        break
#################################################
    elif s1 == 1 and s5 == 1 and s9 == 0:
        s9 = 2
        break
    elif s1 == 1 and s9 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s9 == 1 and s1 == 0:
        s1 = 2
        break
    elif s3 == 1 and s5 == 1 and s7 == 0:
        s7 = 2
        break
    elif s3 == 1 and s7 == 1 and s5 == 0:
        s5 = 2
        break
    elif s5 == 1 and s7 == 1 and s3 == 0:
        s3 = 2
        break

    aimove = randrange(1,9)
    if aimove == 1 and s1 == 0:
        s1 = 2
        break
    elif aimove == 2 and s2 == 0:
        s2 = 2
        break
    elif aimove == 3 and s3 == 0:
        s3 = 2
        break
    elif aimove == 4 and s4 == 0:
        s4 = 2
        break
    elif aimove == 5 and s5 == 0:
        s5 = 2
        break
    elif aimove == 6 and s6 == 0:
        s6 = 2
        break
    elif aimove == 7 and s7 == 0:
        s7 = 2
        break
    elif aimove == 8 and s8 == 0:
        s8 = 2
        break
    elif aimove == 9 and s9 == 0:
        s9 = 2
        break
    else:
        continue
    print("my move:")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)

if (s1 == 2 and s2 == 2 and s3 == 2) or (s4 == 2 and s5 == 2 and s6 == 2) or (s7 == 2 and s8 == 2 and s9 == 2) and pwin != True and awin != True:

    awin = True
    print("i win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif (s1== 2 and s4 == 2 and s7 == 2) or (s2 == 2 and s5 == 2 and s8 == 2) or (s3 == 2 and s6 == 2 and s9 == 2) and pwin != True and awin != True:
    awin = True
    print("i win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif (s1 == 2 and s5 == 2 and s9 == 2) or (s3 == 2 and s5 == 2 and s7 == 2) and pwin != True and awin != True:
    awin = True
    print("i win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif pwin != True and awin != True:
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)


#move 9
while awin != True and pwin != True:


    inp = input("enter slot")
    if inp == "s1" and s1 == 0:
        s1 = 1
        break
    elif inp == "s2" and s2 == 0:
        s2 = 1
        break
    elif inp == "s3" and s3 == 0:
        s3 = 1
        break
    elif inp == "s4" and s4 == 0:
        s4 = 1
        break
    elif inp == "s5" and s5 == 0:
        s5 = 1
        break
    elif inp == "s6" and s6 == 0:
        s6 = 1
        break
    elif inp == "s7" and s7 == 0:
        s7 = 1
        break
    elif inp == "s8" and s8 == 0:
        s8 = 1
        break
    elif inp == "s9" and s9 == 0:
        s9 = 1
        break
    else:
        print("invalid move pls try again")

if s1 == 1 and s2 == 1 and s3 == 1  and pwin != True and awin != True:

    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif s7 == 1 and s8 == 1 and s9 == 1 and pwin != True and awin != True:
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif s4 == 1 and s5 == 1 and s6 == 1 and pwin != True and awin != True:
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)


elif ((s1 == 1 and s4 == 1 and s7 == 1) or (s2 == 1 and s5 == 1 and s8 == 1) or (s3 == 1 and s6 == 1 and s9 == 1)) and pwin != True and awin != True:    
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif ((s1 == 1 and s5 == 1 and s9 == 1) or (s3 == 1 and s5 == 1 and s7 == 1)) and pwin != True and awin != True:   
    pwin = True
    print("you win!!")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif pwin != True and awin != True:
    print("tie")
    print(" ",s1,s2,s3,"\n ",s4,s5,s6,"\n ",s7,s8,s9)
elif pwin == True:
    print("but...")
    sleep(5)
    print("can you beat me without choosing 5 (or you cant do that )")
    a = input("challange accecpted??(y/n)")
