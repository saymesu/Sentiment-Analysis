from tkinter import *
import string
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB


def goBack():
	root.destroy()
	import welcome

def removePunc(doc):
	pc=string.punctuation
	clean_doc=re.sub(f'[{pc}]','',doc)
	return clean_doc

df=pd.read_csv('Restaurant_Reviews.txt',delimiter='\t')
df['Review']=df.Review.apply(removePunc)
cv=CountVectorizer(stop_words='english')
X=cv.fit_transform(df.Review).todense()
gnb=GaussianNB()
gnb.fit(X,df.Liked)	

def mypredict():
	new_rvw=e.get()
	X_test=cv.transform([new_rvw]).todense()
	p=gnb.predict(X_test)
	if(p[0]==1):
		l3.configure(text='Liked',fg='green')
	else:
		l3.configure(text='Not Liked',fg='red')

root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(background='aquamarine')
l=Label(root,text='Review Analysis',bg='aquamarine',font=('',40,'bold'))
l.pack()

l4=Label(root,text='(Predicts customers opinion about food)',bg='aquamarine',font=('',18,'bold'))
l4.pack()

l2=Label(root,text='Enter Review:',bg='aquamarine',font=('',20,'bold'))
l2.place(x=100,y=200)

l3=Label(root,text='',bg='aquamarine',font=('',20,'bold'))
l3.pack(padx=300,pady=50)

e=Entry(root,font=('',20,'bold'))
e.place(x=300,y=200)

b1=Button(root,command=mypredict,text='Predict',font=('',20,'bold'))
b1.place(x=300,y=300)

b2=Button(root,command=goBack,text='Back',font=('',20,'bold'))
b2.place(x=480,y=300)

root.mainloop()
