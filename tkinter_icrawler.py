from icrawler.builtin import BingImageCrawler,GoogleImageCrawler
import tkinter as tk
from tkinter import messagebox as ms

def google(self,self1,self2):
    crawler = GoogleImageCrawler(storage={"root_dir": self})
    crawler.crawl(keyword=self1, max_num=self2)
def bing(self,self1,self2):
    crawler = BingImageCrawler(storage={"root_dir": self})
    crawler.crawl(keyword=self1, max_num=self2)

root = tk.Tk()
root.title("icrawler")
root.geometry("300x200")

func_table=(google,bing)
name_table=['Google','Bing']
rdo_var=tk.IntVar()

for i in range(len(name_table)):
    rdo=tk.Radiobutton(root,value=i,variable=rdo_var,text=name_table[i],anchor='w')
    rdo.place(x=60+(i*100),y=30)

def getpict():
    func=func_table[rdo_var.get()]
    try:
        sel2 = int(en2.get())
        pass
    except:
        ms.showerror(title="icrawler",message="取得画像数は整数で入力してください")
        en2.insert(0,"")
        
    func(en.get(),en.get(),sel2)
    mes_yn=ms.askyesno(title="icrawler",message='画像ダウンロード完了\n\n続けますか？')
    if mes_yn == True:
        pass
    elif mes_yn==False:
        root.destroy()

lav = tk.Label(text="検索キーワード：")
lav.place(x=30,y=60)
en = tk.Entry(width=20)
en.place(x=150,y=60)

lav2 = tk.Label(text="取得画像数：")
lav2.place(x=30,y=90)
en2 = tk.Entry(width=20)
en2.place(x=150,y=90)

btn = tk.Button(root,text="取得",command=getpict)
btn.place(x=100,y=120)

def breaking():
    root.destroy()

btn1 = tk.Button(root,text='終了',command=breaking)
btn1.place(x=150,y=120)

root.mainloop()
