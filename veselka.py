from tkinter import *


class Veselka:

    def __init__(self, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        l["text"] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


d_colors = {
    "red": "#ff0000",
    'orange': "#ff7d00",
    'yellow': "#ffff00",
    'green': "#00ff00",
    'light_blue': "#007dff",
    'blue': "#0000ff",
    'purple': "#7d00ff"
}

root = Tk()
root.geometry("300x300+300+300")
l = Label(root, width=30, justify="center")
e = Entry(root, width=30, justify="center")

l.pack()
e.pack()

# for k, v in d_colors.items():
#     Button(root, bg=v, command=lambda text=k, hex=v: colors(text, hex)).pack(fill=X)


for k, v in d_colors.items():
    Veselka(k, v)

root.mainloop()
