#NAMES

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

class Player():
    def __init__(self, name, cpu):
        self.player = name
        self.cpu = True 
        self.score = 0

    def play_round(self):
        if self.cpu:
            return random.choice(choices)
        else:
            redo = True
            while(redo):
                user_choice = input("Pick r, p, or s")
                if user_choice in ['r', 'p', 's']:
                    redo = False 
                else:
                    print("must pick one of the above options")
            if user_choice == 'r':
                return choices[0]
            elif user_choice == 'p':
                return choices[1]
            else:
                return choices[2]
            

def play_game(num_players):
    players = []
    for i in range(num_players):
        name = input(f"Name of player {i+1}")
        players.append(Player(name, False))

    while len(players) < 2:
        players.append(Player('computer', True))

    while True:
        p1 = players[0].play_round()
        p2 = players[1].play_round()

        if p1 == p2:
            continue 
        elif p1 == 'rock':
            if p2 == 'scissors':
                p1.score += 1
            else:
                p2.score += 1
        elif p1 == 'paper':
            if p2 == 'rock':
                p2.score += 1
            else:
                p1.score += 1
        else:
            if p2 == 'rock':
                p2.score += 1
            else:
                p1.score += 1

        print('current score:')
        print('p1:', p1.score)
        print('p2:', p2.score)

def main():
    num = input('how many players?')
    play_game(num)