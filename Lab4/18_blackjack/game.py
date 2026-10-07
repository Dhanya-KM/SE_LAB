from cards import Deck, hand_value


class Blackjack:
    def __init__(self):
        self.chips = 100

    def show(self, player, dealer, hide=True):
        if hide:
            shown_dealer = ["??"]
        else:
            shown_dealer = [f"{r}{s}" for r, s in dealer]

        print("Dealer:", " ".join(shown_dealer))
        print("Player:", " ".join(f"{r}{s}" for r, s in player),
              "=", hand_value(player))

    def get_wager(self):
        while True:
            print("Chips:", self.chips)

            try:
                wager = int(input("Enter wager: ").strip())
            except ValueError:
                print("Invalid wager. Enter a whole number.")
                continue

            if wager <= 0:
                print("Invalid wager. Wager must be greater than 0.")
                continue

            if wager > self.chips:
                print("Invalid wager. You do not have enough chips.")
                continue

            return wager

    def round(self):
        wager = self.get_wager()

        deck = Deck()

        player = []
        dealer = []

        # Initial deal with empty-deck protection
        for _ in range(2):
            card = deck.draw()

            if card is None:
                print("Deck is empty.")
                return True

            player.append(card)

        for _ in range(2):
            card = deck.draw()

            if card is None:
                print("Deck is empty.")
                return True

            dealer.append(card)

        self.show(player, dealer)

        player_value = hand_value(player)
        dealer_value = hand_value(dealer)

        # Natural blackjack
        player_blackjack = player_value == 21 and len(player) == 2
        dealer_blackjack = dealer_value == 21 and len(dealer) == 2

        if player_blackjack or dealer_blackjack:
            self.show(player, dealer, hide=False)

            if player_blackjack and dealer_blackjack:
                print("Both have blackjack. Push.")

            elif player_blackjack:
                self.chips += wager
                print("Blackjack! Player wins.")
                print("Chips:", self.chips)

            else:
                self.chips -= wager
                print("Dealer has blackjack. Dealer wins.")
                print("Chips:", self.chips)

            return True

        # Player's turn
        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()

            if key == "q":
                print("Game quit.")
                return False

            if key == "s":
                break

            if key == "h":
                card = deck.draw()

                if card is None:
                    print("Deck is empty.")
                    return True

                player.append(card)
                print("You drew:", f"{card[0]}{card[1]}")
                self.show(player, dealer)

                if hand_value(player) > 21:
                    print("Bust. Dealer wins.")
                    self.chips -= wager
                    print("Chips:", self.chips)
                    return True

                continue

            print("Invalid command. Enter h, s, or q.")

        # Dealer's turn
        while hand_value(dealer) < 17:
            card = deck.draw()

            if card is None:
                print("Deck is empty.")
                return True

            dealer.append(card)
            print("Dealer drew:", f"{card[0]}{card[1]}")

        self.show(player, dealer, hide=False)

        player_value = hand_value(player)
        dealer_value = hand_value(dealer)

        # Round resolution
        if dealer_value > 21:
            self.chips += wager
            print("Dealer busts. Player wins.")

        elif player_value > dealer_value:
            self.chips += wager
            print("Player wins.")

        elif player_value < dealer_value:
            self.chips -= wager
            print("Dealer wins.")

        else:
            print("Push.")

        print("Chips:", self.chips)

        return True

    def run(self):
        print("Blackjack — starting chips:", self.chips)

        while self.chips > 0:
            if not self.round():
                return

            if self.chips <= 0:
                print("No chips remaining.")
                return

            if input("Play again? [y/n]: ").strip().lower() != "y":
                return