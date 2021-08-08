# -*- coding:utf -8 -*-
#!/usr/bin/python3
__version__ = '4.2'
from tkinter import *
import tkinter.messagebox as mb
import random
from datetime import datetime

root = Tk()
root.resizable(width=True, height=False)
root.title("Генератор паролей  " + str(__version__))
frm_fields = Frame()
frm_btns = Frame(relief=RAISED, borderwidth=1)
frm_status = Frame()

calculated_text = Entry(master=frm_btns, width=30)

Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
Low = 'qwertyuiopasdfghjklzxcvbnm'
Num = '1234567890'
Spe = '!@#$%^&;*()'

bSymb_var = StringVar()
lSymb_var = StringVar()
nSymb_var = StringVar()
sSymb_var = StringVar()
xSymb_var = StringVar()
mask_var = StringVar()


def getSymb(l):
    if l == "":
        status("Поле символов не может быть пустым", "red")
        return ""
    ls = list(l)
    random.shuffle(ls)
    return random.choice(ls)


def password(argum=0, b=0, c=0):
    status_label['text'] = ""

    Big = bSymb_var.get()
    Low = lSymb_var.get()
    Num = nSymb_var.get()
    Spe = sSymb_var.get()

    Password_mask = mask_var.get()
    psw = []

    for i in Password_mask:
        if i == "c":
            symb = getSymb(Big)
        elif i == "l":
            symb = getSymb(Low)
        elif i == "n":
            symb = getSymb(Num)
        elif i == "s":
            symb = getSymb(Spe)
        elif i == "x":
            symb = xSymb_var.get()
        elif i == "d":
            symb = datetime.now().strftime("%d%m")
        elif i == "D":
            symb = datetime.now().strftime("%d%m%y")
        elif i == "t":
            symb = datetime.now().strftime("%H%M")
        elif i == "T":
            symb = datetime.now().strftime("%H%M%S")
        else:
            status("Некорректный символ в маске - " +
                   i + " заменен на '>'", "red")
            symb = ">"

        psw.append(symb)

    length_entry["text"] = len(''.join(psw))

    calculated_text.delete(0, END)
    calculated_text.insert(0, ''.join(psw))


def copycb(argum=0):
    root.clipboard_clear()
    root.clipboard_append(''.join(calculated_text.get()))
    status("Пароль скопирован в буфер обмена", "blue")


def status(msg, color="black"):
    status_label['foreground'] = color
    status_label['text'] = msg


root.columnconfigure(0, weight=1, minsize=250)
frm_fields.columnconfigure(2, weight=1, minsize=150)
frm_status.columnconfigure(0, weight=1)

bSymb_label = Label(master=frm_fields, text="Заглавные")
bSymb_label.grid(row=0, column=0, sticky="w")
bSymbS_label = Label(master=frm_fields, text="(с)")
bSymbS_label.grid(row=0, column=1, sticky="w")
bSymb_entry = Entry(master=frm_fields, width=32,
                    justify=LEFT, textvariable=bSymb_var)
bSymb_entry.insert(0, Big)
bSymb_entry.grid(row=0, column=2, sticky="ew")
bSymb_res = Button(master=frm_fields, width=1, height=1,
                   text='R', command=lambda: bSymb_var.set(Big))
bSymb_res.grid(row=0, column=3, sticky="w")

lSymb_label = Label(master=frm_fields, text="Прописные")
lSymb_label.grid(row=1, column=0, sticky="w")
lSymbS_label = Label(master=frm_fields, text="(l)")
lSymbS_label.grid(row=1, column=1, sticky="w")
lSymb_entry = Entry(master=frm_fields, width=32,
                    justify=LEFT, textvariable=lSymb_var)
lSymb_entry.insert(0, Low)
lSymb_entry.grid(row=1, column=2, sticky="ew")
lSymb_res = Button(master=frm_fields, width=1, height=1,
                   text='R', command=lambda: lSymb_var.set(Low))
lSymb_res.grid(row=1, column=3, sticky="w")

nSymb_label = Label(master=frm_fields, text="Цифры")
nSymb_label.grid(row=2, column=0, sticky="w")
nSymbS_label = Label(master=frm_fields, text="(n)")
nSymbS_label.grid(row=2, column=1, sticky="w")
nSymb_entry = Entry(master=frm_fields, width=32,
                    justify=LEFT, textvariable=nSymb_var)
nSymb_entry.insert(0, Num)
nSymb_entry.grid(row=2, column=2, sticky="ew")
nSymb_res = Button(master=frm_fields, width=1, height=1,
                   text='R', command=lambda: nSymb_var.set(Num))
nSymb_res.grid(row=2, column=3, sticky="w")

sSymb_label = Label(master=frm_fields, text="Спецсимволы")
sSymb_label.grid(row=3, column=0, sticky="w")
sSymbS_label = Label(master=frm_fields, text="(s)")
sSymbS_label.grid(row=3, column=1, sticky="w")
sSymb_entry = Entry(master=frm_fields, width=32,
                    justify=LEFT, textvariable=sSymb_var)
sSymb_entry.insert(0, Spe)
sSymb_entry.grid(row=3, column=2, sticky="ew")
sSymb_res = Button(master=frm_fields, width=1, height=1,
                   text='R', command=lambda: sSymb_var.set(Spe))
sSymb_res.grid(row=3, column=3, sticky="w")

xSymb_label = Label(master=frm_fields, text="Текст")
xSymb_label.grid(row=4, column=0, sticky="w")
xSymb_label = Label(master=frm_fields, text="(x)")
xSymb_label.grid(row=4, column=1, sticky="w")
xSymb_entry = Entry(master=frm_fields, width=32,
                    justify=LEFT, textvariable=xSymb_var)
xSymb_entry.insert(0, "abc")
xSymb_entry.grid(row=4, column=2, sticky="ew")

dSymb_label = Label(master=frm_fields, text="Дата кор.")
dSymb_label.grid(row=5, column=0, sticky="w")
dSymb_label = Label(master=frm_fields, text="(d)")
dSymb_label.grid(row=5, column=1, sticky="w")
dSymb_entry = Label(master=frm_fields, width=15, justify=LEFT,
                    relief=RIDGE, borderwidth=1,
                    text=datetime.now().strftime("%d%m"))
dSymb_entry.grid(row=5, column=2, sticky="w")

dlSymb_label = Label(master=frm_fields, text="Дата длин")
dlSymb_label.grid(row=6, column=0, sticky="w")
dlSymb_label = Label(master=frm_fields, text="(D)")
dlSymb_label.grid(row=6, column=1, sticky="w")
dlSymb_entry = Label(master=frm_fields, width=15,
                     relief=RIDGE, borderwidth=1,
                     text=datetime.now().strftime("%d%m%y"))
dlSymb_entry.grid(row=6, column=2, sticky="w")

tSymb_label = Label(master=frm_fields, text="Время кор.")
tSymb_label.grid(row=7, column=0, sticky="w")
tSymb_label = Label(master=frm_fields, text="(t)")
tSymb_label.grid(row=7, column=1, sticky="w")
tSymb_entry = Label(master=frm_fields, width=15,
                    relief=RIDGE, borderwidth=1,
                    text=datetime.now().strftime("%H%M"))
tSymb_entry.grid(row=7, column=2, sticky="w")

tlSymb_label = Label(master=frm_fields, text="Время длин.")
tlSymb_label.grid(row=8, column=0, sticky="w")
tlSymb_label = Label(master=frm_fields, text="(T)")
tlSymb_label.grid(row=8, column=1, sticky="w")
tlSymb_entry = Label(master=frm_fields, width=15,
                     relief=RIDGE, borderwidth=1,
                     text=datetime.now().strftime("%H%M%S"))
tlSymb_entry.grid(row=8, column=2, sticky="w")

mask_label = Label(master=frm_fields, text="Маска")
mask_label.grid(row=9, column=0, sticky="w")
mask_entry = Entry(master=frm_fields, width=20, textvariable=mask_var)
mask_entry.insert(0, "clllnnns")
mask_entry.grid(row=9, column=1, columnspan=2, sticky="ew")
help_btn = Button(master=frm_fields, text='?',
                  command=lambda: mb.showinfo(
                      "Справка", "Для генерации пароля необходимо заполнить поле маска в соответствии с требованиями к паролю. Символы для маски указаны около соответствующих полей. Наборы символов можно менять в соответствующих полях. Поля символов можно вернуть к изначальному набору нажатием на кнопку 'R' около поля.\nГорячие клавиши:\nEnter и изменение любого поля - генерирует пароль\nCtrl+c и соответствующая кнопка - копирует пароль в буфер обмена")
                  )
help_btn.grid(row=9, column=3, sticky="w")

display_button = Button(
    master=frm_btns, text="Сгенерить", command=password)
display_button.pack(side=LEFT)

copy_btn = Button(master=frm_btns, width=2, height=1,
                  text='Copy', command=copycb)
copy_btn.pack(side=RIGHT)
calculated_text.pack(fill=X)


status_label = Label(master=frm_status, text="",
                     fg="black", font=("Arial", 8))
status_label.grid(row=0, column=0, sticky="w")
length_entry = Label(master=frm_status, width=3, text="8",
                     relief=RIDGE, borderwidth=1)
length_entry.grid(row=0, column=1, sticky="e")

frm_fields.grid(row=0, column=0, sticky="ew")
frm_btns.grid(row=1, column=0, sticky="ew")
frm_status.grid(row=2, column=0, sticky="ew")

root.update()
root.minsize(root.winfo_width(), root.winfo_height())

bSymb_var.trace_add("write", password)
lSymb_var.trace_add("write", password)
nSymb_var.trace_add("write", password)
sSymb_var.trace_add("write", password)
xSymb_var.trace_add("write", password)
mask_var.trace_add("write", password)
root.bind("<Control-Key-c>", copycb)
root.bind("<Return>", password)
password()
root.mainloop()
