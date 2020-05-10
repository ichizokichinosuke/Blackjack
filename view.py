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
        # self.number_font = tk.font.Font(family="Times", size=40)


    def new_card(self, who=None):
        new_c = random.randint(1, 13)
        kind = self.tramp_kind[random.randint(1,4)]
        self.field_canvas = tk.Canvas(root, bg="green", width=TRAMP_WIDTH-PAD, height=TRAMP_HEIGHT-PAD, highlightthickness=0)

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


        self.field_canvas.create_image((TRAMP_WIDTH-PAD)/2, (TRAMP_HEIGHT-PAD)/2, image=tramp_tk)
        self.field_canvas.place(x=x, y=y)

        if new_c > 10:
            new_c = 10

        return new_c

    def choice_action(self):
        print("Stand?: s or Hit?: h")
        print("Please enter s or h.")
        print("Waiting click...")
        self.operation_event.wait()

    def check_num(self, dealer, player):
        bust_x = 125
        ADD = 75
        if dealer > 21:
            print("Player win!")
            self.bust_result = tk.Label(root, text="Bust!", font=("Times", 40), fg="white", bg="black")
            bust_y = self.dealer_y + ADD
            self.bust_result.place(x=bust_x, y=bust_y)

            return False
        elif player > 21:
            print("Player lose!")
            self.bust_result = tk.Label(root, text="Bust!", font=("Times", 40), fg="white", bg="black")
            bust_y = self.player_y + ADD
            self.bust_result.place(x=bust_x, y=bust_y)

            return False

        if dealer == 21 or player == 21:
            self.disp_result(dealer, player)
            return False

        return True

    def disp_result(self, dealer, player):
        self.disp_total(dealer, player)
        # if self.check_num(dealer, player):
        result = "Lose" if dealer >= player else "Win"
        self.result_label = tk.Label(root, text=result+"!!", font=("Times", 40), fg="white", bg="black")
        self.result_label.place(x=500, y=230)

    def disp_total(self, dealer, player):
        dealer_label = tk.Label(root, text=dealer, font=("Times", 40), fg="white", bg="black")
        player_label = tk.Label(root, text=player, font=("Times", 40), fg="white", bg="black")
        x = 150
        self.dealer_y = 5 + TRAMP_HEIGHT/2
        self.player_y = 400 + TRAMP_HEIGHT/2
        dealer_label.place(x=x, y=self.dealer_y)
        player_label.place(x=x, y=self.player_y)
        print(dealer)
        print(player)
        # dealer_label.pack()
        # player_label.pack()

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

                self.disp_total(dealer, player)
                is_continue = self.check_num(dealer, player)

                if not is_continue:
                    break

                self.choice_action()

                if self.choice == "s":
                    while(dealer <= player):
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
    game_thread.result_label.place_forget()
    game_thread.bust_result.place_forget()

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
PAD = 3
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
back_canvas = tk.Canvas(root, bg="green", width=TRAMP_WIDTH-PAD, height=TRAMP_HEIGHT-PAD, highlightthickness=0)
tkimg = ImageTk.PhotoImage(tramp_back)

back_canvas.place(x=BACK_X, y=BACK_Y)
back_canvas.create_image((TRAMP_WIDTH-PAD)/2,(TRAMP_HEIGHT-PAD)/2,  image=tkimg)

root.configure(bg="green")
root.mainloop()
