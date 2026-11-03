# turtle 迷宫：画一个方形螺旋迷宫，再让小海龟走到中心
import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)

# 画迷宫墙：每走一段就左转 90 度，边越来越短，形成螺旋
wall_length = 300
while wall_length > 20:
    pen.forward(wall_length)
    pen.left(90)
    wall_length = wall_length - 15

# 小海龟从入口走进迷宫中心
walker = turtle.Turtle()
walker.shape("turtle")
walker.color("green")
walker.penup()
walker.goto(150, 150)
walker.write("终点", align="center", font=("Arial", 14, "normal"))
walker.goto(0, 0)

turtle.done()
