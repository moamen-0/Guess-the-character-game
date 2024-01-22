import random
import turtle

jim = turtle.Turtle() #Remember the capital T
jim.speed(0.2) #A speed of 0 makes him go as fast as possible

arm_length = 100 #Change these if you want
leg_length = 120

def reset(): #reset sends him back to the center
    jim.pu() #pu is short for penup. Either work, you can use them interchangeably
    jim.setpos(0,0)
    jim.pd() #pd is short for pendown

def head():
  reset()
  jim.seth(90) #seth is short for set_heading, and it changes the direction jim is facing.
  jim.fd(30)
  jim.rt(90)
  jim.circle(50)

def arm1():
    reset()
    jim.seth(160)
    jim.fd(arm_length/2)
    jim.rt(20)
    jim.fd(arm_length/2)

def arm2():
    reset()
    jim.seth(20)
    jim.fd(arm_length/2)
    jim.lt(20)
    jim.fd(arm_length/2)

def leg1():
    reset()
    jim.seth(270)
    jim.fd(50)
    jim.seth(230)
    jim.fd(leg_length/2)
    jim.lt(40)
    jim.fd(leg_length/2)

def leg2():
    reset()
    jim.seth(270)
    jim.fd(50)
    jim.seth(310)
    jim.fd(leg_length/2)
    jim.rt(40)
    jim.fd(leg_length/2)

ScoreBoard={}

easy=["apple","banana","strawberry","mango","orange","grape"]
medium=["egypt","usa","canada","tunisia","morocco","italy","germany"]
hard=["array","function","class","loop","datastructure","algorithm"]

def play():
    
    name=input("Enter your name : ")
    if name not in ScoreBoard:
        ScoreBoard[name] =0

    level=input("select level [ easy , medium , hard ] : ")
    
    if level == "easy":
        score=1
        #failed=5
        print("!!  Fruits  !!") 
        wordGenerator(level,score,name)
          
    elif level == "medium":
        score=2
        #failed=4
        print("!!  Countries  !!")
        wordGenerator(level,score,name)
                 
    elif level == "hard":
        score=3
        #failed=3
        print("!!  Programming  !!")
        wordGenerator(level,score,name)

    new_game()

def wordGenerator(level,score,name):
    failed=5
    x=''
    if level=="easy":
        word=random.choice(easy)
    if level=="medium":
        word=random.choice(medium)
    if level=="hard":
        word=random.choice(hard)

    #word=random.choice(level)
    wordlist=list(word)
    success=len(wordlist)
    ans='-'*len(wordlist)
    anslist=list(ans)

    while failed>0 and success>0:
        char=input("Guess the character : ")
        if char in wordlist:
            success-=1
            anslist[wordlist.index(char)]=char
            print(anslist)
            wordlist[wordlist.index(char)]=0
        else :
            x=x+'X'
            print("wrong character     ",x,"  ",failed-1," attemps remaining " )
            if (failed ==5) :
                head()
            elif(failed==4):
                arm1()
            elif(failed ==3):
                arm2()
            elif(failed ==2):
                leg1()
            elif(failed ==1):
                leg2()
            failed-=1
            
    if success==0:
        ScoreBoard[name] += score
        turtle.clearscreen()
    else:
        print ("The word was",word)
        turtle.clearscreen()
        
def new_game():
 start=input("1-play\n2-scoreboard\n3-exit\n")
 if start=="1":
     play()
 elif start=="2":
     print(ScoreBoard)
     new_game()
 elif start=="3":
     exit()

new_game()