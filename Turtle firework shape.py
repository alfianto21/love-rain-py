import turtle
import random
import time

def draw_love(t, x, y, size, color):

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.left(50)
    t.forward(size)
    t.circle(size * 0.4, 200)
    t.right(140)
    t.circle(size * 0.4, 200)
    t.forward(size)
    t.end_fill()
    t.setheading(0)

def love_rain():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Rain of Love")
    screen.setup(width=800, height=600)

    # Turtle untuk menggambar hati
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Turtle untuk menggambar teks
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.color("purple")
    text_turtle.speed(1)

    hearts = []

    for _ in range(100):  
        x = random.randint(-400, 400)  
        y = random.randint(-300, 600)  
        size = random.randint(10, 30)  
        color = random.choice(["red", "pink", "magenta", "purple", "violet"]) 
        hearts.append({"x": x, "y": y, "size": size, "color": color})

    def animate_text():
        start_x = -400  
        target_x = 0  
        y_position = 50  

        text_turtle.goto(start_x, y_position)
        text_turtle.write("Semangat, Mayy!!", align="center", font=("Times New Roman", 24, "bold"))

        while text_turtle.xcor() < target_x:
            text_turtle.clear()
            start_x += 10
            text_turtle.goto(start_x, y_position)
            text_turtle.write("Semangat, Mayy!!", align="center", font=("Times New Roman", 24, "bold"))
            time.sleep(0.05)

        text_turtle.goto(start_x, y_position - 40)  
        text_turtle.write("Good Night!!", align="center", font=("Times New Roman", 24, "bold"))

    def rain_hearts():
        while True:
            t.clear()
            for heart in hearts:
                draw_love(t, heart["x"], heart["y"], heart["size"], heart["color"])
                heart["y"] -= random.randint(5, 15)  

                if heart["y"] < -300:
                    heart["y"] = random.randint(300, 600)
                    heart["x"] = random.randint(-400, 400)
                    heart["size"] = random.randint(10, 30)
                    heart["color"] = random.choice(["red", "pink", "magenta", "purple", "violet"])

            screen.update()
            time.sleep(0.03)  #

    animate_text()

    rain_hearts()

love_rain()
