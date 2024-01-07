from tkinter import *
import tkinter.font as font

root = Tk()
root.title("KALKULATOR")
root.geometry("310x400")
root["bg"] = "#CD5B45"

myfont = font.Font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"] = myfont
e["bg"] ="#CD4F39" 
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

def angka(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0,str(sebelum)+str(nilai))

def tambah():
    nomer_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = int(nomer_awal)
    e.delete(0,END)

def kurang():
    nomer_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = int(nomer_awal)
    e.delete(0,END)

def kali():
    nomer_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = int(nomer_awal)
    e.delete(0,END)

def bagi():
    nomer_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = int(nomer_awal)
    e.delete(0,END)

def hapus():
    e.delete(0,END)

def samadengan():
    nomor_akhir = e.get()
    e.delete(0,END)
    if mtk == "penjumlahan":
        e.insert(0,n_awal + int(nomor_akhir))
    elif mtk == "pengurangan":
        e.insert(0,n_awal - int(nomor_akhir))
    elif mtk == "perkalian":
        e.insert(0,n_awal * int(nomor_akhir))
    elif mtk == "pembagian":
        try:
            hitung = n_awal / int(nomor_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError:
            e.insert(0,"TIDAK TERDEFINISI")



btn1 = Button(root,text="1",padx=20,pady=20,command=lambda:angka(1))
btn2 = Button(root,text="2",padx=20,pady=20,command=lambda:angka(2))
btn3 = Button(root,text="3",padx=20,pady=20,command=lambda:angka(3))
btn4 = Button(root,text="4",padx=20,pady=20,command=lambda:angka(4))
btn5 = Button(root,text="5",padx=20,pady=20,command=lambda:angka(5))
btn6 = Button(root,text="6",padx=20,pady=20,command=lambda:angka(6))
btn7 = Button(root,text="7",padx=20,pady=20,command=lambda:angka(7))
btn8 = Button(root,text="8",padx=20,pady=20,command=lambda:angka(8))
btn9 = Button(root,text="9",padx=20,pady=20,command=lambda:angka(9))
btn0 = Button(root,text="0",padx=20,pady=20,command=lambda:angka(0))

plus = Button(root,text="+",padx=20,pady=20,command=tambah)
minus = Button(root,text="-",padx=20,pady=20,command=kurang)
kal = Button(root,text="x",padx=20,pady=20,command=kali)
bag = Button(root,text="/",padx=20,pady=20,command=bagi)
abis = Button(root,text="C",padx=20,pady=20,command=hapus)
sama  = Button(root,text="=",padx=20,pady=20,command=samadengan)

btn1.grid(row=1,column=0,pady=2)
btn2.grid(row=1,column=1,pady=2)
btn3.grid(row=1,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=3,column=0,pady=2)
btn8.grid(row=3,column=1,pady=2)
btn9.grid(row=3,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)

plus.grid(row=1,column=3,pady=2)
minus.grid(row=2,column=3,pady=2)
kal.grid(row=3,column=3,pady=2)
bag.grid(row=4,column=3,pady=2)
abis.grid(row=4,column=0,pady=2)
sama.grid(row=4,column=2,pady=2)

root.mainloop()