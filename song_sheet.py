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
    if r.status_code==200:
        tk.messagebox.showinfo(title='响应成功',message='让我们畅游在id为'+id+'的歌单的世界吧！')
        top.destroy()
        #关闭旧窗口后，建立新的歌单显示窗口
        window = tk.Tk()
        window.title('假网易云音乐真简陋播放器')
        window.geometry('1600x1000')
        songs = []
        artist = []
        popularity = []
        album = []
        playTime = []
        song_id = []
        d = {}
        #获取歌单封面图片链接，下载并使用PIL库处理为tkinter接受的格式后，将其放置在页面左上角
        cover_image_url = response_dict['result']["coverImgUrl"]
        image = requests.get(cover_image_url)
        with open(id+'.jpg', 'wb') as code:  
            code.write(image.content)
        img_open = Image.open(id+'.jpg')
        img_open = img_open.resize((90,95),Image.ANTIALIAS)
        img_ = ImageTk.PhotoImage(img_open)
        tk.Label(window, image = img_,width=90,height=95).pack(anchor='nw')
        #将json文件里的歌手，歌单，播放时长，热度，专辑名等信息放在对应列表，并将歌曲id与编号使用字典建立联系
        for i in range(len(response_dict['result']['tracks'])):
        #print(response_dict['result']['tracks'][0])
            #print(response_dict['result']['tracks'][i]['popularity'])
            popularity.append(response_dict['result']['tracks'][i]['popularity'])
            #print(response_dict['result']['tracks'][i]['id'])
            songs.append(response_dict['result']['tracks'][i]['name'])
            song_id.append(response_dict['result']['tracks'][i]['id'])
            d[i] = response_dict['result']['tracks'][i]['id']
            #print(d)
            #print(response_dict['result']['tracks'][i]['artists'][0]['name'])
            artist.append(response_dict['result']['tracks'][i]['artists'][0]['name'])
            #print(response_dict['result']['tracks'][i]['album']['name'])
            album.append(response_dict['result']['tracks'][i]['album']['name'])
            #print(response_dict['result']['tracks'][i]['bMusic']['playTime'])
            try:
                playTime.append(int(response_dict['result']['tracks'][i]['bMusic']['playTime']/1000))
            except:
                playTime.append('该歌曲时长未找到')
        #显示歌单播放次数
        tk.Label(window,text='歌单播放次数:'+''+str(response_dict['result']['playCount'])).place(x=300,y=50)
        # 获取要播放的歌曲序号
        songid = tk.StringVar()
        songiid=tk.Entry(window,textvariable=songid)
        songiid.place(x=500,y=20)
        
        tk.Label(window,text='请输入歌曲序号：').place(x=350,y=20)
        #建立text组件，以显示歌单基本信息
        textbox = tk.Text(window,width=250,height=50,bg='SlateBlue')
        scr = Scrollbar(window)
        scr.config(command=textbox.yview)
        textbox.config(yscrollcommand=scr.set)
        textbox.place(x=0,y = 100)
        scr.place(x=1585,y=100)

        def download():
            try:
                sid = songid.get()
                durl = 'http://music.163.com/song/media/outer/url?id='+str(d[int(sid)])+'.mp3'
                f = requests.get(durl)  
                with open(sid+'.mp3', 'wb') as code:  
                    code.write(f.content)
            except:
                tk.messagebox.showerror(title= '下载失败',message='该歌曲无版权或为VIP歌曲')
        bt_download=tk.Button(window,text='下载',command=lambda : download())
        bt_download.place(x=700,y=20)
        #定义播放函数，与放置播放按钮
        def play():
            try:
                sid = songid.get()
                durl = 'http://music.163.com/song/media/outer/url?id='+str(d[int(sid)])+'.mp3'
                f = requests.get(durl)  
                with open('sid'+'.mp3', 'wb') as code:  
                    code.write(f.content)
                track = pygame.mixer.music.load('sid'+'.mp3')
                pygame.mixer.music.play()
            except:
                tk.messagebox.showerror(title= '播放失败',message='该歌曲无版权或为VIP歌曲，请前往拥有版权的音乐网站在线播放。')
        bt_play=tk.Button(window,text='播放',command=lambda : play())
        bt_play.place(x=750,y=20)
bt_zr=tk.Button(top,text='载入歌单',command=lambda : zairu())
bt_zr.place(x=350,y=180)

top.mainloop()
