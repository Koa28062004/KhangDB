import turtle

t = turtle.Turtle()
t.speed(2)  
t.penup()
t.goto(-400, 0)
t.pendown()
t.color("red")
t.pensize(10) 

def draw_letter(letter):
    t.penup()
    t.forward(20) 
    t.pendown()
    if letter == ' ':
        t.penup()
        t.forward(20)
        t.pendown()
    elif letter == '!':
        t.left(90)
        t.forward(60)
        t.right(90)
    else:
        t.write(letter, font=("Arial", 36, "normal"))
        t.penup()
        t.forward(20) 
        t.pendown()

message = "Happy Birthday Khang!"
for char in message:
    draw_letter(char)

turtle.done()