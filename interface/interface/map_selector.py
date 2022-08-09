from select import select
import pygame as pg
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import tkinter
import time
import json
import yaml
import string
import os
from math import sqrt
import ast
class Select():
    def __init__(self):
        #Initial
        self.flag_launch = 0
        self.image_file = 0
        self.fname=''
        # First screen
        self.root = Tk()
        self.root.title('GUI')
        screen_width = 800
        screen_height = 600
        self.my_menu = Menu()
        self.sub_menu = Menu()
        self.depot_txt = StringVar()
        self.root.config(menu=self.my_menu)
        self.my_menu.add_cascade(label='File',menu=self.sub_menu)
        self.sub_menu.add_command(label='exit',command=self.exit_program)
        self.TFont = ("Cordia new", 10)      
        Button(self.root, text="select file",command=self.openFile).grid(row=1,column=0)
        self.root.geometry(str(screen_width)+'x'+str(screen_height))
        self.root.mainloop()

        # Info node screen
        self.show_info = Tk()
        self.show_info.title('Info')
        self.show_info.geometry(str(screen_width)+'x'+str(screen_height))
        self.depot_txt = StringVar()
        self.config_name_txt = StringVar()
        self.pd_txt = StringVar()
        self.station_txt = StringVar()
        self.station_list = []
        # to write data
        self.added_node = []
        self.node_pos = []
        self.edge_list = []
        self.edge_num = []
        self.eucl_val = []
        self.pd_id = []


    def openFile(self):
        my_path_default = "$HOME/interface_ws/src/ui/config/"
        # my_path_default = "/home/natta/adv_ws/src/interface/config"
        root_filename = filedialog.askopenfilename(initialdir=my_path_default,title='Select .yaml file',filetypes=(("yaml file","*.yaml"),("all files","*.*")))
        print("Path to File : ",root_filename)
        tkinter.messagebox.showinfo('File path',root_filename )
        Label(text = root_filename,fg="black",font=self.TFont).grid(row=1,column=1)
        if root_filename!='':
            Button(self.root,text='LAUNCH',bg='green',command=self.launch).grid(row=2,column=1)
        with open(root_filename,'r') as f:
            yml_dict = yaml.safe_load(f)
        self.image_file = yml_dict.get('image')
        self.resolution = yml_dict.get('resolution')
        self.origin     = yml_dict.get('origin')
 
    def exit_program(self):
        confirm = tkinter.messagebox.askquestion('Confirmation','Are you sure to exit program ?')
        if confirm == 'yes':
            self.root.destroy()
            pg.quit()
            exit() 

    def exit_program2(self):
        confirm = tkinter.messagebox.askquestion('Confirmation','Are you sure to exit program ?')
        if confirm == 'yes':
            self.show_info.destroy()
            pg.quit()
            exit()    
        
    def launch(self):
        self.flag_launch = 1
        self.root.destroy()
        time.sleep(1)
    
    def create_config(self):
        station_get = self.station_txt.get()
        self.station_list.append(station_get)
        self.station_list = self.station_list[0].split(',')
        pick_dev = '['+self.pd_txt.get()+']'
        
        # print(pick_dev ,type(pick_dev))

        confirm = tkinter.messagebox.askquestion('Confirmation','Are you confrim to write config file ?')
        if confirm == 'yes':
            self.pick_dev = ast.literal_eval(pick_dev)
            self.fname = self.config_name_txt.get()
            if self.fname!='':
                with open(self.fname, 'w') as f:
                    print("----------------The " + str(self.fname) +" file is created--------------")
                
            else :
                with open('new_file.json', 'w') as f:
                    print("----------------The file is created-------------")
            Label(text = "Created ! " ,fg="black",font=tk.TFont).grid(row=5,column=1)    
            Button(tk.show_info, text="Write data",command=tk.wrtie_data,bg='green').grid(row=4,column=3)
                    
    def wrtie_data(self):

        convert_pos = []
        for j in range(0,len(self.node_pos)):
            posx = float((self.node_pos[j][0])*self.resolution)
            posx = '%.1f'%posx
            posy = float((begin.height - self.node_pos[j][1])*self.resolution)
            posy = '%.1f'%posy
            pos = [posx,posy]
            convert_pos.append(pos)

        node_dict = dict(zip(tk.added_node,convert_pos))

        for i in range(len(self.edge_list)):
            self.edge_num += str(i)
        edge_dict = dict(zip(self.edge_num,self.edge_list))


        for k in range(len(self.pick_dev)):
            self.pd_id += str(k)
        pick_dev_dict = dict(zip(self.pd_id,self.pick_dev))


        stations = self.station_list
        len_station = len(stations)
        alphabet_string = string.ascii_uppercase
        alphabet_list = list(alphabet_string)
        alphabet_list = alphabet_list[0:len_station]
        # station_dict = dict(zip(alphabet_list,stations))
         

        # data = {"nodes" : node_dict , "edges" : edge_dict , "stations" : station_dict , "depot" : self.added_node[-1]}
        data = {"nodes" : node_dict , "edges" : edge_dict ,"PICKUP_DELIVERIES" : pick_dev_dict , "depot" : self.added_node[0]}
        print(data)
        with open(self.fname, 'w') as f:
            json.dump(data, f)
            print("---------------data is writed !---------------")
        Label(text = "Writed ! " ,fg="black",font=tk.TFont).grid(row=6,column=1)
    
    def eucl(self,x1,y1,x2,y2):
        return sqrt((x1-x2)**2+(y1-y2)**2)

class Begin():
    def __init__(self):
        # width and height from image size
        self.width = 449
        self.height = 501
        self.screen = pg.display.set_mode((self.width,self.height))
        pg.display.set_caption('gui')

class Draw():
    def __init__(self):  
        self.update = pg.display.update()
        self.font = pg.font.SysFont("Cordia New",begin.height//30)
        firebrick = (178,34,34)
        navy = (0,0,128)
        brown = (139,69,19)
        seagreen = (46,139,87)
        self.color = [firebrick,navy,seagreen,brown]
    def circle(self,pos_x,pos_y,radius):
        pg.draw.circle(begin.screen, (0, 200, 0),[pos_x, pos_y],radius)
        self.update
    def buildtext(self,text,posx,posy):
        pos=(posx,posy)
        label = self.font.render(str(text),1,(0,0,0))
        begin.screen.blit(self.font.render(str(text),True, (0 ,0 ,0)),pos)
        pg.display.update()
    
    def line(self,x1,y1,x2,y2):
        pg.draw.line(begin.screen, (255, 0, 0), (x1, y1), (x2, y2),width=2)
        pg.display.flip()

if __name__ == '__main__':
    pg.init()
    pg.font.init()
    tk=Select()
    
    state = 0
    num_pressadd = 0
    rmouse=0
    click_edge_state = 0
    first_edge_pair = 0
    second_edge_pair = 0
    first_edge_x = 0
    first_edge_y = 0
    second_edge_x = 0
    second_edge_y = 0

    screen_list=[]
    pos_node_click=[]
    added_node =[]
    edge_list = []
    edge_list_no_cost = []
    added_node_str=''
    edge_list_str=''
    
    begin = Begin() 
    bg = pg.image.load(tk.image_file)    # load image from yaml to overlay on pygame
    bg = pg.transform.scale(bg,(begin.width, begin.height))
    rect = bg.get_rect()
    screen = begin.screen
    screen.fill((255,255,255))
    rect = rect.move((0,0))

    draw = Draw()
    while(tk.flag_launch==1):
        if state==0:
            screen.blit(bg,rect)
            pg.display.update()
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()
                    exit()
            pg.display.set_caption('Add Node , Press Enter to do next step')
            state=1
        
        # Add node to graph
        elif state==1:       
            mouse = pg.mouse.get_pos()
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        added_node_str = str(added_node)
                        added_node_str = added_node_str.replace("[","").replace("]","")
                        pg.display.set_caption('Add Edge , Press Enter to do next step')
                        state=2
                        
                        
                elif event.type == pg.MOUSEBUTTONDOWN and event.button==1: #if left click ,Add node at mouse pos
                    # print(mouse)
                    px = mouse[0]
                    py = mouse[1]
                    p = [px,py]
                    pos_node_click.append(p)  #save node click pos
                    added_node.append(str(num_pressadd))

                    current_screen = pg.Surface.copy(begin.screen) #draw node with num
                    screen_list.append(current_screen)
                    draw.circle(mouse[0],mouse[1],begin.width//70)               
                    draw.buildtext(num_pressadd,mouse[0]-begin.width//140,mouse[1]-begin.width//70)
                    
                    rmouse=0
                    num_pressadd+=1
                    
                elif event.type == pg.MOUSEBUTTONDOWN and event.button==3:  #if right click ,Undo one time
                    if num_pressadd>=0 and rmouse==0:
                            del pos_node_click[-1]
                            del added_node[-1]
                            num_pressadd = num_pressadd-1
                            begin.screen.blit(current_screen,(0,0)) 
                            rmouse=1    

        # Add edge to graph                  
        elif state==2:
           
            mouse = pg.mouse.get_pos()
            r = begin.width//70          
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        edge_list_str = str(edge_list_no_cost)
                        edge_list_str = edge_list_str[1:]
                        edge_list_str = edge_list_str[:-1]
                        state=3
                if click_edge_state ==0:
                    if event.type == pg.MOUSEBUTTONDOWN and event.button==1: #if left click ,Select pair
                        for i in range(0,len(pos_node_click)):
                            if pos_node_click[i][0]-r<=mouse[0]<=pos_node_click[i][0]+r and pos_node_click[i][1]-r<=mouse[1]<=pos_node_click[i][1]+r :
                                first_edge_pair = i
                                first_edge_x = pos_node_click[i][0]
                                first_edge_y = pos_node_click[i][1]
                                click_edge_state=1
                elif click_edge_state==1:
                    if event.type == pg.MOUSEBUTTONDOWN and event.button==1: #if left click ,Select pair
                        for i in range(0,len(pos_node_click)):
                            if pos_node_click[i][0]-r<=mouse[0]<=pos_node_click[i][0]+r and pos_node_click[i][1]-r<=mouse[1]<=pos_node_click[i][1]+r :
                                second_edge_pair = i
                                second_edge_x = pos_node_click[i][0]
                                second_edge_y = pos_node_click[i][1]
                                if first_edge_pair!=second_edge_pair:
                                    #draw and add edge to list
                                    draw.line(first_edge_x,first_edge_y,second_edge_x,second_edge_y)                                   
                                    tk.eucl_val.append(tk.eucl(first_edge_x,first_edge_y,second_edge_x,second_edge_y))
                                    cost = tk.eucl(first_edge_x,first_edge_y,second_edge_x,second_edge_y)
                                    edge_list_no_cost.append([first_edge_pair,second_edge_pair])
                                    edge_list.append([first_edge_pair,second_edge_pair,cost])                      
                                    click_edge_state=0
            pg.display.update()


        elif state==3:
            Label(text = "Total added node:",fg="black",font=tk.TFont,justify='left').grid(row=0,column=0)
            Label(text = str(num_pressadd) + "  node",fg="black",font=tk.TFont,anchor=E).grid(row=0,column=1)           
            Label(text = "Node:" ,fg="black",font=tk.TFont,justify='left').grid(row=1,column=0)
            Label(text = added_node_str ,fg="black",font=tk.TFont,anchor=E).grid(row=1,column=1)
            Label(text = "Edge:" ,fg="black",font=tk.TFont).grid(row=2,column=0)
            Label(text = edge_list_str ,fg="black",font=tk.TFont,anchor=E).grid(row=2,column=1)
            # Label(text = "Select station" ,fg="black",font=tk.TFont).grid(row=3,column=0)
            # station_box = Entry(tk.show_info,textvariable=tk.station_txt)
            # station_box.grid(row=3,column=1)


            Label(text = "Pickup & Deliveries :\n(format = [pick_up, delivery, amount])" ,fg="black",font=tk.TFont,anchor=E).grid(row=3,column=0)
            pd_box = Entry(tk.show_info,textvariable=tk.pd_txt).grid(row=3,column=1)


            Label(text = "Config file name:" ,fg="black",font=tk.TFont).grid(row=4,column=0)
            config_name_box = Entry(tk.show_info,textvariable=tk.config_name_txt)
            config_name_box.grid(row=4,column=1)
            Button(tk.show_info, text="create config",command=tk.create_config).grid(row=4,column=2)
            Button(tk.show_info, text="Exit",command=tk.exit_program2,bg='red').grid(row=10,column=0) 
            tk.added_node = added_node
            tk.node_pos = pos_node_click
            tk.edge_list = edge_list


            tk.show_info.mainloop() 
    
    
    