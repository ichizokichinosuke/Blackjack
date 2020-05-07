import random

def new_card(who=None):
    new_c = random.randint(1, 13)
    # print(who)
    if who == "d":
        print(f"Dealer's new number is {new_c}.")

    elif who == "p":
        print(f"Player's new number is {new_c}.")

    if new_c > 10:
        new_c = 10

    return new_c

def choice_action():
    print("Stand?: s or Hit?: h")
    print("Please enter s or h.")

    choice = input()

    return choice

def check_num(dealer, player):
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

def disp_result(dealer, player):
    assert dealer <= 21 and player <= 21, "We could'nt check number."
    who_win = "Dealer" if dealer >= player else "Player"

    print(f"Winner is {who_win}!!")

def run():
    while(True):
        print("Game Start...")
        dealer = 0
        player = 0
        try_first = True
        while(True):
            if dealer < 17:
                dealer += new_card(who="d")
            player += new_card(who="p")
            if try_first:
                try_first = False
                continue

            print(f"Dealer's total number is {dealer}.")
            print(f"Player's total number is {player}.")

            is_continue = check_num(dealer, player)

            if not is_continue:
                break

            choice = choice_action()

            while(not(choice == "s" or choice == "h")):
                choice = choice_action()

            if choice == "s":
                while(dealer < 17):
                    dealer += new_card(who="d")
                    print(f"Dealer's total number is {dealer}.")

                disp_result(dealer, player)
                break
            elif choice == "h":
                continue

        print("Play again?")
        print("Please enter Yes: y or No: n.")
        game_again = input()
        if game_again == "y" or game_again == "Y":
            continue
        else:
            break

def main():
    run()

if __name__ == "__main__":
    main()
