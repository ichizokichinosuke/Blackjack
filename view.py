import tkinter as tk
from tkinter import ttk
import threading, random
from PIL import Image, ImageTk

event = threading.Event()

class game(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.choice = ""
        self.tramp_kind = {1:"spade", 2: "clover", 3: "diamond", 4: "heart"}

    def new_card(self, who=None):
        new_c = random.randint(1, 13)
        kind = self.tramp_kind[random.randint(1,4)]
        tramp_image = tk.PhotoImage(file=f"../Tramp/{kind}_{new_c}.png")
        # print(kind, new_c)
        # canvas = tk.Canvas(bg="green", width=300, height=400)
        # print(tramp_image)

        # print(who)
        if who == "d":
            print(f"Dealer's new number is {new_c}.")
            x = 300
            y = 20
        elif who == "p":
            print(f"Player's new number is {new_c}.")
            x = 300
            y = 480

        # canvas.place(x=x, y=y)
        # canvas.create_image(x, y, image=tramp_image)

        if new_c > 10:
            new_c = 10

        return new_c

    def choice_action(self):
        print("Stand?: s or Hit?: h")
        print("Please enter s or h.")
        print("Waiting click...")
        event.wait()

    def wait_button(self, ):
        print("*"*20)

    def check_num(self, dealer, player):
        if dealer > 21:
            print("Player win!")
            return False
        elif player > 21:
            print("Player lose!")
            return False

        if dealer == 21:
            print("Player lose!")
            return False
        elif player == 21:
            print("Player win!")
            return False

        return True

    def disp_result(self, dealer, player):
        if self.check_num(dealer, player):
            who_win = "Dealer" if dealer >= player else "Player"

            print(f"Dealer's total number is {dealer}.")
            print(f"Player's total number is {player}.")
            print("*"*20)
            print(f"Winner is {who_win}!!")
            print("*"*20)

    def run(self):
        while(True):
            print("Game Start...")
            dealer = 0
            player = 0
            try_first = True
            while(True):
                if dealer < 17:
                    dealer += self.new_card(who="d")
                player += self.new_card(who="p")
                if try_first:
                    try_first = False
                    continue

                print(f"Dealer's total number is {dealer}.")
                print(f"Player's total number is {player}.")

                is_continue = self.check_num(dealer, player)

                if not is_continue:
                    break

                self.choice_action()

                if self.choice == "s":
                    while(dealer < 17):
                        dealer += self.new_card(who="d")
                        print(f"Dealer's total number is {dealer}.")

                    self.disp_result(dealer, player)
                    break
                elif self.choice == "h":
                    continue

            print("Play again?")
            print("Please enter Yes: y or No: n.")
            game_again = input()
            if game_again == "y" or game_again == "Y":
                self.choice = ""
                continue
            else:
                break

def game_start():
    th.start()

def choose_hit():
    th.choice = "h"
    event.set()
    event.clear()

def choose_stand():
    th.choice = "s"
    event.set()
    event.clear()

def image_resize(width, img):
    resized_image = img.resize((width, int(width*img.size[1]/img.size[0])))
    return resized_image

"""
Const values
"""
TRAMP_WIDTH = 140
PAD = 3
BACK_X = 500
BACK_Y = 20

"""
Main part
"""
th = game()

root = tk.Tk()
root.title("Blackjack")
root.geometry("650x500+500+10")

start_bt = ttk.Button(text="START", width=35, command=game_start)
start_bt.pack(anchor=tk.SW, side=tk.LEFT)

hit_bt = ttk.Button(text="HIT", width=35, command=choose_hit)
hit_bt.pack(anchor=tk.SW, side=tk.LEFT)
stand_bt = ttk.Button(text="STAND", width=35, command=choose_stand)
stand_bt.pack(anchor=tk.SW, side=tk.LEFT)

tramp_back = Image.open("../Tramp/others_2.png")
tramp_back = image_resize(TRAMP_WIDTH, tramp_back)
TRAMP_HEIGHT = tramp_back.size[1]
back_canvas = tk.Canvas(root, bg="green", width=TRAMP_WIDTH-PAD, height=TRAMP_HEIGHT-PAD)
tkimg = ImageTk.PhotoImage(tramp_back)

back_canvas.place(x=BACK_X, y=BACK_Y)
back_canvas.create_image(0, 0, image=tkimg, anchor=tk.NW)


root.configure(bg="green")
root.mainloop()
