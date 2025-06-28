from cards import card
from art import logo
import random

card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
face_values = ['X', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def deal_cards(cards_list):
    _card = random.randint(1, 13)
    cards_list.append(_card)


def match_scores(cards_list):
    scores_list = []
    for i in range(0, len(cards_list)):
        scores_list.append(card_values[cards_list[i]-1])
    return scores_list


def display_cards(gambler_cards):
    print("You Cards: ")
    for _cards in gambler_cards:
        print(card[_cards])


def sum_of_scores(cards_list):
    total = 0
    for score in cards_list:
        total += score

    return total


def print_two_cards_side_by_side(left_value):
    if left_value == 1:
        left_value = "A"
    elif left_value == 11:
        left_value = "J"
    elif left_value == 12:
        left_value = "Q"
    elif left_value == 13:
        left_value = "K"
    else:
        left_value = str(left_value)

    card_left = [
        "┌─────────┐",
        f"│{left_value: <2}       │",
        "│         │",
        "│    ♦️   │",
        "│         │",
        f"│       {left_value: >2}│",
        "└─────────┘"
    ]

    card_right = [
        "┌─────────┐",
        f"│X        │",
        "│         │",
        "│    ♦️   │",
        "│         │",
        f"│        X│",
        "└─────────┘"
    ]

    for left_line, right_line in zip(card_left, card_right):
        print(f"{left_line}  {right_line}")


def show_dealer_cards(_computer_cards):
    to_show_dealer = []
    for a in range(0, len(_computer_cards)):
        to_show_dealer.append(face_values[_computer_cards[a]])
    print(f"Dealer Cards: {to_show_dealer}")


print(logo)
choice = input("Welcome to Black Jack!! The House is Watching. Are You Ready to Play?(Type 'y' or 'n')\n").lower()
while choice == 'y':
    computer_cards = []
    player_cards = []
    for x in range(2):
        deal_cards(computer_cards)
        deal_cards(player_cards)

    print("Dealers Cards: ")
    print_two_cards_side_by_side(computer_cards[0])
    player_scores = match_scores(player_cards)
    computer_scores = match_scores(computer_cards)
    player_sum = sum_of_scores(player_scores)
    computer_sum = sum_of_scores(computer_scores)
    game = True
    while game:
        display_cards(player_cards)
        print(f"Your Current Score: {player_sum}")
        print(f"Dealer's Score of First Card: {card_values[computer_cards[0]-1]}")
        if player_sum == 21:
            print("Black Jack!!")
            if len(player_cards) > 2:
                while computer_sum < 17:
                    deal_cards(computer_cards)
                    computer_scores = match_scores(computer_cards)
                    computer_sum = sum_of_scores(computer_scores)
            if player_sum > computer_sum:
                print(f"The Dealer Scored {computer_sum}")
                show_dealer_cards(computer_cards)
                print("You win!")
                game = False
            if player_sum == computer_sum:
                print(f"The Dealer Scored {computer_sum}")
                show_dealer_cards(computer_cards)
                print("Match Drawn!")
                game = False
            if computer_sum > 21:
                print(f"The Dealer Scored {computer_sum}")
                show_dealer_cards(computer_cards)
                print("Dealer Bust, You Win!")
                game = False

        elif player_sum > 21:
            if 11 in player_scores:
                index = player_scores.index(11)
                player_scores[index] = 1
                player_sum -= 10
            else:
                print("Bust, You Lost!")
                print(f"The Dealer Scored {computer_sum}")
                show_dealer_cards(computer_cards)
                game = False

        else:
            want_card = input("Do You Want Another Card(type 'y' or 'n'): ").lower()
            if want_card == 'y':
                deal_cards(player_cards)
                player_scores = match_scores(player_cards)
                player_sum = sum_of_scores(player_scores)
            elif want_card == 'n':
                while computer_sum < 17:
                    deal_cards(computer_cards)
                    computer_scores = match_scores(computer_cards)
                    computer_sum = sum_of_scores(computer_scores)
                if player_sum > 21:
                    if 11 in player_scores:
                        index = player_scores.index(11)
                        player_scores[index] = 1
                        player_sum -= 10
                    else:
                        print("Bust, You Lost!")
                        print(f"The Dealer Scored {computer_sum}")
                        show_dealer_cards(computer_cards)
                        game = False
                elif computer_sum > 21:
                    print(f"The Dealer Scored {computer_sum}")
                    print("Dealer Bust, You Win!")
                    show_dealer_cards(computer_cards)
                    game = False
                elif player_sum > computer_sum:
                    print(f"The Dealer Scored {computer_sum}")
                    show_dealer_cards(computer_cards)
                    print("You win!")
                    game = False
                elif player_sum == computer_sum:
                    print(f"The Dealer Scored {computer_sum}")
                    show_dealer_cards(computer_cards)
                    print("Match Drawn!")
                    game = False

                elif computer_sum > player_sum:
                    print(f"The Dealer Scored {computer_sum}")
                    show_dealer_cards(computer_cards)
                    print("You Lost!")
                    game = False
            elif choice != 'y' and choice != 'n':
                print("Invalid Input, Game Closed")

    choice = input("Do you want to play another Game?(Type 'y' or 'n')\n").lower()
    if choice == 'y':
        print("\n" * 100)
    elif choice != 'y' and choice != 'n':
        print("Invalid Input, Game Closed")
