#-------------------------------------------ALL MODULES-----------------------------------------#
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
from tkinter import filedialog
from tkinter import *
from time import sleep
from time import strftime
from tkinter import messagebox  
from tkinter import ttk 
from threading import Thread
import datetime as dt
import pandas as pd
import os
import pyautogui
from PIL import ImageTk, Image
import tkinter.scrolledtext as scrolledtext
import pyperclip as pc
import requests
from bs4 import BeautifulSoup
import sqlite3



#--------------------------MAIN WINDOW INITIALIZER----------------------------#
def wwindow():
    root = Tk()
    root.iconbitmap('D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico')
    root.title("Marketing Medium")
    root.maxsize(width=1366, height=768)
    root.minsize(width=1366, height=768)
    image_path = PhotoImage(file = "D:\MarketingMedium\env_tkinter\Mainfolder\images\whatsbgnew.png")
    bg_image = Label(root,image = image_path)
    bg_image.place(relheight = 1,relwidth= 1)

    #-----------------------------MAIN WINDOW CLEAR DATA[FUNCTION]----------------------------------#
    def clear_data(tree,text):
        for item in tree.get_children():
            tree.delete(item)
        text.delete("1.0",END)

    #-----------------------------MAIN WINDOW UPDATE TME[FUNCTION]----------------------------------#
    def update_time():
        current_time = strftime('%I:%M:%S %p')
        clockimgright.config(text=current_time)
        root.after(1000, update_time)

    #-----------------------------MAIN WINDOW COUNTRY CODE[FUNCTION]--------------------------------#
    def cc(event):
        global cc_w
        cc_w = selected_elem.get()
    
    #------------------------MAIN WINDOW BROWSE FILE[FUNCTION]----------------------------------#       
    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.xlsx*"),("all files","*.*")))
        global label_file_explorer
        label_file_explorer = filename
        valuechange_w = f"{label_file_explorer}"
        update_listbox_browse_w(valuechange_w)

    #-----------------------MAIN WINDOW DOWNTXTPLS FOR EXCEL UPDATE[FUNCTION]-----------------------#
    def update_listbox_browse_w(new_value_browse_w):
        # Clear existing items
        downtxtpls_w.delete(1,1)
        downtxtpls_w.insert(1,"Your Excel file path : " + new_value_browse_w)
    
    #-----------------------------MAIN WINDOW CHOOSE FILE[FUNCTION]----------------------------------#
    def choosefile():
        filename2 = filedialog.askopenfilename(initialdir = "/",title = "Select a File")
        global label_choose_file
        label_choose_file = filename2
        valuechange_w_c = f"{label_choose_file}"
        update_listbox_choose_w(valuechange_w_c)

    #--------------MAIN WINDOW DOWNTXTPLS FOR CHOOSE FILE UPDATE[FUNCTION]----------#
    def update_listbox_choose_w(new_value_choose_w):
        # Clear existing items
        downtxtpls_w.delete(2,2)
        downtxtpls_w.insert(2,"Your Choosen file path : " + new_value_choose_w)

    #-----------------------------MAIN WINDOW SLEEP UP & DOWN[FUNCTION]-----------------------------#
    def up():
        number.set(number.get()+1)

    def down():
        number.set(number.get()-1)
        
    #-----------------------------MAIN WINDOW SUBMIT[FUNCTION]----------------------------------#
    def submitFunction() :
        #--------------------------MESSAGE------------------------#
        if my_str.get() == "Message":
            sleep(int(entry.get()))
            global excel_data
            excel_data = pd.read_excel(f'{label_file_explorer}')
                    # Start a new instance of Chrome WebDriver
            driver = webdriver.Chrome()

            # Open WhatsApp Web
            driver.get("https://web.whatsapp.com/")
            sleep(60)  # Wait for the user to scan the QR code and log in

            # Iterate over each row in the Excel sheet
            for index, row in excel_data.iterrows():
                try:
                    name = row['Name']
                    phone = str(row['Phone'])
                    
                    # Search for the contact by name
                    search_box = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
                    search_box.click()
                    search_box.send_keys(phone)
                    search_box.send_keys(Keys.ENTER)
                    sleep(10)  # Wait for the contact to load
                    
                    # Send message
                    message_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
                    message_box.send_keys(text.get("1.0",'end-1c'))
                    message_box.send_keys(Keys.ENTER)
                    sleep(15)  # Wait for the message to send
                    tree.insert("","end", values=('',phone,'Done'))
                except Exception as e:
                    tree.insert("","end",values=('',phone,'Failed'))
                    # Close the browser
            driver.quit()
    
        #--------------------IMAGE AND VIDEO----------------------#    
        if my_str.get() == "Image and Video":
            sleep(int(entry.get()))
            excel_data = pd.read_excel(f'{label_file_explorer}')
            count = 0
            driver = webdriver.Chrome()
            driver.get('https://web.whatsapp.com')
            sleep(60)  # Wait for the user to scan the QR code and log in

            # Iterate over each row in the Excel sheet
            for index, row in excel_data.iterrows():
                    try:
                        name = row['Name']
                        phone = str(row['Phone'])
                    
                        # Search for the contact by name
                        search_box = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
                        search_box.click()
                        search_box.send_keys(phone)
                        search_box.send_keys(Keys.ENTER)
                        sleep(10)  # Wait for the contact to load
                        attachment_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//div[@title = "Attach"]')))
                        attachment_box.click()
                        sleep(10)
                        image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                        sleep(10)
                        image_box.send_keys(f'{label_choose_file}')
                        sleep(20)
                        send_button = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
                        send_button.click()
                        sleep(30)
                        tree.insert("", "end", values=('',phone,'Done'))
                        sleep(4)
                    except Exception as e:
                        tree.insert("", "end", values=('',phone,'Failed'))
            driver.quit()
            
        #--------------------DOCUMENT-------------------------#    
        if my_str.get() == "Document":
            sleep(int(entry.get()))
            excel_data = pd.read_excel(f'{label_file_explorer}')
            driver = webdriver.Chrome()
            driver.get('https://web.whatsapp.com')
            sleep(60)  # Wait for the user to scan the QR code and log in

            # Iterate over each row in the Excel sheet
            for index, row in excel_data.iterrows():
                    try:
                        name = row['Name']
                        phone = str(cc_w)+str(row['Phone'])
                    
                        # Search for the contact by name
                        search_box = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
                        search_box.click()
                        search_box.send_keys(phone)
                        search_box.send_keys(Keys.ENTER)
                        sleep(10)  # Wait for the contact to load
                        attachment_box = driver.find_element(By.XPATH,'//div[@title = "Attach"]')
                        attachment_box.click()
                        sleep(15)
                        image_box = driver.find_element(By.XPATH,
                            '//input[@accept="*"]')
                        sleep(10)
                        image_box.send_keys(f'{label_choose_file}')

                        sleep(10)

                        send_button = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
                        send_button.click()
                        sleep(20)
                        tree.insert("", "end", values=('',phone,'Done'))
                        sleep(4)
                    except Exception as e:
                        tree.insert("", "end", values=('',phone,'Failed'))
            driver.quit() 
            
        #-----------------MESSAGE + IMAGE AND VIDEO------------------#
        if my_str.get() == "Message + Image and Video":
            sleep(int(entry.get()))
            excel_data = pd.read_excel(f'{label_file_explorer}')
            driver = webdriver.Chrome()
            driver.get('https://web.whatsapp.com')
            sleep(60)  # Wait for the user to scan the QR code and log in

            # Iterate over each row in the Excel sheet
            for index, row in excel_data.iterrows():
                    try:
                        name = row['Name']
                        phone = str(cc_w)+str(row['Phone'])
                    
                        # Search for the contact by name
                        search_box = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
                        search_box.click()
                        search_box.send_keys(phone)
                        search_box.send_keys(Keys.ENTER)
                        sleep(10)  # Wait for the contact to load
                        # Send message
                        message_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
                        message_box.send_keys(text.get("1.0",'end-1c'))
                        sleep(15)  # Wait for the message to send
                        attachment_box = driver.find_element(By.XPATH,'//div[@title = "Attach"]')
                        attachment_box.click()
                        sleep(10)
                        image_box = driver.find_element(By.XPATH,
                            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                        sleep(10)
                        image_box.send_keys(f'{label_choose_file}')
                        sleep(10)
                        send_button = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
                        send_button.click()
                        sleep(20)
                        tree.insert("", "end", values=('',phone,'Done'))
                        sleep(4)
                    except Exception as e:
                        tree.insert("", "end", values=('',phone,'Failed'))
            driver.quit()

        #--------------------GROUP MESSAGE--------------------------#      
        if my_str.get() == "Group Message":
            sleep(int(entry.get()))
            excel_data = pd.read_excel(f'{label_file_explorer}')
                    # Start a new instance of Chrome WebDriver
            driver = webdriver.Chrome()

            # Open WhatsApp Web
            driver.get("https://web.whatsapp.com/")
            sleep(60)  # Wait for the user to scan the QR code and log in

            # Iterate over each row in the Excel sheet
            for index, row in excel_data.iterrows():
                try:
                    name = row['Name']
                    phone = str(row['Phone'])
                    
                    # Search for the contact by name
                    search_box = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
                    search_box.click()
                    search_box.send_keys(name)
                    search_box.send_keys(Keys.ENTER)
                    sleep(10)  # Wait for the contact to load
                    
                    # Send message
                    message_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
                    message_box.send_keys(text.get("1.0",'end-1c'))
                    message_box.send_keys(Keys.ENTER)
                    sleep(15)  # Wait for the message to send
                    tree.insert("", "end", values=(name,'','Done'))
                except Exception as e:
                    tree.insert("","end",values=(name,'','Failed'))
                    # Close the browser
            driver.quit()
                            
        #--------------------GROUP MESSAGE + DOCUMENT----------------------#      
        if my_str.get() == "Group Message + Document":
            sleep(int(entry.get()))
            excel_data = pd.read_excel(f'{label_file_explorer}')
            driver = webdriver.Chrome()
            driver.get('https://web.whatsapp.com')
            sleep(60)  # Wait for the user to scan the QR code and log in

            # Iterate over each row in the Excel sheet
            for index, row in excel_data.iterrows():
                    try:
                        name = row['Name']
                        phone = str(cc_w)+str(row['Phone'])
                        # Search for the contact by name
                        search_box = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
                        search_box.click()
                        search_box.send_keys(name)
                        search_box.send_keys(Keys.ENTER)
                        sleep(10)  # Wait for the contact to load
                        # Send message
                        message_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
                        message_box.send_keys(text.get("1.0",'end-1c'))
                        sleep(15)  # Wait for the message to send
                        attachment_box = driver.find_element(By.XPATH,'//div[@title = "Attach"]')
                        attachment_box.click()
                        sleep(15)
                        image_box = driver.find_element(By.XPATH,
                            '//input[@accept="*"]')
                        sleep(10)
                        image_box.send_keys(f'{label_choose_file}')
                        sleep(10)
                        send_button = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
                        send_button.click()
                        sleep(20)
                        tree.insert("", "end", values=(name,'','Done'))
                    except Exception as e:
                        tree.insert("","end",values=(name,'','Failed'))
                    # Close the browser
            driver.quit() 

    #---------------------MAIN WINDOW COMBINE ARGS FOR CLICK HERE[FUNCTION]-----------------------#    
    def combine_funcs(*funcs): 
            def inner_combined_func(*args, **kwargs): 
                for f in funcs:  
                    f(*args, **kwargs)  
            return inner_combined_func     

    #--------------------------SELECT TYPE WINDOW INITIALIZER[FUNCTION]-------------------------------#
    def openNewWindow():
        newWindow = Toplevel()
        newWindow.iconbitmap("D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico")
        newWindow.title("Select type(WW)")
        newWindow.geometry("200x200")
        #-----------------------SELECT TYPE WINDOW CLICK HERE ARGS[FUNCTION]---------------------------#
        def combine_funcs(*funcs): 
            def inner_combined_func(*args, **kwargs): 
                for f in funcs:  
                    f(*args, **kwargs)  
            return inner_combined_func 
        
        #--------------------------MAIN WINDOW SELECT ELEMENT[FUNCTION]------------------------------#  
        def value_changed(event):
            global selected_value_w
            selected_value_w = selected_method.get()
            update_listbox(selected_value_w)
            
        #--------------MAIN WINDOW DOWNTXTPLS UPLDATE FOR SELECT TYPE[FUNCTION]--------------------#
        def update_listbox(new_value):
            downtxtpls_w.delete(0,0)  # Clear existing items
            downtxtpls_w.insert(0,"Selected Type is: " + new_value)
                
        #-----------------------SELECT TYPE GWINDOW MESSAGEBOX[FUNCTION]---------------------------#
        def onClick(): 
            messagebox.showinfo("Message Box", "This is selected",parent=newWindow) 
            newWindow.destroy()
                
        #-----------------------SELECT TYPE GWINDOW DROPDOWN[FUNCTION]---------------------------#
        selected_method = StringVar(value='Mode')
        combobox2 = ttk.Combobox(newWindow,font=('Roboto','10'), textvariable = selected_method,width=22)
        combobox2['values'] = ('Message', 'Image and Video', 'Document','Message + Image and Video','Group Message','Group Message + Document')
        combobox2['state'] = 'readonly'
        combobox2.pack()   
        combobox2.bind('<<ComboboxSelected>>', value_changed)
        btn_click= Button(newWindow,text="Click Here",command=combine_funcs(lambda:my_str.set(selected_method.get()),onClick))
        btn_click.pack()
            
    #---------------------SELECT TYPE WINDOW JISMY VALUES JARHA HY-------------------#        
    my_str = StringVar()

    #-----------------------GMAIL WINDOW INITIALIZER[FUNCTION]---------------------------#
    def gmailwindow():
        #-------------------------SQLITE[FUNCTION] FOR GMAIL----------------------------#
        def save_to_database():
        # Connect to SQLite database (creates the database file if it doesn't exist)
            conn = sqlite3.connect('treeview_data_g.db')
            cursor = conn.cursor()

            # Create a table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS treeview_data_g (
                    id INTEGER PRIMARY KEY,
                    GmailID VARCHAR(255),
                    Status TEXT
                )
            ''')

            # Get data from Treeview
            data = []
            for item in tree.get_children():
                values = tree.item(item, 'values')
                data.append((values[0], values[1]))

            # Save data to SQLite table
            cursor.executemany('INSERT INTO treeview_data_g (GmailID, Status) VALUES (?, ?)', data)

            # Commit changes and close the connection
            conn.commit()
            conn.close()
        
        newgmailWindow = Toplevel()
        newgmailWindow.title("New Window")
        newgmailWindow.geometry("1366x768")
        newgmailWindow.iconbitmap('D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico')
        newgmailWindow.title("Marketing Medium")
        newgmailWindow.minsize(width=1200, height=600)
        global image_path_g
        image_path_g= PhotoImage(file = "D:\MarketingMedium\env_tkinter\Mainfolder\images\gmailbg.png")
        bg_image_g = Label(newgmailWindow,image = image_path_g)
        bg_image_g.pack()
        
        #--------------------CLOCK-TIMER-G[FUNCTION]-----------------#
        def update_time():
            current_timeg = strftime('%I:%M:%S %p')
            clockimgrightg.config(text=current_timeg)
            newgmailWindow.after(1000, update_time)
            
        #--------------------DATE-G-----------------------#
        dateg = dt.datetime.now()
        dateupperleftg = Label(newgmailWindow, text=f"{dateg:%Y-%m-%d}", font="gothic, 17 bold",bg="black",fg="white")
        dateupperleftg.place(x=92, y=7)
        
        #--------------------CLOCK-TIMER-G-----------------#
        clockimgrightg = Label(newgmailWindow, text="", font="gothic, 17 bold",bg="black",fg="white")
        clockimgrightg.place(x=1151, y=7)
        update_time()
        
        #------------------SUBJECT-ENTRYBOX-gmail-----------------#
        global subject_text
        subject_text = StringVar(value='Enter Subject')
        subentry = Entry(newgmailWindow,textvariable=subject_text,font="gothic, 15 bold",width=22,bd=3)
        subentry.place(x=290,y=67,height=33)
        
        #-----------------SLEEP-TIMER-GMAIL[FUNCTION]-------------------------#
        def up_g():
            number_g.set(number_g.get()+1)
        def down_g():
            number_g.set(number_g.get()-1)
        
        #------------SLEEP-COUNTDOWN------------------#
        number_g = IntVar()
        entry_g = Entry(newgmailWindow, textvariable=number_g, justify='center',font="gothic 10")
        entry_g.place(x=570,y=67,width=54)
        buttonframe_g = Frame(entry_g)
        buttonframe_g.pack(side=RIGHT)
        buttonup_g = Button(buttonframe_g, text="▲", font="gothic 5", command=up_g,background="#3BA4FF",foreground="white")
        buttonup_g.pack(side=TOP,pady=2)
        buttondown_g = Button(buttonframe_g, text="▼", font="gothic 5", command=down_g,background="#3BA4FF",foreground="white")
        buttondown_g.pack(side=BOTTOM,pady=2)
        
        #-----------------------upload-xlsx[FUNCTION]------------------#
        def browseFiles_g():
            filename_G = filedialog.askopenfilename(parent=newgmailWindow,initialdir = "/",title = "Select a File",filetypes = (("Text files","*.xlsx*"),("all files","*.*")))
            global label_file_explorer_g
            label_file_explorer_g = filename_G
            valuechange = f"{label_file_explorer_g}"
            update_listbox_browse(valuechange)
            
        #----------------------GMAIL WINDOW DOWNTXTPLS EXCEL PATH[FUNCTION]-----------------#
        def update_listbox_browse(new_value_browse):
        # Clear existing items
            downtxtpls.delete(1,1)
            downtxtpls.insert(1,"Your Excel file path : " + new_value_browse)
        
        #-----------------UPLOAD XLSX-GMAIL------------------#
        global button_explore_img_g
        button_explore_img_g= PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\gxlsxbox.png")
        button_explore_g = Button(newgmailWindow,image=button_explore_img_g,highlightthickness = 0, bd = 0,command=browseFiles_g)
        button_explore_g.place(x=650,y=61)
        
        #-------------------MESSAGE-TEXTBOX-[GMAIL]------------------#
        vg=Scrollbar(newgmailWindow,orient='vertical',bg="darkgray")
        vg.place(height=117,x=796,y=143)
        textg=Text(newgmailWindow, font=("gothic, 17"), yscrollcommand=vg.set,width=38,height=4,bd=4)
        vg.config(command=textg.yview)
        textg.place(x=290,y=143)
        
        #--------------------------SELECT TYPE GWINDOW INITIALIZER[FUNCTION]------------------------#
        def openNewWindow_gs():
            newWindow_gs = Toplevel()
            newWindow_gs.iconbitmap("D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico")
            newWindow_gs.title("New Window")
            newWindow_gs.geometry("200x200")
            #-----------------------SELECT TYPE GWINDOW CLICK HERE ARGS[FUNCTION]-----------------#
            def combine_funcs(*funcs): 
                def inner_combined_func(*args, **kwargs): 
                    for f in funcs:  
                        f(*args, **kwargs)  
                return inner_combined_func
            
            #-------------------------SELECT TYPE GWINDOW UPDATE DOWNLIST[FUNCTION]----------------#
            def value_changed_g(event):
                selected_value = selected_method_gs.get()
                update_listbox(selected_value)
            
            #-------------------------SELECT TYPE GWINDOW UPDATE DOWNLIST[FUNCTION]----------------#
            def update_listbox(new_value):
                downtxtpls.delete(0,0)  # Clear existing items
                downtxtpls.insert(0,"Selected Type is: " + new_value)
                
            #-----------------------SELECT TYPE GWINDOW MESSAGEBOX[FUNCTION]-------------------#
            def onClick_gs(): 
                messagebox.showinfo("Message Box", "This is selected",parent=newgmailWindow) 
                newWindow_gs.destroy()
                
            #-----------------------SELECT TYPE GWINDOW DROPDOWN[FUNCTION]---------------------------#
            selected_method_gs = StringVar(value='Mode')
            combobox2_gs = ttk.Combobox(newWindow_gs,font=('gothic','10'), textvariable = selected_method_gs,width=22)
            combobox2_gs['values'] = ('Message', 'Message + Attachment')
            combobox2_gs['state'] = 'readonly'
            combobox2_gs.pack()     
            combobox2_gs.bind('<<ComboboxSelected>>', value_changed_g)
            btn_click_gs= Button(newWindow_gs,text="Click Here",command=combine_funcs(lambda:my_str_gs.set(selected_method_gs.get()),onClick_gs))
            btn_click_gs.pack()
        
        #---------------------SELECT TYPE GWINDOW JISMY VALUES JARHA HY-------------------#        
        my_str_gs = StringVar()
        
        #-----------------SELECT-TYPE-NEW-WINDOW-[GMAIL]-------------------------#
        global btn_ty
        btn_ty= PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\gselecttype.png")
        imgbtnty = Button(newgmailWindow,image=btn_ty,highlightthickness = 0, bd = 0,command=openNewWindow_gs)
        imgbtnty.place(x=320, y=295)
        
        #-------------------PLEASESELECT-DOWN-LISTBOX-[GMAIL]------------------#
        downtxt=Scrollbar(newgmailWindow,orient='horizontal',background="black")
        downtxt.place(width=909,x=0,y=631)
        global downtxtpls
        downtxtpls=Listbox(newgmailWindow,bg="lightgray",font=("gothic, 16 bold"), xscrollcommand=downtxt.set,width=75,height=6,bd=4)
        downtxt.config(command=downtxtpls.xview)
        downtxtpls.insert("end","Please Select the Type,Excel file and if necessary choose the attachment")
        downtxtpls.place(x=0,y=469)
        
        #--------------------------CHOOSE-FILE[FUNCTION,GMAIL]-------------
        def choosefile_g(): 
            filename_g = filedialog.askopenfilename(parent=newgmailWindow,initialdir = "/",title = "Select a File")
            global label_choose_file_g
            label_choose_file_g = filename_g
            valuechange_choosefile = f"{label_choose_file_g}"
            update_listbox_choose(valuechange_choosefile)

        def update_listbox_choose(new_value_choose):
            downtxtpls.delete(2,2)  # Clear existing items
            downtxtpls.insert(2,"Your choosen file path: " + new_value_choose)

        #-----------------CHOOSEFILE-DOWN-----------------#
        global button_choose_file_img_g
        button_choose_file_img_g = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\gchoosefile.png")
        button_choose_file_g = Button(newgmailWindow,image=button_choose_file_img_g,highlightthickness = 0, bd = 0,command = choosefile_g)
        button_choose_file_g.place(x=515,y=295)
        
        #---------------------CLEARDATA[FUNCTION,GMAIL]-------------------#
        def clear_data(tree,textg):
            for item in tree.get_children():
                tree.delete(item)
            textg.delete("1.0",END)
        
        #-----------------CLEARDATA-GMAIL-----------------#
        button_cleardata_text_g = StringVar()
        global button_cleardata_img_g
        button_cleardata_img_g = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\gcleardata.png")
        button_cleardata_g = Button(newgmailWindow,image=button_cleardata_img_g,textvariable=button_cleardata_text_g,highlightthickness = 0, bd = 0,command=lambda: clear_data(tree,textg))
        button_cleardata_g.place(x=320,y=360)
        
        #--------------CREDENTIALS[GMAIL WINDOW FUNCTION]--------------------#
        def credentials_g():
            credentials = Toplevel()
            credentials.iconbitmap("D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico")
            credentials.title("Credentials(GG)")
            credentials.geometry("400x400")
            credentials.minsize(width=400,height=400)
            credentials.configure(bg="#FDB62E")
        
        #-----------------------GMAIL WINDOW COMBINE_FUNCTION[FUNCTION]---------------------------#
            def combine_funcs_g(*funcs): 
                def inner_combined_func_g(*args,**kwargs): 
                    for f in funcs:  
                        f(*args, **kwargs)  
                return inner_combined_func_g 
            
            #-----------------------GMAIL WINDOW MESSAGEBOX[FUNCTION]---------------------------#
            def onClick_g():
                if id_g.get() == ""  or pass_g.get() == "":
                    messagebox.showwarning("Message Box", "Entry valid credentials",parent=credentials)
                else:
                    messagebox.showinfo("Message Box", "Credentials Saved",parent=credentials)
                credentials.destroy()
                
            #-----------------------GMAIL WINDOW GMAILID LABEL---------------------------#
            id = Label(credentials,text="GMAIL ID: ",font="gothic, 10 bold",bd=0,highlightthickness=0,background="#FDB62E")
            id.place(x=37,y=128)
            
            #-----------------------GMAIL WINDOW GMAILID ENTRY---------------------------#
            global id_g
            id_g = StringVar()
            entry_id_g = Entry(credentials, textvariable=id_g, justify='center',font="gothic 10",bd="3")
            entry_id_g.focus()
            entry_id_g.place(x=130,y=125,width=200)
            
            #-----------------------GMAIL WINDOW PASSWORD LABEL---------------------------#
            password = Label(credentials,text="PASSWORD: ",font="gothic, 10 bold",bd=0,highlightthickness=0,background="#FDB62E")
            password.place(x=30,y=164)
            
            #-----------------------GMAIL WINDOW GMAILID ENTRY---------------------------#
            global pass_g
            pass_g = StringVar()
            entry_pass_g = Entry(credentials,show="*",textvariable=pass_g, justify='center',font="gothic 10",bd="3")
            entry_pass_g.place(x=130,y=159,width=200)
            
            #-----------------------GMAIL WINDOW CREDENTIALS SAVE[FUNCTION]---------------------------#
            up_save = Button(credentials,text="Save",background="#56E032",font="gothic, 12 bold",justify='center',bd=2,fg="white",command=combine_funcs_g(lambda:(my_str_g_id.set(id_g.get())),lambda:(my_str_g_pass.set(pass_g.get())),lambda:(onClick_g())))
            up_save.place(x=230,y=220)
            
            #---------------------CLEAR[GMAIL-FUNCTION]--------------------#
            def clear_g(entry_id_g,entry_pass_g):
                entry_id_g.delete(0, END)
                entry_pass_g.delete(0, END)
                
            #----------------------CLEAR[BUTTON,GMAIL]----------------------#
            up_clear = Button(credentials,text="Clear",background="#FF3134",font="gothic, 12 bold",justify='center',bd=2,fg="white",command=lambda: clear_g(entry_id_g,entry_pass_g))
            up_clear.place(x=160,y=220)
        
        #---------------------GMAIL WINDOW JISMY VALUES JARHA HY[GMAILID,PASS]-------------------#
        my_str_g_id = StringVar()
        my_str_g_pass = StringVar()    
        
        #-----------------CREDENTIALS button [GMAIL]-----------------#
        global button_credentials_img
        button_credentials_img = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\gcredentials.png")
        button_credentials = Button(newgmailWindow,image=button_credentials_img,highlightthickness = 0, bd = 0,command = credentials_g)
        button_credentials.place(x=515,y=360)
        
        #-------------------GMAIL WINDOW THREADING[FUNCTION]-------------------#
        def threadinggmail(): 
        # Call work function
            if textg.get("1.0",'end-1c') == "":
                messagebox.showwarning("Message Box", "Write your Text",parent=newgmailWindow)
            else:
                t2=Thread(target=submitFunctiongmail) 
                t2.start()
        
        #----------------------SUBMIT_BUTTON[GMAIL]-----------------#
        global button_submit_img_G
        button_submit_img_G = PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\gsendbtn.png")
        button_submit_G = Button(newgmailWindow,image=button_submit_img_G,bd = 0,highlightthickness=0,command=threadinggmail)
        button_submit_G.place(x=720,y=318)

        #-----------------------GMAIL WINDOW RESULT-DEPICTING-TEXTBOX-----------------------#
        g = ttk.Style()
        g.theme_use('clam')
        vhg=Scrollbar(newgmailWindow,orient='vertical',background="black")
        vhg.place(height=575,x=1335,y=61)
        tree = ttk.Treeview(newgmailWindow, column=("c1", "c2"), show='headings',yscrollcommand=vhg.set)
        vhg.config(command=tree.yview)

        tree.column("# 1", anchor=CENTER,width=242)
        tree.heading("# 1", text="Gmail-ID")
        
        tree.column("# 2", anchor=CENTER,width=141)
        tree.heading("# 2", text="Status")
        tree.place(x=945,y=61,height=575)
        
        save_button = Button(newgmailWindow, text="Save to SQLite",bg="black",fg="white", font="gotic",command=save_to_database)
        save_button.place(x=1100,y=650)

        #---------------------------GMAIL-WORKING SUBMIT [FUNCTION]----------------------#
        def submitFunctiongmail() :
        #--------------------------MESSAGE------------------------#
            if my_str_gs.get() == "Message":
                sleep(int(entry_g.get()))
                global dataframe
                dataframe = pd.read_excel(f'{label_file_explorer_g}')
                
                driver = webdriver.Chrome()
                
                try:
                    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
                    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
                    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
                    driver.implicitly_wait(15)
                    loginBox = driver.find_element(By.XPATH,'//*[@id ="identifierId"]')
                    loginBox.send_keys(id_g.get())
                    nextButton = driver.find_element(By.XPATH,'//*[@id ="identifierNext"]')
                    nextButton.click()

                    sleep(2)

                    passWordBox = driver.find_element(By.XPATH,
                        '//*[@id ="password"]/div[1]/div / div[1]/input')
                    passWordBox.send_keys(pass_g.get())
                    nextButton = driver.find_element(By.XPATH,'//*[@id ="passwordNext"]')
                    nextButton.click()
                    sleep(2)
                    closenoti = driver.find_element(By.XPATH,'//button[@title="Close"]')
                    closenoti.click()
                    driver.implicitly_wait(15)

                    for i in dataframe.index:
                        sleep(2)
                        compose_btn = driver.find_element(by=By.CSS_SELECTOR,value=('.T-I.T-I-KE.L3'))
                        compose_btn.click()
                        sleep(2)
                        to_field = driver.find_element(by=By.CSS_SELECTOR, value=('.agP.aFw'))
                        to_field.send_keys(dataframe.loc[i]['Email'])
                        sleep(2)
                        subject_field = driver.find_element(by=By.CSS_SELECTOR, value=('.aoT'))
                        subject_field.send_keys(subject_text.get())
                        textEntry = driver.find_element(By.XPATH,'//div[@aria-label="Message Body"]')
                        body_content = textg.get("1.0",'end-1c')
                        textEntry.send_keys(body_content)
                        sendButton = driver.find_element(By.XPATH, '//div[@data-tooltip-delay="800"]')
                        sendButton.click()
                        tree.insert("","end",values=(dataframe.loc[i]['Email'],'Done'))
                        sleep(5)
                        
                except Exception as e:
                    tree.insert("","end",values=('',dataframe.loc[i]['Email'],'Failed,Try Again'))
            
            #--------------------------MESSAGE + FILE------------------------#
            if my_str_gs.get() == "Message + Attachment":
                sleep(int(entry_g.get()))
                global dataframe2
                dataframe2 = pd.read_excel(f'{label_file_explorer_g}')
                driver = webdriver.Chrome()
                try:
                    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
                    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
                    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
                    driver.implicitly_wait(15)
                    loginBox = driver.find_element(By.XPATH,'//*[@id ="identifierId"]')
                    loginBox.send_keys(id_g.get())
                    nextButton = driver.find_element(By.XPATH,'//*[@id ="identifierNext"]')
                    nextButton.click()
                    sleep(2)
                    passWordBox = driver.find_element(By.XPATH,
                        '//*[@id ="password"]/div[1]/div / div[1]/input')
                    passWordBox.send_keys(pass_g.get())

                    nextButton = driver.find_element(By.XPATH,'//*[@id ="passwordNext"]')
                    nextButton.click()
                    sleep(2)
                    closenoti = driver.find_element(By.XPATH,'//button[@title="Close"]')
                    closenoti.click()
                    driver.implicitly_wait(15)

                    for i in dataframe2.index:
                        sleep(2)
                        compose_btn = driver.find_element(by=By.CSS_SELECTOR,value=('.T-I.T-I-KE.L3'))
                        compose_btn.click()
                        sleep(2)
                        to_field = driver.find_element(by=By.CSS_SELECTOR, value=('.agP.aFw'))
                        to_field.send_keys(dataframe2.loc[i]['Email'])
                        sleep(2)
                        subject_field = driver.find_element(by=By.CSS_SELECTOR, value=('.aoT'))
                        subject_field.send_keys(subject_text.get())
                        textEntry = driver.find_element(By.XPATH,'//div[@aria-label="Message Body"]')
                        body_content = textg.get("1.0",'end-1c')
                        textEntry.send_keys(body_content)
                        sleep(5)
                        filevar = driver.find_element(By.NAME,"Filedata")
                        filevar.send_keys(f'{label_choose_file_g}') 
                        sendButton = driver.find_element(By.XPATH, '//div[@data-tooltip-delay="800"]')
                        sendButton.click()
                        sleep(2)
                        tree.insert("","end",values=(dataframe2.loc[i]['Email'],'Done'))
                        
                except Exception as e:
                    tree.insert("","end",values=('',dataframe2.loc[i]['Email'],'Failed,Try Again'))
    #GMAILEND WINDOW ENDING---------------------------------------------------------#

    #-------------------------------INSTA WINDOW INITITALISING[FUNCTION]--------------------------#
    def instawindow():
        newwindowinsta = Toplevel()
        newwindowinsta.iconbitmap("D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico")
        newwindowinsta.title("Marketing Medium[Instagram Initializer]")
        newwindowinsta.geometry('1366x768')
        global image_path_i
        image_path_i = PhotoImage(file = "D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\instabg.png")
        bg_image_i = Label(newwindowinsta,image = image_path_i)
        bg_image_i.place(relheight = 1,relwidth= 1)
        
        #--------------------DATE-I-----------------------#
        datei = dt.datetime.now()
        global dateupperlefti
        dateupperlefti = Label(newwindowinsta, text=f"{datei:%Y-%m-%d}", font="roboto, 15 bold",bg="black",fg="white")
        dateupperlefti.place(x=153, y=7)

        #--------------------CLOCK-TIMER-I[FUNCTION]-----------------------#
        def update_time_i():
            current_timei = strftime('%I:%M:%S %p')
            clockimgrighti.config(text=current_timei)
            newwindowinsta.after(1000, update_time_i)
            
        #--------------------CLOCK-TIMER-I-----------------#
        global clockimgrighti
        clockimgrighti = Label(newwindowinsta, text="", font="roboto, 15 bold",bg="black",fg="white")
        clockimgrighti.place(x=1130, y=7)
        update_time_i()

        #--------------------------------INSTA-LOGIN--------------------------------#
        def combine_funcs_i(*funcs): 
            def inner_combined_func_i(*args,**kwargs): 
                for f in funcs:  
                    f(*args, **kwargs)  
            return inner_combined_func_i 

        #-----------------------INSTA WINDOW MESSAGEBOX[FUNCTION]---------------------------#
        def onClick_i():
            if id_i.get() == ""  or pass_i.get() == "":
                messagebox.showwarning("Message Box", "Entry valid credentials",parent=newwindowinsta)
            else:
                messagebox.showinfo("Message Box","Credentials saved",parent=newwindowinsta)

        #-----------------------INSTA WINDOW INSTAID LABEL---------------------------#
        global iid
        iid = Label(newwindowinsta,text="Phone number, username or email address",fg="gray",font="roboto, 10 bold",bd="0",highlightthickness=0,background="white")
        iid.place(x=63,y=210)

        #-----------------------INSTA WINDOW INSTAID ENTRY---------------------------#
        global id_i
        id_i = StringVar()
        entry_id_i = Entry(newwindowinsta,bg="#FAFAFA",textvariable=id_i,font="roboto 12",bd="3")
        entry_id_i.focus()
        entry_id_i.place(x=63,y=240,width=311,height=30)

        #-----------------------INSTA WINDOW PASSWORD LABEL---------------------------#
        global ipassword
        ipassword = Label(newwindowinsta,fg="gray",text="Password",font="roboto, 10 bold",bd=0,highlightthickness=0,background="white")
        ipassword.place(x=63,y=290)

        #-----------------------INSTA WINDOW INSTAID ENTRY---------------------------#
        global pass_i
        pass_i = StringVar()
        global entry_pass_i
        entry_pass_i = Entry(newwindowinsta,show="*",textvariable=pass_i,bg="#FAFAFA",font="roboto 12",bd="3")
        entry_pass_i.place(x=63,y=320,width=311,height=30)

        #-----------------------INSTA WINDOW CREDENTIALS SAVE[FUNCTION]---------------------------#
        global instaloginbtn
        instaloginbtn = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\loginsta.png")
        upi_save = Button(newwindowinsta,image=instaloginbtn,bd=0,highlightthickness=0,command=combine_funcs_i(lambda:(my_str_i_id.set(id_i.get())),lambda:(my_str_i_pass.set(pass_i.get())),lambda:(onClick_i())))
        upi_save.place(x=63,y=390)

        #---------------------INSTA WINDOW JISMY VALUES JARHA HY[INSTAID,PASS]-------------------#
        my_str_i_id = StringVar()
        my_str_i_pass = StringVar()   

        #---------------------------------INSTA BROWSE FOLDER----------------------------------#
        def f():
            global folder_path
            folder_path = filedialog.askdirectory(title="Select a Folder",parent=newwindowinsta)
            global folder_name
            folder_name = folder_path.split("/")[-1]
        
        def fsuc():
            if folder_path:
                messagebox.showinfo("Message Box","Folder got updated",parent=newwindowinsta)

        #------------------------INSTA MAIN WORKING[FUNCTION]----------------------------#
        def s():
            try:
                upload_files_path = os.path.join(os.path.abspath(folder_path + "/../"),folder_name)
                driver = webdriver.Chrome()
                driver.maximize_window()
                driver.implicitly_wait(20)

                driver.get("https://www.instagram.com/")

                my_email=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
                my_email.send_keys(id_i.get())

                my_password=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
                my_password.send_keys(pass_i.get())

                login=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
                login.click()

                sleep(10)
            
                upload=driver.find_element(By.XPATH,"//*[@aria-label='New post']")
                upload.click()
                sleep(10)
                com = driver.find_element(By.XPATH,"//button[text()='Select from computer']")
                com.click()
                for index, upload_item in enumerate(os.listdir(upload_files_path)):
                    sleep(5)
                    pyautogui.typewrite(f"{upload_files_path}\{upload_item}")
                    sleep(5)
                    pyautogui.press('enter')
                    if index+1 !=len(os.listdir(upload_files_path)):
                        
                        driver.find_element(By.XPATH,"//*[@aria-label='Open media gallery']").click()
                        driver.find_element(By.XPATH,"//*[@aria-label='Plus icon']").click()

                driver.find_element(By.XPATH,"//div[text()='Next']").click()
                
                driver.find_element(By.XPATH,"//div[text()='Next']").click()
                sleep(5)
                cc = driver.find_element(By.XPATH,"//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r']")
                cc.send_keys(texti.get())
                sleep(2)
                driver.find_element(By.XPATH,"//div[text()='Share']").click()
                WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.XPATH,"//div[text()='Post shared']"),"Post shared"))
                sleep(5)
                driver.find_element(By.XPATH,"//*[@aria-label='Close']").click()
                driver.refresh()
                sleep(2)
                global sl
                sl = Label(newwindowinsta,text="Post shared",fg="white",bg="black",font="roboto, 12")
                sl.place(x=1005,y=135)
                
            except Exception as e:
                global fl
                fl = Label(newwindowinsta,text="Post couldn't be shared",fg="white",bg="black",font="roboto, 12")
                fl.place(x=1155,y=135)
                
        #------------------------------------INSTA-BROWSEF[BUTTON]------------------------------------#
        global button_browse_file_img_i
        button_browse_file_img_i = PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\browsef.png")
        button_choose_file_g = Button(newwindowinsta,image=button_browse_file_img_i,highlightthickness = 0, bd = 0,command=combine_funcs(lambda:(f()),lambda:(fsuc())))
        button_choose_file_g.place(x=643,y=270)
        global button_submit_img_I
        button_submit_img_I = PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\sendi.png")
        
        def delete_label_text():
            sl.config(text="")
        def delete_label_text_fl():
            fl.config(text="")

        #------------------------------------INSTA-THREADING-----------------------------------#
        def threadinginsta(): 
            messagebox.showinfo("Message Box", "Please wait until the automation not get's to an end",parent=newwindowinsta)
            t2=Thread(target=s) 
            t2.start()
            newwindowinsta.after(3000, delete_label_text)
            newwindowinsta.after(3000, delete_label_text_fl)
                                        
        #--------------------------------INSTA-SUBMIT-BUTTON----------------------------------#
        global button_submit_G
        button_submit_G = Button(newwindowinsta,image=button_submit_img_I,bd = 0,highlightthickness=0,command=threadinginsta)
        button_submit_G.place(x=609,y=515)

        #--------------------------CAPTION IWINDOW INITIALIZER[FUNCTION]------------------------#
        def openNewWindow_ic():
            newWindow_ic = Toplevel()
            newWindow_ic.iconbitmap("D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico")
            newWindow_ic.title("New Window")
            newWindow_ic.geometry("200x200")
            #-----------------------CAPTION IWINDOW CLICK HERE ARGS[FUNCTION]-----------------#
            def combine_funcs(*funcs): 
                def inner_combined_func(*args, **kwargs): 
                    for f in funcs:  
                        f(*args, **kwargs)  
                return inner_combined_func
            
            #----------------SELECT TYPE IWINDOW MESSAGEBOX[FUNCTION]-------------------#
            def onClick_ic():
                if texti.get() == "":
                    messagebox.showwarning("Message Box", "Please write your caption!",parent=newWindow_ic) 
                else:
                    messagebox.showinfo("Message Box", "Caption is saved.",parent=newwindowinsta) 
                    newWindow_ic.destroy()
                    
            #-----------------------INSTA WINDOW PASSWORD LABEL---------------------------#
            global icaption
            icaption = Label(newWindow_ic,fg="gray",text="Enter your caption ⬇",justify="center",font="roboto, 10 bold",bd=0,highlightthickness=0)
            icaption.place(x=5,y=0)

            #-------------------CAPTION-ENTRYBOX-[GMAIL]------------------#
            global vi
            vi=Scrollbar(newWindow_ic,orient='horizontal',bg="darkgray")
            vi.place(width=190,x=0,y=140)
            global texti
            texti = StringVar()
            global entry_texti
            entry_texti = Entry(newWindow_ic, textvariable=texti,font=("roboto, 15"),bg="black",fg="white",xscrollcommand=vi.set,width=17,bd=4)
            entry_texti.place(x=0,y=18,height=120)
            entry_texti.focus()
            vi.config(command=entry_texti.xview)
            
            #-----------------------------CAPTION-SAVE-BUTTON-----------------------------------#
            global up_save
            up_save = Button(newWindow_ic,text="Save",bg="#0095F6",fg="white",font="roboto, 12 bold",justify='center',bd=2,command=combine_funcs(lambda:(my_str_g_id.set(texti.get())),lambda:(onClick_ic())))
            up_save.place(x=80,y=170)

        #--------------------------CAPTION KHI VALUE JISMY JARHI HY[INSTA]------------------------#  
        my_str_g_id = StringVar()

        #-----------------CAPTION-SAVE-BUTTON-NEW-WINDOW-[INSTA]-------------------------#
        global btn_ty
        btn_ty= PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\captionbtn.png")
        imgbtnty = Button(newwindowinsta,image=btn_ty,highlightthickness = 0, bd = 0,command=openNewWindow_ic)
        imgbtnty.place(x=560, y=523)
    #--------------------------------INSTA-WINDOW-END-----------------------------------#

    def hashtags():
        # Create the main window
        hash = Toplevel()
        hash.title("Hash Tags Finder")
        hash.iconbitmap('D:\MarketingMedium\env_tkinter\Mainfolder\images\mmlogosmall.ico')
        hash.maxsize(width=550, height=500)
        hash.minsize(width=550, height=500)

        # Load image for the header
        global imghead
        imghead = ImageTk.PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\hashtag.jpg")

        # Create and place the header label
        head = Label(hash, image=imghead)
        head.place(x=-40, y=-12)

        # Variables for user input
        user_name = StringVar()

        def clear():
            # Clear the Entry and ScrolledText widgets
            ac.delete(0, END)
            ac.insert(0, "Your Keyword")
            msge.delete("1.0", END)
            messagebox.showinfo("Clear", "Clear Data Successfully", parent=hash)

        def removeValue(event):
            # Remove default text when clicking on the Entry widget
            event.widget.delete(0, 'end')

        def findhashtag():
            # Find hashtags based on user input
            msge.delete("1.0", END)
            if len(ac.get()) == 0 or ac.get() == "Your Keyword":
                messagebox.showerror("Error", "Enter Your Keyword", parent=hash)
            else:
                try:
                    keyword = user_name.get().replace(" ", '')
                    url = f"http://best-hashtags.com/hashtag/{keyword}/"
                    messagebox.showinfo("Clear", "We Are Finding Best Results", parent=hash)
                    res = requests.get(url)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    res = soup.find_all('p1')
                    res = str(res)
                    if "[<p1>" in res or "</p1>]" in res:
                        res = res.replace("[<p1>", "")
                        res = res.replace("</p1>]", "")
                        res = res.replace("#bhfyp", "#marketingmedium")
                    msge.insert(END, f"{res}\n")

                except:
                    msge.insert(END, "Something Wrong, Plz Try Again\n")

        def findhashtagThread():
            # Run findhashtag in a separate thread
            t1 = Thread(target=findhashtag)
            t1.start()

        def copy():
            # Copy the content of ScrolledText to clipboard
            if len(msge.get("1.0", "end-1c")) == 0:
                messagebox.showerror("Error", "Text Box Is Blank", parent=hash)
            else:
                pc.copy(msge.get("1.0", END))
                messagebox.showinfo("Copy", "Data Successfully Copied", parent=hash)

        # Create Entry widget for user input
        global ac
        ac = Entry(hash, bd=2, width=30, font='sans-serif 12 bold', textvariable=user_name)
        ac.insert(0, "Your Keyword")
        ac.bind("<Button-1>", removeValue)
        ac.place(x=150, y=95)

        # Create buttons for actions
        global enter
        enter = Button(hash, text="Generate Now", font='Verdana 10 bold', bg="#ecad12", command=findhashtagThread)
        enter.place(x=200, y=140)
        
        global clearbtn
        clearbtn = Button(hash, text="Clear", font='Verdana 10 bold', bg="#ecad12", command=clear)
        clearbtn.place(x=330, y=140)

        # Create ScrolledText widget for displaying results
        global msge
        msge = scrolledtext.ScrolledText(hash, undo=True, font='sans-serif 12', bd=3, width="30", wrap='word')
        msge.place(x=10, y=210, height=250)

        # Create button to copy hashtags to clipboard
        global copy_btn
        copy_btn = Button(hash, text="Copy Hashtag", font='Verdana 10 bold', bg="#ecad12", fg="black", command=copy)
        copy_btn.place(x=13, y=465)
    #---------------------------------------HASHTAG-WINDOW-END--------------------------------#

    #--------------------MAIN WINDOW DATE-----------------------#
    date = dt.datetime.now()
    dateupperleft = Label(root, text=f"{date:%Y-%m-%d}", font="Roboto, 17 bold",bg="black",fg="white")
    dateupperleft.place(x=84, y=9)

    #--------------------MAIN WINDOW CLOCK-TIMER-----------------#
    clockimgright = Label(root, text="", font="Roboto, 17 bold",bg="black",fg="white")
    clockimgright.place(x=1151, y=9)
    update_time()

    #-------------------GMAIL-NEW WINDOW BUTTON-----------------------------#
    gmailnewwindow_img = PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\buttonsidegm.png")
    gmailnewwindow = Button(root,image=gmailnewwindow_img,highlightthickness = 0, bd = 0,command=gmailwindow)
    gmailnewwindow.place(x=1217,y=80)

    #-------------------INSTA-NEW WINDOW BUTTON-----------------------------#
    instanewwindow_img = PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\buttonsideinsta.png")
    instanewwindow = Button(root,image=instanewwindow_img,highlightthickness = 0, bd = 0,command=instawindow)
    instanewwindow.place(x=1217,y=160)

    #-------------------HASH-NEW WINDOW BUTTON-----------------------------#
    hashnewwindow_img = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\hashimg.png")
    hashnewwindow = Button(root,image=hashnewwindow_img,highlightthickness = 0, bd = 0,command=hashtags)
    hashnewwindow.place(x=1217,y=240)

    # #-----------------MAIN WINDOW UPLOAD XLSX------------------#
    button_explore_img= PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\uploadxlsx.png")
    button_explore = Button(root,image=button_explore_img,highlightthickness = 0, bd = 0,command=browseFiles)
    button_explore.place(x=550,y=67)

    # #-----------------MAIN WINDOW CHOOSEFILE-DOWN-----------------#
    button_choose_file_img = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\choosefile.png")
    button_choose_file = Button(root,image=button_choose_file_img,highlightthickness = 0, bd = 0,command = choosefile)
    button_choose_file.place(x=480,y=295)

    # #-----------------MAIN WINDOW CLEARDATA-----------------#
    button_cleardata_text = StringVar()
    button_cleardata_img = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\cleardata.png")
    button_cleardata = Button(root,image=button_cleardata_img,textvariable=button_cleardata_text,highlightthickness = 0, bd = 0,command=lambda: clear_data(tree,text))
    button_cleardata.place(x=480, y=370)

    #---------------MAIN WINDOW BUTTON-SUBMIT THREAD[FUNCTION]--------------------#
    def threading(): 
        # Call work function 
        t1=Thread(target=submitFunction) 
        t1.start()
        messagebox.showinfo("Message Box","Wait until the automation gets over",parent=root)
    #--------------------------------MAIN WINDOW SUBMIT-------------------------------------#
    button_submit_img = PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\submit.png")
    button_submit = Button(root,image=button_submit_img,bd = 0,highlightthickness=0,command=threading)
    button_submit.place(x=670,y=320)

    #-----------------MAIN WINDOW SELECT-TYPE-NEW-WINDOW-------------------------#
    btn_tp= PhotoImage(file="D:\\MarketingMedium\\env_tkinter\\Mainfolder\\images\\Selectype.png")
    imgbtntp = Button(root,image=btn_tp,highlightthickness = 0, bd = 0,command=openNewWindow)
    imgbtntp.place(x=290, y=295)

    # #-------------------PLEASESELECT-DOWN-LISTBOX-[MAIN WINDOW]------------------#
    downtxt_w=Scrollbar(root,orient='horizontal',background="black")
    downtxt_w.place(width=791,x=0,y=631)
    downtxtpls_w=Listbox(root,bg="lightgray", font=("gothic, 16 bold"), xscrollcommand=downtxt_w.set,width=65,height=6,bd=4)
    downtxt_w.config(command=downtxtpls_w.xview)
    downtxtpls_w.insert("end","Please Select the Type,Excel file and if necessary choose the attachment")
    downtxtpls_w.place(x=0,y=469)

    # #---------MAIN WINDOW SELECT CODE--------------------#
    selected_elem = IntVar(value='Select Code')
    combobox = ttk.Combobox(root,font=('Roboto','15'), textvariable = selected_elem,width=10)
    combobox['values'] = ('+91', '+86', '+1')
    combobox.place(x=290,y=72,height=33)
    combobox.bind('<<ComboboxSelected>>', cc)

    # #------------MAIN WINDOW SLEEP-COUNTDOWN------------------#
    number = IntVar()
    entry = Entry(root, textvariable=number, justify='center',font="Roboto 10")
    entry.place(x=450,y=72,width=50)
    buttonframe = Frame(entry)
    buttonframe.pack(side=RIGHT)
    buttonup = Button(buttonframe, text="▲", font="Roboto 5", command=up,background="#1F4F4F",foreground="white")
    buttonup.pack(side=TOP,pady=2)
    buttondown = Button(buttonframe, text="▼", font="Roboto 5", command=down,background="#1F4F4F",foreground="white")
    buttondown.pack(side=BOTTOM,pady=2)

    # #-------------------MAIN WINDOW MESSAGE-TEXTBOX------------------#
    v=Scrollbar(root,orient='vertical',background="black")
    v.place(height=117,x=705,y=143)
    text=Text(root, font=("Roboto, 17"), yscrollcommand=v.set,width=31,height=4,bd=4)
    v.config(command=text.yview)
    text.place(x=290,y=143)

    #-----------------------MAIN WINDOW RESULT-DEPICTING-TEXTBOX-----------------------#
    s = ttk.Style()
    s.theme_use('clam')
    vh=Scrollbar(root,orient='vertical',background="black")
    vh.place(height=582,x=1176,y=64)
    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings',yscrollcommand=vh.set)
    vh.config(command=tree.yview)

    tree.column("# 1", anchor=CENTER,width=117)
    tree.heading("# 1", text="Name")
    tree.column("# 2", anchor=CENTER,width=117)
    tree.heading("# 2", text="Contact")
    tree.column("# 3", anchor=CENTER,width=117)
    tree.heading("# 3", text="Status")

    tree.place(x=820,y=64,height=583)

    #--------------------------------Main window marquee--------------------------------#

    lbm = Label(root, text="If you have any queries or suggestion contact me on +91 9819209763 and refer the above mentioned link ⬆ to know more on how to use the app?",bg="#1F4F4F",fg="white",font=('Roboto',16))
    lbm.place(x=0,y=662,width=1366,height=45)
    lbm.after(1000,lambda:marquee_fun(lbm,10,30,1368,1366,'left',3))


    #--------------------------------marquee function------------------------------------#
    def marquee_fun(widget,widget_w,widget_h,total_w,total_h,direction,speed,position=1368):
        if direction=='right':
            if position>=total_w-widget_w:
                position=0
            position = position + speed
            widget.place(x=position)
        elif direction=='left':
            if position<0:
                position=total_w-widget_w
            position = position - speed
            widget.place(x=position)
            
        widget.after(50, lambda:marquee_fun(widget,widget_w,widget_h,total_w,total_h,direction,speed,position))


    #-------------------------------MAIN WINDOW DATABASE[FUNCTION---------------------------#
    def save_to_database_w():
        # Connect to SQLite database (creates the database file if it doesn't exist)
        conn = sqlite3.connect('treeview_data_w1.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS treeview_data_w1 (
                id INTEGER PRIMARY KEY,
                Name TEXT ,
                Contact INTEGER ,
                Status TEXT
            )
        ''')

        # Get data from Treeview
        if my_str.get() == "Message" or my_str.get() == "Image and Video" or my_str.get() == "Document" or my_str.get() == "Document":
            dataw = []
            for itemw in tree.get_children():
                values = tree.item(itemw, 'values')
                dataw.append((values[1],values[2]))

            # Save data to SQLite table
            
            cursor.executemany('INSERT INTO treeview_data_w1 (Contact, Status) VALUES (?,?)', dataw)
        if my_str.get() == "Group Message" or my_str.get() == "Group Message + Document":
            dataw = []
            for itemw in tree.get_children():
                values = tree.item(itemw, 'values')
                dataw.append((values[0],values[2]))

            # Save data to SQLite table
            
            cursor.executemany('INSERT INTO treeview_data_w1 (Name, Status) VALUES (?,?)', dataw)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    save_db = PhotoImage(file="D:\MarketingMedium\env_tkinter\Mainfolder\images\savedb.png")
    save_button_w = Button(root,image=save_db,bd=0,highlightthickness=0,command=save_to_database_w)
    save_button_w.place(x=290, y=370)
    
    #Define a callback function
    def callback(url):
        webbrowser.open_new_tab(url)
    guidetbn = PhotoImage(file="D:\MarketingMedium\Mainfolder\images\guide.png")

    #Create a Label to display the link
    link = Button(root,image=guidetbn,highlightthickness = 0, bd = 0,cursor="hand2")
    link.place(x=1217,y=610)
    link.bind("<Button-1>", lambda e:
    callback("file:///D:/MarketingMedium/Mainfolder/video.html"))

    root.mainloop()


