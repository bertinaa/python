from tkinter import *
FONT = ("Arial",14,"normal")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10,pady=10) #padding

miles = Label(text="Miles", font=FONT)
miles.grid(row=0, column=2)
miles.config(pady=10,padx=10)

equal = Label(text="is equal to", font=FONT)
equal.grid(row=1, column=0)
equal.config(pady=10,padx=10)

km = Label(text="Km", font=FONT)
km.grid(row=1, column=2)
km.config(pady=10,padx=10)

ans = Label(text="0", font=FONT)
ans.grid(row=1, column=1)
ans.config(pady=10,padx=10)



def miles_to_km():
    user_input = int(input.get())
    answer = user_input * 1.6
    ans.config(text=answer)

#creating button1
button1 = Button(text="Calculate",command=miles_to_km)
button1.grid(row=2,column=1)



#entry
input = Entry(width=10)
input.grid(row=0,column=1)






window.mainloop()
