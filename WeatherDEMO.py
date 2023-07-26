from tkinter import *
from tkinter import ttk, messagebox
import requests
import time
import geonamescache # need to be worked with databases or additional API

API = "512a30300eeecccbe7d876e6261c1b75"
URL = 'http://api.openweathermap.org/data/2.5/weather'
GC = geonamescache.GeonamesCache() # to get Cities data for autofill


def start():
    location = pole1.get()
    print(f"І прийде велика інфа.")
    # messagebox.showinfo(message=location)
    params = {'APPID': API, 'q': location, 'units': 'metric'}
    result = requests.get(URL, params=params)
    weather = result.json()
    # time_Sunrise = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(int(weather["sys"]["sunrise"])))
    print(weather)
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}' \
                   f'\nCountry: {str(weather["sys"]["country"])}' \
                   f'\nWind speed: {weather["wind"]["speed"]} metr per second' \
                   f'\nSunrise: {time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(int(weather["sys"]["sunrise"])))}' \
                   f'\nSunset: {time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(int(weather["sys"]["sunset"])))}'

def autofill_cities():
    entered_text = pole1.get()
    suggest = []
    cities = GC.get_cities()
    for city in cities:
        if entered_text.lower() in city['name'].lower():
            suggest.append(city["name"])
    pole1["values"] = suggest # in a case of Combobox

def clean_text(event):
    val1.set("")


def text_appear_again(event):
    val1.set("Enter your City")


def color_change(event):
    colorBatton.configure("Custom.TButton", background="blue")



# Полученные данные добавляем в текстовую надпись для отображения пользователю

root = Tk()
root.geometry("600x600+900+200")
root.title("Weather program")  # Назва вікна
root.wm_attributes("-alpha", 0.97)  # прозорість вікна
root.resizable(height=False,width=False)
frame1 = Frame(background="light blue")
frame1.place(relheight=1, relwidth=1)

label = ttk.Label(frame1, text="Have a nice day, by the way, no matter what...", font=14)
label.pack()
# canvas = Canvas(root, bg="#00FFFF") # ДЛя відображення графіку холст
# canvas.pack()
button = ttk.Button(frame1, text="Show the whether, be happy together !!!", style="Custom.TButton",command=start)
button.pack()

val1 = StringVar()
val1.set("Enter your City")

pole1 = ttk.Combobox(frame1, textvariable=val1)
pole1.pack(pady=20)
pole1.bind("<Button-1>", clean_text)
pole1.bind('<<ComboboxSelected>>', lambda _: autofill_cities()) # Подія ComboboxSelected — це віртуальна подія в Tkinter,
# яка запускається, коли елемент вибрано з віджета ttk.Combobox.
# Він конкретно представляє подію вибору елемента зі спадного списку.
frame1.bind("<Button-1>", text_appear_again)

colorBatton = ttk.Style()
colorBatton.configure("Custom.TButton", background="yellow")

button.bind("<Button-1>", color_change)

info = Label(frame1, text="Information",bg='#ffb700', font=40, height=10,width=50)
info.pack()
info.bind("<Button-1>", text_appear_again)
root.mainloop()














