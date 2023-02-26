#My Glossary Project
from tkinter import *
from PIL import ImageTk, Image
#Key Down Function
def click():
    entered_text=textentry.get()
    output.delete(0.0,END)
    try:
        definition=my_compdictionary[entered_text]
    except:
        definition="Sorry There is no Word Like That Please try Again"
    output.insert(END,definition)
    
###Main
window=Tk()
canv=Canvas(window,bg="black")
canv.grid(row=0,column=0)
window.title("My Computer Science Glossary")
window.configure(background="black")
#### My Photo
img=ImageTk.PhotoImage(Image.open("download.jpg"))
canv.create_image(0,0,anchor=W,image=img)
#Create Label
Label(window,text="Enter The Word you Would Like A definition for:",bg="black",fg="white",font="none 12 bold").grid(row=1,column=0,sticky=W)
#Create a text entry boy
textentry=Entry(window,width=20,bg="White")
textentry.grid(row=2,column=0,sticky=W)
# add a submit button
Button(window,text="SUBMIT",width=6,command=click).grid(row=3,column=0,sticky=W)
# create another label
Label(window,text="\nDefinition:",bg="black",fg="white",font="none 12 bold").grid(row=4,column=0,sticky=W)
#Create Text Box
output=Text(window,width=75,height=6,wrap=WORD,background="white")
output.grid(row=5,column=0,columnspan=2,sticky=W)
#the dictionary
my_compdictionary={"Algorithm":"Step By Step for a complete task","bug":"A piece of code that causes problem"}



