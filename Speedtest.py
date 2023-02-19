import speedtest
import tkinter as tk
import messagebox
from tkinter import *

st=speedtest.Speedtest()

#Window Properties
root=tk.Tk()
root.geometry("600x250+400+80")
root.resizable(False, False)
root.title("Speedtest")
root.configure(background='#154c79')

image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

photo=PhotoImage(file="logo.png")
myimage=Label(image=photo,background='#154c79')
myimage.place(x=5, y=5)

down_speed = st.download()/(1025*1025)
up_speed = st.upload()/(1025*1025)

speed = " "

def button_click(args):
    # global down_speed
    # global up_speed
    if args == 1:
        speed = tk.StringVar(str(st.download()/(1025*1025)))
        
    elif args == 2:
        speed = tk.StringVar(root, str(st.upload()/(1025*1025)))

    # elif args == 3:
    #     st.results.ping
    

    # elif args == 3:
    #     servername=[]
    #     st.get_servers(servername)
    #     messagebox.showinfo(st.results.ping)
        



download_button = tk.Button(root, text='Download Speed', width = 14, font='Candara, 12', 
 background='white', foreground='#154c79', command=lambda:button_click(1)).place(x=50, y=110)

upload_button = tk.Button(root, text='Upload Speed', width = 14, font='Candara, 12', 
 background='white', foreground='#154c79', command=lambda:button_click(2)).place(x=250, y=110)

ping_button = tk.Button(root, text='Ping', width = 14, font='Candara, 12', 
 background='white', foreground='#154c79', command=lambda:button_click(3)).place(x=450, y=110)

dspeed_Label = tk.Label(root, textvariable=speed, 
                        height=0, width=18, font=("Cambria", 26)).place(x=130, y=150)

# option=int(input('''What speed do you want to measure:
# 1) Download Speed

# 2) Upload Speed

# 3) Ping

# Your Choice'''))

# if option==1:
#     messagebox.showinfo(st.download()/(1025*1025),"Mbps")

# elif option==2:
#     print(st.upload()/(1025*1025),"Mbps")

# elif option==3:
#     servername=[]
#     st.get_servers(servername)
#     print(st.results.ping)

# else:
#     print("Please enter correct option")

root.mainloop()