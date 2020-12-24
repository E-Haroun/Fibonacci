'''
Created by Haro_un

'''   
def square(T, S):
  for k in range(0,4):
    T.forward(S)
    T.left(90)

def repeat(T, f, N, A, S, k):
  for j in range(0, N):
    f(T, S)
    T.left(A)
    S = k*S

import turtle
my_window = turtle.Screen() 
my_window.bgcolor("black")
#my_window.size("1920*1080")
turtle.Pen().width(800)
turtle.color("#ff5733")
turtle.speed("fastest")     
repeat(turtle, square, 108, 10, 200, 0.97)

exitonclick()
