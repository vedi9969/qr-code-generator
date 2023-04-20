from tkinter import *
import tkinter.messagebox as msg
from matplotlib import image
import pyqrcode
import png
from pyqrcode import QRCode
import tkinter.ttk as ttk


root = Tk()
root.geometry("1200x700")
root.resizable(False,False)
root.configure(bg="#247F4F")

global links
global color_var
global title_var
links = StringVar()
color_var = StringVar()
title_var = StringVar()


###################colors####################
Blue = [ 0, 0, 153]
green = [0, 102, 0]
black = [27, 28, 28]
red = [189, 70, 107]
cyan = [144, 209, 206]

color_t = (Blue,green,black,red,cyan)
# print(color_t[1])


def reset():
    links.set("")
    color_var.set("Select BG Color")
    title_var.set("")
    img_view.config(image="")



def create():

    # new_l = links.get()
    # url = pyqrcode.create(new_l, error='H',version=20,mode='binary')
    # url.png('new.png', scale = 3)
    
    if color_var.get() == "Blue":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[0]),background=[255, 255, 255])
        msg.showinfo("Success", f"{name_ent} Your QRcode Created!")

        global Image
        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)
        
    
    elif color_var.get() =="green":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[1]),background=[255, 255, 255])
        msg.showinfo("Success", f"{name_ent} Your QRcode Created!")

        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)

    
    elif color_var.get() =="black":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[2]),background=[255, 255, 255])
        msg.showinfo("Success", f"{name_ent} Your QRcode Created!")

        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)

    elif color_var.get() =="red":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[3]),background=[255, 255, 255])
        msg.showinfo("Success", f"{name_ent} Your QRcode Created!")
   
        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)
    
    elif color_var.get() =="cyan":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[4]),background=[255, 255, 255])
        msg.showinfo("Success", f"{name_ent} Your QRcode Created!")
        
        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)

    else:
        color_var.get() == "" or title_var.get() == "" or links.get() == ""
        msg.showerror("Error", "All Fields Are Required")

            


#################images#################
heading = PhotoImage(file=r"C:\\Users\\Vedika\\Downloads\\12.png")
create_img = PhotoImage(file=r"C:\\Users\\Vedika\\Downloads\\11.png")
reset_img = PhotoImage(file=r"C:\\Users\\Vedika\\Downloads\\13.png")
################################################################


############## UI Part ###################

frame = Frame(root,bg="#f2f2f2")
frame.place(x = 70, y = 90, height=580, width= 1050)

head_img = Label(root,image=heading, bg="#247F4F")
head_img.place(x = 430, y= 10)


title_lbl = Label(frame,text="Enter Your Image Title",bg="#f2f2f2",fg="#595959",font="sans-serif 15 bold")  #Verdana
title_lbl.place(x= 40, y= 40)

title_ent = Entry(frame,textvariable=title_var,bd=0,font="sans-serif 12 bold")
title_ent.place(x = 40, y=90, height=30, width=400)

lbl1 = Label(frame,text="Your URl",bg="#f2f2f2",fg="#595959",font="sans-serif 15 bold")  #Verdana
lbl1.place(x= 40, y= 300)

ent = Entry(frame,textvariable=links,bd=0,font="sans-serif 12 bold")
ent.place(x = 40, y=360, height=40, width=500)



lbl2 = Label(frame,text="SET COLOURS",bg="#f2f2f2",fg="#595959",font="sans-serif 15 bold")  #Verdana
lbl2.place(x= 40, y= 170)

lbl2_combo = ttk.Combobox(frame,textvariable=color_var,font="Verdana 8 bold", width=18, state="readonly")
lbl2_combo["values"] = ("Select BG Color", "Blue", "green", "black", "red", "cyan")
lbl2_combo.current(0)
lbl2_combo.place(x = 45, y = 230)


gen_btn = Button(frame,image=create_img,bd=0,command=create)
gen_btn.place(x= 40, y = 450)

reset_btn = Button(frame,image=reset_img,bd=0,command=reset)
reset_btn.place(x= 320, y = 450)


intro = Label(frame,text="Created By Team !",bg="#f2f2f2",font="sans-serif 9 ")
intro.place(x = 500, y=560)


########## this is for showing qrocode in the box  ##########
img_view = Label(frame)
img_view.pack(padx=50,pady=10,side=RIGHT)



root.mainloop()