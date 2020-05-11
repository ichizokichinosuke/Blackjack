import tkinter as tk

root = tk.Tk()
root.title("Blackjack")
root.geometry("600x500+500+10")

start_bt = tk.Button(text="START", width=50)
# start_bt.bind("<Button-1>", DeleteEntryValue)
start_bt.pack(side=tk.BOTTOM)
root.configure(bg="green")

root.mainloop()
