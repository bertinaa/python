from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=500) #width, height of the screen, keyword argument
#screen.setup(500,400) positional arguments

#pop up for getting the bet from the user, this works similar to input()
user_bet = screen.textinput(title="Place your bet",prompt="Which turtle do you think is going to win? : ")

tim = Turtle()
tom = Turtle()
ben = Turtle()
gwen = Turtle()
max = Turtle()
ken = Turtle()
lucy = Turtle()
jules = Turtle()

tim.shape("turtle")
tom.shape("turtle")
ben.shape("turtle")
gwen.shape("turtle")
tim.shape("turtle")
tim.shape("turtle")
tim.shape("turtle")
tim.shape("turtle")


tim.goto(-250,200)
tom.goto(-250,150)
ben.goto(-250,50)
gwen.goto(-250,0)
max.goto(-250,-50)
ken.goto(-250,-100)
lucy.goto(-250,-150)
jules.goto(-250,-200)

tim.color("orange")
tom.color("blue")
ben.color("green")
gwen.color("purple")
max.color("red")
ken.color("black")
lucy.color("yellow")
jules.color("pink")

screen.exitonclick()
