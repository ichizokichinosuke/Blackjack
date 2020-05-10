import tkinter as tk
from tkinter import ttk
import threading, random
from PIL import Image, ImageTk


class game(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.choice = ""
        self.tramp_kind = {1:"spade", 2: "clover", 3: "diamond", 4: "heart"}
        self.dealer_imgs = []
        self.player_imgs = []
        self.daemon = True
        self.alive = True
        self.game_start_event = threading.Event()
        self.operation_event = threading.Event()
        self.next_game_event = threading.Event()


    def new_card(self, who=None):
        new_c = random.randint(1, 13)
        kind = self.tramp_kind[random.randint(1,4)]
        self.field_canvas = tk.Canvas(root, bg="green", width=TRAMP_WIDTH-PAD, height=TRAMP_HEIGHT-PAD)

        tramp_image = Image.open(f"../Tramp/{kind}_{new_c}.png")
        tramp_image = image_resize(TRAMP_WIDTH, tramp_image)
        tramp_tk = ImageTk.PhotoImage(tramp_image)



        x = 200
        if who == "d":
            print(f"Dealer's new number is {new_c}.")
            y = 5
            self.dealer_imgs.append(tramp_tk)
            x += len(self.dealer_imgs)*TRAMP_WIDTH/2

        elif who == "p":
            print(f"Player's new number is {new_c}.")
            y = 400
            self.player_imgs.append(tramp_tk)
            x += len(self.player_imgs)*TRAMP_WIDTH/2

        self.field_canvas.place(x=x, y=y)
        self.field_canvas.create_image(0, 0, image=tramp_tk, anchor=tk.NW)

        if new_c > 10:
            new_c = 10

        return new_c

    def choice_action(self):
        print("Stand?: s or Hit?: h")
        print("Please enter s or h.")
        print("Waiting click...")
        self.operation_event.wait()

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
        while True:
            print("Game Start...")
            self.game_start_event.wait()
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
            switchButtonStateToDisabled()

def game_start():
    game_thread.game_start_event.set()
    game_thread.game_start_event.clear()
    start_bt.config(state=tk.DISABLED)

def choose_hit():
    game_thread.choice = "h"
    game_thread.operation_event.set()
    game_thread.operation_event.clear()

def choose_stand():
    game_thread.choice = "s"
    game_thread.operation_event.set()
    game_thread.operation_event.clear()

def next_game():
    game_thread.dealer_imgs = []
    game_thread.player_imgs = []
    game_thread.field_canvas.delete("all")
    game_thread.game_start_event.set()
    game_thread.game_start_event.clear()
    switchButtonStateToAbled()

def switchButtonStateToAbled():
    hit_bt.config(state=tk.NORMAL)
    stand_bt.config(state=tk.NORMAL)
    next_game_bt.config(state=tk.DISABLED)

def switchButtonStateToDisabled():
    hit_bt.config(state=tk.DISABLED)
    stand_bt.config(state=tk.DISABLED)
    next_game_bt.config(state=tk.NORMAL)

def image_resize(width, img):
    resized_image = img.resize((width, int(width*img.size[1]/img.size[0])))
    return resized_image

"""
Const values
"""
TRAMP_WIDTH = 140
PAD = 5
BACK_X = 800
BACK_Y = 5

"""
Main part
"""
root = tk.Tk()
root.title("Blackjack")
root.geometry("1000x700+500+10")

game_thread = game()
game_thread.start()

start_bt = ttk.Button(text="START", width=35, command=game_start)
start_bt.pack(anchor=tk.SW, side=tk.LEFT)

hit_bt = ttk.Button(text="HIT", width=35, command=choose_hit)
hit_bt.pack(anchor=tk.SW, side=tk.LEFT)
stand_bt = ttk.Button(text="STAND", width=35, command=choose_stand)
stand_bt.pack(anchor=tk.SW, side=tk.LEFT)

next_game_bt = ttk.Button(text="Next Game", width=35, command=next_game, state=tk.DISABLED)
next_game_bt.pack(anchor=tk.SW, side=tk.LEFT)

tramp_back = Image.open("../Tramp/others_2.png")
tramp_back = image_resize(TRAMP_WIDTH, tramp_back)
TRAMP_HEIGHT = tramp_back.size[1]
back_canvas = tk.Canvas(root, bg="green", width=TRAMP_WIDTH-PAD, height=TRAMP_HEIGHT-PAD)
tkimg = ImageTk.PhotoImage(tramp_back)

back_canvas.place(x=BACK_X, y=BACK_Y)
back_canvas.create_image(0, 0, image=tkimg, anchor=tk.NW)


root.configure(bg="green")
root.mainloop()
