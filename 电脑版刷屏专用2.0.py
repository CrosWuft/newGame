from pynput import mouse, keyboard
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import time
fn='croswuft.cs.txt'
root=tk.Tk()
root.title("信息刷屏Create by CrosWuft")
m=mouse.Controller()
k=keyboard.Controller()
def wrong2():
    tkinter.messagebox.showerror(title='Error', message='请将ico文件放在本文件旁边')
try:
    root.iconbitmap('a.ico')
except:
    pass
    #command=wrong2()
root.geometry("550x200+500+300")
lb=Label(root,text='Create by CrosWuft',bg='red',font=('华文楷体',15))
lb.grid(row=0,column=0)
lb=Label(root,text="请输入要发送的内容：",font=('华文楷体',15))
lb.grid(row=2,column=0)
entry1=Entry(root,font=('Arial',15))
entry1.grid(row=2,column=1)
lb=Label(root,text="请输入要发送的次数：",font=('华文楷体',15))
lb.grid(row=3,column=0)
entry2=Entry(root,font=('Arial',15))
entry2.grid(row=3,column=1)
lb=Label(root,text="请输入要发送的模式：",font=('华文楷体',15))
lb.grid(row=4,column=0)
entry3=Entry(root,font=('Arial',15))
entry3.grid(row=4,column=1)
lb=Label(root,text='(模式不输入或输错为默认)',font=('华文楷体',13))
lb.grid(row=5,column=0)
def wrong():
    tkinter.messagebox.showerror(title='Error', message='请输入正确的次数!')
def anjian():
    m.click(mouse.Button.left)
    try:
        ks = int(entry2.get())
    except:
        command = wrong()
    else:
        if entry3.get()=='one by one' or entry3.get()=='2':
            kv=0
            tkinter.messagebox.showwarning(title='Waring', message='即將开始刷屏，请将鼠标放在要刷屏的信息栏上')
            time.sleep(2)
            for i in range(ks):
                kv=kv+1
                time.sleep(0.1)
                ka=str(kv)
                k.type(entry1.get())
                k.type(" ")
                k.type(ka)
                time.sleep(0.1)
                k.press(keyboard.Key.enter)
                k.release(keyboard.Key.enter)
        elif entry3.get()=='3' or entry3.get()=='get cs':
            with open(fn, 'a') as cr:
                pass
            tkinter.messagebox.showwarning(title='Waring', message='即將开始刷屏，请将鼠标放在要刷屏的信息栏上')
            time.sleep(2)
            with open(fn, 'r+', encoding='utf-8', errors='ignore') as cr:
                lines = cr.readlines()
                for i in range(ks):
                    for line in lines:
                        ast = ''
                        ast += line.rstrip()
                        time.sleep(0.1)
                        k.type(ast)
                        time.sleep(0.3)
                        k.press(keyboard.Key.enter)
                        k.release(keyboard.Key.enter)
        elif entry3.get()=='1':
            time.sleep(2)
            for i in range(ks):
                time.sleep(0.1)
                k.type(entry1.get())
                time.sleep(0.1)
                k.press(keyboard.Key.enter)
                k.release(keyboard.Key.enter)
        else:
            tkinter.messagebox.showwarning(title='Waring', message='即將开始刷屏，请将鼠标放在要刷屏的信息栏上')
            time.sleep(2)
            for i in range(ks):
                time.sleep(0.1)
                k.type(entry1.get())
                time.sleep(0.1)
                k.press(keyboard.Key.enter)
                k.release(keyboard.Key.enter)
btn=Button(root,text="刷屏",font=('华文楷体', 12),relief="raised", width=8, height=1,bd="6",command=anjian)
btn.grid(row=6,column=1)
root.mainloop()


