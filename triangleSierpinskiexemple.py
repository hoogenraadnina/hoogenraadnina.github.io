import turtle
T = turtle.Turtle() ; T.speed(0)
T.hideturtle()

 

def Sier (n,L):
    if n == 0:
        for i in range (0,3):
            T.fd(L)
            T.left(120)

    if n > 0:
        Sier(n-1,L/2)
        T.fd(L/2)
        Sier(n-1,L/2)
        T.bk(L/2)
        T.left(60)
        T.fd(L/2)
        T.right(60)
        Sier(n-1,L/2)
        T.left(60)
        T.bk(L/2)
        T.right(60)

 

T.penup(); T.goto(-400,-300)
T.pendown() ; T.width()
Sier(4,600)

 
