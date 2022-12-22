click = False
count = 0


def b_click(b):
    global click, count
    if b["text"] == ' ' and click == False:
        b["text"] = 'X'
        click = True
        count += 1
        check_if_won()
    elif b["text"] == ' ' and click == True:
        b["text"] = 'O'
        click = False
        count += 1
        check_if_won()
    else:
        messagebox.showerror('TicTakToe', 'Hey! The box has already been selected!')


def disable_all_buttons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)


def check_if_won():
    global winner
    winner = True

    if btn1["text"] == 'X' and btn2["text"] == 'X' and btn3["text"] == 'X':
        btn1.config(bg='red')
        btn2.config(bg='red')
        btn3.config(bg='red')
        winner = False
        messagebox.showinfo('TikTakToe', 'Congrats! X wins!')
        disable_all_buttons()
    elif btn4["text"] == 'X' and btn5["text"] == 'X' and btn6["text"] == 'X':
        btn4.config(bg='red')
        btn5.config(bg='red')
        btn6.config(bg='red')
        winner = False
        messagebox.showinfo('TikTakToe', 'Congrats! X wins!')
        disable_all_buttons()
    elif btn7["text"] == 'X' and btn8["text"] == 'X' and btn9["text"] == 'X':
        btn7.config(bg='red')
        btn8.config(bg='red')
        btn9.config(bg='red')
        winner = False
        messagebox.showinfo('TikTakToe', 'Congrats! X wins!')
        disable_all_buttons()
    elif btn1["text"] == 'X' and btn4["text"] == 'X' and btn7["text"] == 'X':
        btn1.config(bg='red')
        btn4.config(bg='red')
        btn7.config(bg='red')
        winner = False
        messagebox.showinfo('TikTakToe', 'Congrats! X wins!')
        disable_all_buttons()
    elif btn2["text"] == 'X' and btn5["text"] == 'X' and btn8["text"] == 'X':
        btn2.config(bg='red')
        btn5.config(bg='red')
        btn8.config(bg='red')
        winner = False
        messagebox.showinfo('TikTakToe', 'Congrats! X wins!')
        disable_all_buttons()
    elif btn3["text"] == 'X' and btn6["text"] == 'X' and btn9["text"] == 'X':
        btn3.config(bg='red')
        btn6.config(bg='red')
        btn9.config(bg='red')
        winner = False
        messagebox.showinfo('TikTakToe', 'Congrats! X wins!')
        disable_all_buttons()
    elif btn1["text"] == 'X' and btn5["text"] == 'X' and btn9["text"] == 'X':
        btn1.config(bg='red')
        btn5.config(bg='red')
        btn9.config(bg='red')
        winner = False
        messagebox.showinfo('TikTakToe', 'Congrats! X wins!')
        disable_all_buttons()
    elif btn3["text"] == 'X' and btn5["text"] == 'X' and btn7["text"] == 'X':
        btn3.config(bg='red')
        btn5.config(bg='red')
        btn7.config(bg='red')
        winner = False
        messagebox.showinfo('TikTakToe', 'Congrats! X wins!')
        disable_all_buttons()

    # checking O for the win
    if btn1["text"] == 'O' and btn2["text"] == 'O' and btn3["text"] == 'O':
        btn1.config(bg='red')
        btn2.config(bg='red')
        btn3.config(bg='red')
        winner = True
        messagebox.showinfo('TikTakToe', 'Congrats! O wins!')
        disable_all_buttons()
    elif btn4["text"] == 'O' and btn5["text"] == 'O' and btn6["text"] == 'O':
        btn4.config(bg='red')
        btn5.config(bg='red')
        btn6.config(bg='red')
        winner = True
        messagebox.showinfo('TikTakToe', 'Congrats! O wins!')
        disable_all_buttons()
    elif btn7["text"] == 'O' and btn8["text"] == 'O' and btn9["text"] == 'O':
        btn7.config(bg='red')
        btn8.config(bg='red')
        btn9.config(bg='red')
        winner = True
        messagebox.showinfo('TikTakToe', 'Congrats! O wins!')
        disable_all_buttons()
    elif btn1["text"] == 'O' and btn4["text"] == 'O' and btn7["text"] == 'O':
        btn1.config(bg='red')
        btn4.config(bg='red')
        btn7.config(bg='red')
        winner = True
        messagebox.showinfo('TikTakToe', 'Congrats! O wins!')
        disable_all_buttons()
    elif btn2["text"] == 'O' and btn5["text"] == 'O' and btn8["text"] == 'O':
        btn2.config(bg='red')
        btn5.config(bg='red')
        btn8.config(bg='red')
        winner = True
        messagebox.showinfo('TikTakToe', 'Congrats! O wins!')
        disable_all_buttons()
    elif btn3["text"] == 'O' and btn6["text"] == 'O' and btn9["text"] == 'O':
        btn3.config(bg='red')
        btn6.config(bg='red')
        btn9.config(bg='red')
        winner = True
        messagebox.showinfo('TikTakToe', 'Congrats! O wins!')
        disable_all_buttons()
    elif btn1["text"] == 'O' and btn5["text"] == 'O' and btn9["text"] == 'O':
        btn1.config(bg='red')
        btn5.config(bg='red')
        btn9.config(bg='red')
        winner = True
        messagebox.showinfo('TikTakToe', 'Congrats! O wins!')
        disable_all_buttons()
    elif btn3["text"] == 'O' and btn5["text"] == 'O' and btn7["text"] == 'O':
        btn3.config(bg='red')
        btn5.config(bg='red')
        btn7.config(bg='red')
        winner = True
        messagebox.showinfo('TikTakToe', 'Congrats! O wins!')
        disable_all_buttons()

    if count == 9:
        messagebox.showinfo('TikTakToe', 'Tie')
        disable_all_buttons()


def reset():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global count, click
    click = False
    count = 0
    btn1 = Button(win, text=' ', command=lambda: b_click(btn1), font=("Helvetica", 20))
    btn2 = Button(win, text=' ', command=lambda: b_click(btn2), font=("Helvetica", 20))
    btn3 = Button(win, text=' ', command=lambda: b_click(btn3), font=("Helvetica", 20))

    btn4 = Button(win, text=' ', command=lambda: b_click(btn4), font=("Helvetica", 20))
    btn5 = Button(win, text=' ', command=lambda: b_click(btn5), font=("Helvetica", 20))
    btn6 = Button(win, text=' ', command=lambda: b_click(btn6), font=("Helvetica", 20))

    btn7 = Button(win, text=' ', command=lambda: b_click(btn7), font=("Helvetica", 20))
    btn8 = Button(win, text=' ', command=lambda: b_click(btn8), font=("Helvetica", 20))
    btn9 = Button(win, text=' ', command=lambda: b_click(btn9), font=("Helvetica", 20))

    btn1.grid(row=0, column=0, stick='nwes')
    btn2.grid(row=0, column=1, stick='nwes')
    btn3.grid(row=0, column=2, stick='nwes')
    btn4.grid(row=1, column=0, stick='nwes')
    btn5.grid(row=1, column=1, stick='nwes')
    btn6.grid(row=1, column=2, stick='nwes')
    btn7.grid(row=2, column=0, stick='nwes')
    btn8.grid(row=2, column=1, stick='nwes')
    btn9.grid(row=2, column=2, stick='nwes')


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
win.geometry('450x450')
win.title('TikTakToe by Max')
win.resizable(False, False)

reset()

win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=150)
win.grid_columnconfigure(2, minsize=150)

win.grid_rowconfigure(0, minsize=150)
win.grid_rowconfigure(1, minsize=150)
win.grid_rowconfigure(2, minsize=150)

my_menu = Menu(win)
win.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

win.mainloop()
