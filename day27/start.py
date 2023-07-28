#this code has a label, button and entry and used 'pack'

import tkinter
FONT = ("Arial",24,"bold")

window = tkinter.Tk() #similar to Screen on turtle module
window.title("GUI Interactions with tkinter")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label",font=FONT)
label.pack() #to bring it to the center of the screen by default; bottom, top,center,left, right are also acceptable
label["text"] = "New Text" #changes text on screen from I am a label to New text
label.config(text="Hello") #changes text on screen frm New text to hello


def button_clicked():
    text_on_screen = input.get()
    label.config(text=text_on_screen)
#creating buttons
button = tkinter.Button(text="Click me",command=button_clicked)
button.pack()

#entry
input = tkinter.Entry(width=10)
input.pack()
# input.get() #returns input as string





window.mainloop() #Similar to exitonclick(), keeps the window open
