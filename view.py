import tkinter as tk
import game

def game_start():
    game.run()

root = tk.Tk()
root.title("Blackjack")
root.geometry("600x500+500+10")

start_bt = tk.Button(text="START", width=30, command=game_start)
# start_bt.bind("<Button-1>", game_start)
start_bt.pack(anchor=tk.SW, side=tk.LEFT)

hit_bt = tk.Button(text="HIT", width=30, )
hit_bt.pack(anchor=tk.SW, side=tk.LEFT)
stand_bt = tk.Button(text="STAND", width=30, )
stand_bt.pack(anchor=tk.SW, side=tk.LEFT)
root.configure(bg="green")



root.mainloop()
