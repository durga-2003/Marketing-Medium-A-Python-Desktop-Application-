#--------------------------LIBRARIES-----------------------------------#
from tkinter import *
from tkinter import messagebox  
import requests
import json
from mainwindowofwgih import wwindow

#--------------------------MAIN FUNCTION-----------------------------------#
URL = 'http://localhost:8000/'

def login(username,password):
    global token_out
    username = entry_usr_l.get()
    password = entry_pass_l.get()
    print(username,password)
    if username == '' or password == '':
        messagebox.showerror(
            'Required Field', 'Enter proper username/password')
    else:
        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(URL+'account-token-auth/',data=data)
            response_dict = json.loads(response.text)
            print(response_dict)
            token_out = response_dict['token']
            print(token_out)
            messagebox.showinfo('Login success','Welcome to Marketing Medium')
            rootlogin.destroy()
            wwindow()
        
        except Exception as e:
            messagebox.showerror('Login failure','Username or password is incorrect')

#--------------------------ROOTWINDOW-----------------------------------#
rootlogin = Tk()
rootlogin.iconbitmap('D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico')
rootlogin.title("Marketing Medium")
rootlogin.maxsize(width=550, height=593)
rootlogin.minsize(width=550, height=593)
image_path_login = PhotoImage(file = "D:\MarketingMedium\env_tkinter\Mainfolder\images\loginimg.png")
bg_image_login = Label(rootlogin,image = image_path_login)
bg_image_login.place(relheight = 1,relwidth= 1)

#--------------------------USERNAME LABEL-----------------------------------#
user_l = StringVar()
entry_usr_l = Entry(rootlogin, textvariable=user_l, justify='center',font="amatic 13",bd="3")
entry_usr_l.focus()
entry_usr_l.place(x=200,y=243,width=250)

#--------------------------PASSWORD LABEL-----------------------------------#
pass_l = StringVar()
entry_pass_l = Entry(rootlogin,show="*",textvariable=pass_l, justify='center',font="amatic 13",bd="3")
entry_pass_l.place(x=200,y=317,width=250)

#--------------------------LOGIN BUTTON-----------------------------------# 
loginbtn_img = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\loginbtn.png")
loginbtn = Button(rootlogin,image=loginbtn_img,bd=0,highlightthickness=0,command=lambda: login(entry_usr_l.get(), entry_pass_l.get()))
loginbtn.place(x=352,y=390)

#--------------------------CLEAR DATA-----------------------------------#
def cleardata(entry_usr_l,entry_pass_l):
          entry_usr_l.delete(0, END)
          entry_pass_l.delete(0, END)
          
clearbtn_img = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\clearbtn.png")
clearbtn = Button(rootlogin,image=clearbtn_img,bd=0,highlightthickness=0,command=lambda: cleardata(entry_usr_l,entry_pass_l))
clearbtn.place(x=198,y=390)

rootlogin.mainloop()
