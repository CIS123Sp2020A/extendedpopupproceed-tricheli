#Tenisce Richelieu
from tkinter import 
import tkinter.messagebox as box

#The first step after imports is crate a window
window = Tk()

#This shows up at the top of the frame
window.title('Message Box Example')

#create the dialog for the window
def dialog():
    var = box. askyesno('Message Box', 'Proceed?')

    if var == 1:
        box.showinfo('Yes Box', 'Proceeding...')
    else:
        box.showwarning('No Box', 'Cancelling...')

#creating a button
btn = Button(window, text='Click', command= dialog)

#have to pack the button
btn.pack(padx = 150, pady = 50)

#start the action and keep it going
window.mainloop()
