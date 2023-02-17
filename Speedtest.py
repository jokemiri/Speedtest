import speedtest
import tkinter as tk
import messagebox

def download_speed():
    print("Button Clicked")

def upload_speed():
    print("Button 2 Clicked")

st=speedtest.Speedtest()

#Window Properties
root=tk.Tk()
root.geometry("600x600+400+80")
root.resizable(False, False)
root.title("Speedtest")
root.configure(background='#154c79')

download_button = tk.Button(root, text='Download Speed', font='Candara, 14', 
 background='white', foreground='#154c79', command=download_speed).place(x=30, y=30)

upload_button = tk.Button(root, text='Upload Speed', font='Candara, 14', 
 background='white', foreground='#154c79', command=upload_speed).place(x=250, y=30)

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