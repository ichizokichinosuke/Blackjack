import tkinter as tk
from tkinter import ttk
import threading
import game

def game_start():

    th = threading.Thread(target=game_class.run())
    th.start()
    # game.run()
    # start_bt.state(["disabled"])

def choose_hit():
    game.choice_action("h")
    # print("\n")

def choose_stand():
    game.choice_action("s")
    # print("\n")


game_class = game.game()

root = tk.Tk()
root.title("Blackjack")
root.geometry("650x500+500+10")

start_bt = ttk.Button(text="START", width=35, command=game_start)
# start_bt.bind("<Button-1>", game_start)
start_bt.pack(anchor=tk.SW, side=tk.LEFT)

hit_bt = ttk.Button(text="HIT", width=35, command=choose_hit)
hit_bt.pack(anchor=tk.SW, side=tk.LEFT)
stand_bt = ttk.Button(text="STAND", width=35, command=choose_stand)
stand_bt.pack(anchor=tk.SW, side=tk.LEFT)


root.configure(bg="green")
root.mainloop()
