from cgitb import text
from logging import shutdown
import tkinter as myproject
from tkinter.messagebox import showerror

one = myproject.Tk()
one.title("Ben sana yardım için burdayım 😀")
one.geometry("700x200")

user = myproject.Label(text="KULLANICI ADI:")
user.place(x=20,y=10)

y= myproject.StringVar()
user_girisi = myproject.Entry(textvariable=y)
user_girisi.place(x=130,y=10)

kullanici = myproject.Label(text="Şifre GİRİSİ:")
kullanici.place(x=20,y=35)

x= myproject.StringVar()
kullanici_girisi = myproject.Entry(textvariable=x)
kullanici_girisi.place(x=130,y=30)

giris = myproject.Button(text="Giris",command = showerror)
print("False !!!")
giris.place(x=30,y=100)
shutdown
x= myproject.StringVar()
kullanici_girisi = myproject.Entry(textvariable=x)
kullanici_girisi.place(x=200,y=30)


one.mainloop()

one = myproject.mainloop()