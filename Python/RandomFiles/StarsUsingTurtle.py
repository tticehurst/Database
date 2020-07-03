import turtle

def main():
    count = 1
    turtle.reset()
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.penup()
    turtle.setposition(-150,80)
    turtle.pendown()
    while count <= 5:
        turtle.forward(300)
        turtle.right(144)
        count = count + 1
    turtle.exitonclick()

if __name__ == "__main__":
    main()
