import turtle
import random



screen= turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("black")

#code starts here
t=turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write("Background color",font=("Ariel",30,""),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write("1.Tan",font=("Ariel",20,""),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('azure')
t.write("2.Azure ",font=("Ariel",20,""),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('aquamarine')
t.write("3.Aquamarine",font=("Ariel",20,""),align="left")



t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('Dark khaki')
t.write("4.Dark khaki",font=("Ariel",20,""),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write("Choose a color",font=("Ariel",30,""),align="center")

choice=int(input("Choose a color"))
if choice==1:
    screen.bgcolor('tan')
elif choice==2:
    screen.bgcolor('azure')

elif choice==3:
    screen.bgcolor('aquamarine')

else:
    screen.bgcolor('dark khaki')

t.clear()
#enter your name
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('black')
t.write("Enter Your Name",font=("Ariel",30,""),align="center")


name =input("Enter your name:")
t.clear()
operation= random.randint(1,4)
if operation==1:
    symbol="+"
    #add
    # num1=int(input("Enter a number: "))
    # num2=int(input("Enter another number: "))

    num1=random.randint(-100,100)
    num2=random.randint(-100,100)
    solution = num1 + num2
if operation==2:
    symbol="-"
    #subtract
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    solution = num1 - num2

if operation==3:
    #multiply
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    solution = num1 * num2

elif operation ==4:
    #divide
    symbol="/"
    num1 = random.randint(-10, 10)
    num2 = random.randint(1, 10)
    sign=random.randint(1,2)

    if sign== 2:
        num2= -1+num2
    solution = num1 / num2


t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('blue')
t.write(name,font=("Ariel",30,""),align="center")



t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('red')
t.write(num1,font=("Ariel",30,""),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('green')
t.write(symbol,font=("Ariel",30,""),align="center")


t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('blue')
t.write(num2,font=("Ariel",30,""),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('green')
t.write("=",font=("Ariel",30,""),align="center")
answer=int(input("What is  the answer: "))
t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('purple')
t.write(solution,font=("Ariel",30,""),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write("Your answer: "+str(answer),font=("Ariel",30,""),align="center")



if answer== solution:
    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.pencolor('black')
    t.write("Good job" , font=("Ariel", 30, ""),align="center")

else:
    screen.bgcolor("darkorange")
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.pencolor('black')
    t.write("Wrong", font=("Ariel", 30, ""), align="center")








#always the last line in code
turtle.done()