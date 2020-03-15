# Script Name       :song_sheet.py
# Author            :WangHao
# Created time      :15th March 2020
# Last Modified     
# Version           :1.0
# Modification      :

# Description       :crawling playlist information 

import tkinter as tk
import requests


top=tk.Tk()
top.title('歌单初始化页面')
top.geometry('450x400')
tk.Label(top,text='请输入歌单id:').place(x=100,y=180)
playlist=tk.StringVar()
lll=tk.Entry(top,textvariable=playlist)
lll.place(x=180,y=180)
def zairu():
    id=playlist.get()
    url = 'http://music.163.com/api/playlist/detail?id='+id
    r = requests.get(url)
    response_dict = r.json()
    return r.status_code
bt_zr=tk.Button(top,text='载入歌单',command=lambda : zairu())
bt_zr.place(x=350,y=180)

top.mainloop()
