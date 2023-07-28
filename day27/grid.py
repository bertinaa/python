import tkinter
FONT = ("Arial",24,"bold")

window = tkinter.Tk() #similar to Screen on turtle module
window.title("GUI Interactions with tkinter")
window.minsize(width=500, height=300)
window.config(padx=10,pady=10) #padding

label = tkinter.Label(text="I am a Label",font=FONT)
label.grid(row=0,column=0)
label["text"] = "New Text" #changes text on screen from I am a label to New text
label.config(text="Hello") #changes text on screen frm New text to hello


def button_clicked():
    text_on_screen = input.get()
    label.config(text=text_on_screen)
#creating button1
button = tkinter.Button(text="Click me",command=button_clicked)
button.grid(row=1,column=1)

#creating button2
button1 = tkinter.Button(text="Click me",command=button_clicked)
button1.grid(row=0,column=2)



#entry
input = tkinter.Entry(width=10)
input.grid(row=2,column=3)
# input.get() #returns input as string





window.mainloop() #Similar to exitonclick(), keeps the window open
