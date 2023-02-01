from tkinter import*
window=Tk()

text1 =Label(window,text="Username")
text1.grid(column=0,row=0)

text2 =Label(window,text="Password")
text2.grid(column=0,row=1)

ent =Entry(window)
ent.grid(column=1,row=0)

ent2 =Entry(window)
ent2.grid(column=1,row=1)

but =Button(window,text="Login",bg="yellow",fg="black")
but.grid(column=1,row=2)
window.mainloop()
