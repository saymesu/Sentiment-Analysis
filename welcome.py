from tkinter import *

def spam():
	import spam
	root.destroy()

def review():
	import review
	root.destroy()
	
def main():
	import main
	root.destroy()
	
root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(background='aquamarine')
l=Label(root,text='Sentiment Analysis',bg='aquamarine',font=('',40,'bold'))
l.pack()

b1=Button(root,command=review,text='Review Analysis',font=('',20,'bold'))
b1.place(x=450,y=200)

b2=Button(root,command=spam,text='Spam Detection',font=('',20,'bold'))
b2.place(x=850,y=200)

b3=Button(root,command=main,text='Log Out',font=('',20,'bold'))
b3.place(x=700,y=450)

root.mainloop()
