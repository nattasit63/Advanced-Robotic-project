from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import tkinter
from turtle import color
#Initial
screen_width = 300
screen_height = 180
orgin_ship_x =0
orgin_ship_y =0
root = Tk()
root.title('UI')
TFont = ("Cordia new", 10)
depot_txt = StringVar()



#ALL FUNCTION
def openFile():
    root_filename = filedialog.askopenfilename(initialdir="/home/natta/adv_ws/src/interface/config",title='Select .yaml file',filetypes=(("yaml file","*.yaml"),("all files","*.*")))
    print("Path to File : ",root_filename)
    tkinter.messagebox.showinfo('File path',root_filename )
    text_DEPOT = Label(text ="Depot node : ",fg="black",font=TFont).grid(row=3,column=0)
    depot_box = Entry(root,textvariable=depot_txt)
    depot_box.grid(row=3,column=1)
def exit_program():
    confirm = tkinter.messagebox.askquestion('Confirmation','Are you sure to exit program ?')
    if confirm == 'yes':
        root.destroy()


#create menu
my_menu = Menu()
sub_menu = Menu()
root.config(menu=my_menu)
my_menu.add_cascade(label='File',menu=sub_menu)
sub_menu.add_command(label='exit',command=exit_program)

#create text on screen
# text1 = Label(text ="Select File",fg="red",font=TFont)
# text1.place(x=screen_width/2,y=screen_height/2)

#create button and do something
button1=Button(root, text="select file",command=openFile)
button1.grid(row=1,column=0)




root.geometry(str(screen_width)+'x'+str(screen_height))
root.mainloop()