import random

class Card:
    def __init__(self, rank, suit, value = 0):
        self.rank = rank
        self.suit = suit
        self.value = value

    def ace_value(self):
        return self.value == 11

    def get_value(self):
        return self.value
    
    def reveal(self):
        return(f"{self.suit} {self.rank}")

class Card_Deck:

    def __init__(self):
        self.cards = []

    def build_deck(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
        
    def prep_blackjack(self):
        for card in self.cards:
            if card.rank == "A":
                card.value = 11
            elif card.rank in ["J", "Q", "K"]:
                card.value = 10
            else:
                card.value = int(card.rank)

    def shuffle_deck(self):
        for old in range(len(self.cards) -1, 0, -1):
            new = random.randint(0, old)
            self.cards[old], self.cards[new] = self.cards[new], self.cards[old]

    def draw_card(self):
        return self.cards.pop()

        
class Player:

    def __init__(self, name = "Player", hand = []):
        self.name = name
        self.hand = hand
    
    def ace_value(self, score):
        for card in self.hand:
            if score > 21 and card.value == 11:
                card.value = 1
        
    

def play_blackjack():
    player = Player(name = input("What's your name, stranger?\n"))
    player.chips = 1500
    playing = True
    while playing:
        new_round = input("Play next hand? ['yes' or 'no']")
        if new_round == 'no':
            break
        if new_round != 'yes':
            print(f"Wha'd you say, {player.name}?")
        else:
            current_round = True
            while current_round:
                house_hand = []
                player.hand = []
                deck = Card_Deck()
                deck.build_deck()
                deck.prep_blackjack()
                house_score = 0
                player_score = 0
                deck.shuffle_deck()
                next_card = deck.draw_card()
                player.hand.append(next_card)
                player_score += next_card.value
                next_card = deck.draw_card()
                house_hand.append(next_card)
                house_score += next_card.value
                next_card = deck.draw_card()
                player.hand.append(next_card)
                player_score += next_card.value
                next_card = deck.draw_card()
                house_hand.append(next_card)
                house_score += next_card.value
                dealer_turn = False
                player_turn = True
                while player_turn:
                    print("----Dealer's Hand----")
                    print("<hidden>\t")
                    for card in house_hand:
                        print(card.reveal())

                    print(f"----{player.name}'s Hand----")
                    for card in player.hand:
                        print(card.reveal())
                    print(f"Total: {str(player_score)}")
                    if player_score == 21:
                        print("Blackjack! You win!")
                        player_turn = False
                        current_round = False
                        break


                    action = input(f"Hit or stand, {player.name}?\n\t(type 'hit' or 'stand')")
                    if action.lower() == 'stand':
                        player_turn = False
                        dealer_turn = True
                    elif action.lower() == 'hit':
                        next_card = deck.draw_card()
                        player.hand.append(next_card)
                        player_score += next_card.value
                        for card in player.hand:
                            if card.value == 11 and player_score > 21:
                                card.value = 1
                                player_score -= 10
                        if player_score > 21:
                            for card in player.hand:
                                print(card.reveal())
                            print(f"BUSTED at {player_score}!")
                            player_turn = False
                            current_round = False
                    else:
                        print("Wha'd you say, pardner?")

                while dealer_turn:
                    print("----Dealer's Hand----")
                    for card in house_hand:
                        card.reveal()
                    print(f"Total: {str(house_score)}")
                    print(f"----{player.name}'s Hand----")
                    for card in player.hand:
                        card.reveal()
                    print(f"Total: {str(player_score)}")

                    while house_score < 17:
                        next_card = deck.draw_card()
                        house_hand.append(next_card)
                        house_score += next_card.value
                        for card in house_hand:
                            if card.value == 11 and house_score > 21:
                                card.value = 1
                                house_score -= 10
                        input(f"Dealer draws the {next_card.reveal()}!\nDealer Total = {house_score}.")
                    dealer_turn = False
                    if house_score > 21:
                        print(f"The dealer busted! {player.name.title()} wins!")
                        dealer_turn = False
                        
                    elif house_score >= player_score:
                        print(f"Too bad, {player.name.title()}! The house wins.")
                        dealer_turn = False
                        
                    else:
                        print(f"You win this round, {player.name.title()}!")
                        dealer_turn = False
                        
                    deal_again = input("Play again? ('yes' or 'no')")
                    if deal_again == 'no':
                        break


play_blackjack()




        
    


  