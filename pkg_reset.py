#!/usr/bin/env python3
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import tkinter
import time
import os
import shutil

class Action():
    def __init__(self):
        #Initial
        screen_width = 600
        screen_height = 400
        self.time_count =9
        
        self.root = Tk()
        self.root.title('RESET')
        self.TFont = ("Cordia new", 20)
        self.TFont2 = ("Cordia new", 25)
        self.TFont3 = ("Cordia new", 15)
        self.widget = 0
        self.confirm = 0
        self.flag_proceed= 0
        self.state=0
        self.w = screen_width
        self.h = screen_height
        self.password = ''
        self.wrong_pass=0
        
        Label(text ="You are about to ",fg="black",font=self.TFont3).place(x=self.w/60,y=self.h/13)
        Label(text =" remove all ROS-related workspaces and packages.",fg="black",font=self.TFont3).place(x=self.w/60 + self.w/5.5,y=self.h/13)
        Label(text ="ROS environment will be reverted to its original state as if it were recently installed.",fg="black",font=self.TFont3).place(x=self.w/60 ,y=self.h/7)
        Label(text ="PLEASE REMOVE ALL NECESSARY FILES",fg="red",font=self.TFont3).place(x=self.w/60 ,y=self.h/4)
        Label(text =" in ROS2_Directory before proceeding",fg="black",font=self.TFont3).place(x=self.w/60 + self.w/2.25 ,y=self.h/4)
        Label(text ="to the next step.",fg="black",font=self.TFont3).place(x=self.w/60 ,y=self.h/3.25)
        button1=Button(self.root, text="Next",bg='green',fg='white',command=self.click_proceed)
        button1.place(x=self.w/6,y=self.h*3/4)
        button2=Button(self.root, text="Exit",bg='red',fg='white',command=self.cancel_click)
        button2.place(x=self.w/6 + self.w/2,y=self.h*3/4)  
        self.root.geometry(str(screen_width)+'x'+str(screen_height))
        self.root.eval('tk::PlaceWindow . center')
        self.root.mainloop()

        

    def cancel_click(self):
        confirm_cancel = tkinter.messagebox.askquestion('Confirmation','Are you sure to exit program ?')
        if confirm_cancel == 'yes':
            self.root.destroy()
            self.root2.destroy()
            exit()

    def click_proceed(self):
            self.state =1
            self.root.destroy()

    def click_proceed2(self):
        self.confirm = tkinter.messagebox.askquestion('Confirmation','Are you sure to proceed ?')
        if self.confirm == 'yes':
            self.password = self.pass_txt.get() 
            self.root2.destroy()
            self.state =5
            
        
    def back_btn(self):
        confirm_cancel = tkinter.messagebox.askquestion('Confirmation','Are you sure to exit program ?')
        if confirm_cancel == 'yes':      
            self.root2.destroy()
            self.state = 0
            exit()
    
    def abort(self):
        self.state=4
        self.root3.destroy()
        exit()
    
    def save_password(self):
        self.password = self.pass_txt.get() 
        print(self.password)
    def second_screen(self):
        # second
        self.root2 = Tk()
        self.root2.title('RESET')
        self.root2.geometry(str(self.w)+'x'+str(self.h))
        Label(text ="By pressing the reset button,",fg="black",font=self.TFont3).place(x=self.w/60,y=self.h/7)
        Label(text ="the reverting process will begin after 10 seconds have passed.",fg="black",font=self.TFont3).place(x=self.w/60,y=self.h/4)
        proceed_btn=Button(self.root2, text="Proceed",bg='green',fg='white',command=self.click_proceed2)
        proceed_btn.place(x=self.w/6,y=self.h*3/4)
        cancel_btn=Button(self.root2, text="Exit",bg='red',fg='white',command=self.back_btn)
        cancel_btn.place(x=self.w/6 + self.w/2,y=self.h*3/4)
        Label(text ="Input password  : ",fg="black",font=self.TFont).place(x=self.w/60,y=self.h/2.5)
        self.pass_txt = StringVar()
        password_box = Entry(self.root2,textvariable=self.pass_txt)
        password_box.place(x=self.w/60 + self.w/4,y=self.h/2.5 +self.h/60)
        if self.wrong_pass ==1:
            Label(text ="Incorrect password",fg="red",font=self.TFont).place(x=self.w/1.8,y=self.h/2.5)
            self.wrong_pass=0
        self.root2.eval('tk::PlaceWindow . center')       
        self.root2.mainloop()
    
    def third_screen(self):   
        self.root3 = Tk()
        self.root3.title('RESET')
        self.root3.geometry(str(self.w)+'x'+str(self.h))
        self.root3.eval('tk::PlaceWindow . center')
        Label(text ="The reverting process will start in ...",fg="black",font=self.TFont3).place(x=self.w/60 ,y=self.h/13)
        abort_btn=Button(self.root3, text="ABORT",bg='red',fg='white',command=self.abort)
        abort_btn.place(x=self.w/2-self.w/50,y=self.h*3/4)
        while(self.time_count!=-1):            
            Label(text = str(self.time_count),fg="black",font=self.TFont2).place(x=self.w/2,y=self.h/2-self.h/12)
            self.time_count-=1
            time.sleep(1)
            self.root3.update()
        print(self.password)
        self.root3.destroy()
        tk.state=3
    
    def four_screen(self):
        self.root4 = Tk()
        self.root4.title('RESET')
        self.root4.geometry(str(self.w)+'x'+str(self.h))
        self.root4.eval('tk::PlaceWindow . center')
        Label(text = "REVERTING . . .",fg="black",font=self.TFont2).place(x=self.w/2-self.w/6,y=self.h/2-self.h/12)
        self.root4.update()
    def complete(self):
        Label(text = "Revert Complete !",fg="black",font=tk.TFont2).place(x=tk.w/2-tk.w/6,y=tk.h/2-tk.h/12)
        self.root4.update()

class Reset():

    def __init__(self,Password):
        self.password=Password

    def testpassword(self):
        try:
            pathdel = os.path.join(os.path.expanduser('~'), '.testpassword')
            self.Sendcommand("sudo mkdir ~/.testpassword")
            shutil.rmtree(pathdel)
            print("")
            print("***************Password TRUE***************")
            return 1
        except:
            print("***************Password False***************")
            return 0

    def Sendcommand(self,q):
        try:
            sudopassword = self.password
            command = q
            os.system('echo %s|sudo -S %s' % (sudopassword, command))
        except:
            print("self.password wrong")
        return 1

    def removeROS2(self):
        try:
            self.Sendcommand("sudo apt remove ~nros-foxy-* -y")
            self.Sendcommand("sudo apt autoremove -y")
            print("***************Remove Done***************")
        except:
            print("***************Error Uninstall***************")
        return 1
        

    def installROS2(self):
        try:
            self.Sendcommand("sudo apt update -y")
            self.Sendcommand("sudo apt upgrade -y")
            self.Sendcommand("sudo apt install ros-foxy-desktop -y")
            print("***************Install Done***************")
        except:
            print("***************Error Install***************")
        return 1


    def manageDirectory(self):
        try:
            pathdel = os.path.join(os.path.expanduser('~'), 'ROS2_Directory')
            shutil.rmtree(pathdel)
            print("***************Delete ROS2_Directory Done***************")
            os.mkdir(pathdel)
            print("***************Create ROS2_Directory Done***************")

        except:
            print("***************Not found ROS2_Directory***************")
            os.mkdir(pathdel)
            print("***************Create ROS2_Directory Done***************")
        return 1

    def getId(self):
        try:
            ww=os.environ["USER"]
            num=""
            for i in range (0,len(ww)):
                if(ww[i].isnumeric()):
                    num=num+ww[i]
            return str(int(num))
        except:
            print("Get fail")
            return str(1)

    def clearbashrc(self):
        try:
            pathw = os.path.join(os.path.expanduser('~'), '.bashrc')
            pathr = os.path.join(os.path.expanduser('~'),'.pkg_reset', ".RAW_bashrc")
            fr=open(pathr, 'r') 
            fw=open(pathw, 'w') 
            for line in fr:
                fw.write(line)
            fw.write("export ROS_DOMAIN_ID=" + self.getId())
            print("***************Reset bashrc Done***************")
        except:
            print("***************Reset bashrc Fail***************")
        return 1
    def runReset(self):
        self.manageDirectory()
        self.removeROS2()
        self.installROS2()
        self.clearbashrc()  
        return 1 


if __name__ == '__main__' :
    tk = Action()
    while(1):
        if tk.state==1:
                tk.second_screen()
                
                # tk.state=2
        elif tk.state==2:
                tk.third_screen()
   
        elif tk.state==3:
            #mark state
            

            tk.four_screen()
            if rr.runReset():
                tk.complete()
                print('DONEEEEEEEEEEEEEE')        
                tk.state=4

        elif tk.state==4:
            time.sleep(1)
            exit()

        elif tk.state==5: ##Check pass
            rr=Reset(tk.password)
            if rr.testpassword(): #passwd correct
                tk.state=2
            else:        
                tk.state=1
                tk.wrong_pass = 1
                print("wrong password")
