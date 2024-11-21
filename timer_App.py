import tkinter as tk
import time
from tkinter import ttk
import winsound

count = False

def count_down():
    global count
    count = True

    hour_h, minute_m, second_s = expect_h.get(), expect_m.get(), expect_s.get()

    total_sec = hour_h * 3600 + minute_m * 60 + second_s

    while total_sec > -1 and count:
        if second_s >= 0:
            if second_s > 9:
                seconds.set(f' {second_s} ')
                second_s -= 1
                total_sec -= 1
                root.update()
                time.sleep(1)
            else:
                seconds.set(f' 0{second_s} ')
                second_s -= 1
                total_sec -= 1
                root.update()
                time.sleep(1)

        elif minute_m > 0:
            if minute_m > 9:
                minutes.set(f' {minute_m} ')
                minute_m -= 1
                second_s = 59
            else:
                minutes.set(f' 0{minute_m} ')
                minute_m -= 1
                second_s = 59

        elif hour_h > 0:
            if hour_h > 9:
                hour_h -=1
                hours.set(f' {hour_h} ')
                minute_m = 59
            else:
                hour_h -= 1
                hours.set(f' 0{hour_h} ')
                minute_m = 59

    print(total_sec)
    if total_sec == -1:
        winsound.PlaySound(r'ur path to sad-meow-song.wav', winsound.SND_ASYNC)


def edit():
    toplvl = tk.Toplevel()
    toplvl.config(padx=10, pady=10)

    hour_label = tk.Label(toplvl, text='Часы : ')
    min_label = tk.Label(toplvl, text='Минуты : ')
    sec_label = tk.Label(toplvl, text='Секунды : ')

    hour_label.grid(column=0, row=0, sticky="w")
    min_label.grid(column=0, row=1, sticky="w")
    sec_label.grid(column=0, row=2, sticky="w")

    hours_entry = tk.Entry(toplvl)
    minutes_entry = tk.Entry(toplvl)
    seconds_entry = tk.Entry(toplvl)

    hours_entry.grid(column=1, row=0, padx=10, sticky="e")
    minutes_entry.grid(column=1, row=1, padx=10, sticky="e")
    seconds_entry.grid(column=1, row=2, padx=10, sticky="e")

    send_button = ttk.Button(toplvl,
                             text='Подтвердить',
                             command= lambda: send(hours_entry.get(),
                                          minutes_entry.get(),
                                          seconds_entry.get(), toplvl)
                             )
    send_button.grid(columnspan=2, row=3, pady=10)

def send(h, m, s, w):
    global count
    count = False

    try:
        hour = int(h)
    except:
        hour = 0

    try:
        minute = int(m)
    except:
        minute = 0

    try:
        second = int(s)
    except:
        second = 0

    if 25 > hour > 9:
        hours.set(f' {hour} ')
    elif hour < 10:
        hours.set(f' 0{hour} ')
    else:
        hour = 24
        hours.set(f' {hour} ')

    if 60 > minute > 9:
        minutes.set(f' {minute} ')
    elif minute < 10:
        minutes.set(f' 0{minute} ')
    else:
        minute = 59
        minutes.set(f' {minute} ')

    if 60 > second > 9:
        seconds.set(f' {second} ')
    elif second < 10:
        seconds.set(f' 0{second} ')
    else:
        second = 59
        seconds.set(f' {second} ')

    expect_h.set(hour)
    expect_m.set(minute)
    expect_s.set(second)

    w.destroy()


root = tk.Tk()

expect_h = tk.IntVar()
expect_m = tk.IntVar()
expect_s = tk.IntVar()

hours = tk.StringVar(value='00')
minutes = tk.StringVar(value='00')
seconds = tk.StringVar(value='00')

hours_label = tk.Label(root,
                       font=('Arial', 50),
                       textvariable=hours)
col1_label = tk.Label(root,
                      font=('Arial', 50),
                      text=':')
minutes_label = tk.Label(root,
                         font=('Arial', 50),
                         textvariable=minutes)
col2_label = tk.Label(root,
                      font=('Arial', 50),
                      text=':')
seconds_label = tk.Label(root,
                         font=('Arial', 50),
                         textvariable=seconds)


hours_label.grid(column=0, row=0)
col1_label.grid(column=1, row=0)
minutes_label.grid(column=2, row=0)
col2_label.grid(column=3, row=0)
seconds_label.grid(column=4, row=0)


button_frame = tk.Frame(root)
button_frame.grid(column=0, row=1, columnspan=5)

start_button = ttk.Button(button_frame,
                          text='Начать',
                          command=count_down)
edit_button = ttk.Button(button_frame,
                         text='Изменить',
                         command=edit)

start_button.grid(column=0, row=0, padx=5)
edit_button.grid(column=1, row=0, padx=5)

root.mainloop()
