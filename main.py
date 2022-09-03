import random
from artwork import logo
from user_input import user_option_handler

shoe = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card() -> int:
    """
    Deals a random card.
    """
    return random.choice(shoe)


def deal_opening_hand() -> list[int]:
    """
    Deals the opening hand for a player.
    """
    return [deal_card() for _ in range(2)]


def calculate_score(hand: list[int]) -> tuple[int, bool]:
    """
    Calculates the sum total of the hand
    """
    sum = 0
    busted = False

    for card in hand:
        sum += card

    if sum > 21:
        if 11 not in hand:
            busted = True
        else:
            hand[hand.index(11)] = 1
            [sum, busted] = calculate_score(hand)

    return [sum, busted]


def display_hands(player: list[int], dealer: list[int | str]) -> None:
    print("-" * 30)
    print(f"Your Cards:     {player}")
    print(f"Dealer's Cards: {dealer}")

    return None


def main():
    game_running = True

    while game_running:
        player_hand = deal_opening_hand()
        [player_score, player_busted] = calculate_score(player_hand)
        dealer_hand = deal_opening_hand()
        [dealer_score, dealer_busted] = calculate_score(dealer_hand)

        player_turn = True
        while player_turn:
            display_hands(player_hand, [dealer_hand[0], ""])

            hit_or_stand = user_option_handler("(h)it or (s)tand? ", ["h", "s"])
            if hit_or_stand == "h":
                player_hand.append(deal_card())
                [player_score, player_busted] = calculate_score(player_hand)

                if player_busted:
                    player_turn = False

            else:
                player_turn = False

        if player_busted:
            display_hands(player_hand, dealer_hand)
            print("You Busted! Game Over!")

        else:
            dealer_turn = True
            while dealer_turn:
                if dealer_score < 17:
                    dealer_hand.append(deal_card())
                    [dealer_score, dealer_busted] = calculate_score(dealer_hand)
                    if dealer_busted:
                        dealer_turn = False

                else:
                    dealer_turn = False

            display_hands(player_hand, dealer_hand)
            if dealer_busted:
                print("Dealer Busts! You win! Game Over!")
            elif player_score > dealer_score:
                print("You win! Game Over!")
            elif player_score == dealer_score:
                print("Push! Game Over!")
            else:
                print("You lose! Game Over!")

        play_again = user_option_handler("Play again? (y|n) ", ["y", "n"])
        if play_again == "n":
            game_running = False


if __name__ == "__main__":
    print(logo)
    main()
