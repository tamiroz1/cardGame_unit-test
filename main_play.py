from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player
from CardGame import CardGame

def main():
    # Input player names
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")
    num_of_cards = int(input("Enter number of cards to deal: "))

    # Initialize the game with the given players
    game = CardGame(player1_name, player2_name, num_of_cards)

    # Deal cards to the players and print their initial hands
    print("\n the game starting now!!")
    print("please welcome our players for today : ")
    print(game.player1)
    print(game.player2)

    # Play 10 rounds of the game
    for round in range(1, 11):
        print(f"\nRound {round}:")
        # Each player throws a random card
        player1_card: Card = game.player1.get_card()
        player2_card: Card = game.player2.get_card()
        print(f"{game.player1.name} threw {player1_card}")
        print(f"{game.player2.name} threw {player2_card}")

        # Check for tie using __eq__ function ( an Unexpected case)
        if player1_card == player2_card:
            print("It's a tie!")
            continue  # Skip the rest of the loop and move to the next round

        # Determine the winner of the round
        if player1_card > player2_card:
            game.player1.add_card(player1_card)
            game.player1.add_card(player2_card)
            print(f"{game.player1.name} wins this round!")
        else:
            game.player2.add_card(player1_card)
            game.player2.add_card(player2_card)
            print(f"{game.player2.name} wins this round!")

    # Determine the winner of the game
    winner = game.get_winner()
    if winner:
        print("\nthats was an amazing game please welcome our winner:")
        print(f"{winner}")

if __name__ == "__main__":
    main()
