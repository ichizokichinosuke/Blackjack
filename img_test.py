import tkinter as tk
from tkinter import ttk
import threading, random
from PIL import Image, ImageTk

def image_resize(width, img):
    resized_image = img.resize((width, int(width*img.size[1]/img.size[0])))
    return resized_image

root = tk.Tk()
root.title("Blackjack")
root.geometry("650x500+500+10")

# tramp_back = tk.PhotoImage(file="../Tramp/others_2.png")
TRAMP_WIDTH = 140
PAD = 3
tramp_back = Image.open("../Tramp/others_2.png")
tramp_back = image_resize(TRAMP_WIDTH, tramp_back)

TRAMP_HEIGHT = tramp_back.size[1]

"""
TEST
"""
imgs = []
for i in range(2):
    new_c = random.randint(1, 13)
    kind = "spade"

    tramp_image = Image.open(f"../Tramp/{kind}_{new_c}.png")
    tramp_image = image_resize(TRAMP_WIDTH, tramp_image)
    tramp_tk = ImageTk.PhotoImage(tramp_image)
    imgs.append(tramp_tk)
    field_canvas = tk.Canvas(root, bg="green", width=TRAMP_WIDTH-PAD, height=TRAMP_HEIGHT-PAD)

    # print(tramp_image)
    x = 250
    y = 20 + i*250

    field_canvas.place(x=x, y=y)
    field_canvas.create_image(0, 0, image=tramp_tk, anchor=tk.NW)

"""
"""
canvas = tk.Canvas(root, bg="green", width=TRAMP_WIDTH-PAD, height=TRAMP_HEIGHT-PAD)

tkimg = ImageTk.PhotoImage(tramp_back)

# canvas.pack()
X = 500
Y = 20
canvas.place(x=X, y=Y)
canvas.create_image(0, 0, image=tkimg, anchor=tk.NW)




root.configure(bg="green")
root.mainloop()
