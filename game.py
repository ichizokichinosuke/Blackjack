import random
import threading
import time

# event = threading.Event()

class game(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.choice = ""

    def new_card(self, who=None):
        new_c = random.randint(1, 13)
        # print(who)
        if who == "d":
            print(f"Dealer's new number is {new_c}.")

        elif who == "p":
            print(f"Player's new number is {new_c}.")

        if new_c > 10:
            new_c = 10

        return new_c

    def choice_action(self):
        print("Stand?: s or Hit?: h")
        print("Please enter s or h.")
        self.choice = ""
        while (not(self.choice == "h" or self.choice == "s")):
            # pass
            # print("Wait")
            time.sleep(10)

        # choice = input()

        # return choice

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
        # assert dealer <= 21 and player <= 21, "We could'nt check number."
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

                # self.choice = self.choice_action()

                # while(not(self.choice == "s" or self.choice == "h")):
                #     self.choice = self.choice_action()
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

def main():
    game_class = game()
    game_class.run()

if __name__ == "__main__":
    main()
