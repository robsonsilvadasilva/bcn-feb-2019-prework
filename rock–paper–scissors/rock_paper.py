# Scissors, paper, rock, lizard and spock.
import random 
hands = ['scissors', 'paper', 'rock', 'lizard', 'spock']

list_hands = [ ('scissors','paper'),
                ('paper','rock'),
                ('rock','lizard'),
                ('lizard','spock'),
                ('spock', 'scissors'),
                ('scissors','lizard'),
                ('lizard', 'paper'),
                ('paper','spock'),
                ('spock','rock'),
                ('rock','scissors') ]


def machine_turn():
    return random.choice(hands)

def player_turn():
    k = int(input((f'Your turn {name}. Choose: 1)Scissors, 2)Paper, 3)Rock, 4)Lizard, 5)Spock: ')))
    while k<1 or k>5:
        k = int(input((f'{name} Please type a number between 1 and 5.\n1)Scissors, 2)Paper, 3)Rock, 4)Lizard, 5)Spock: ')))
    return hands[k-1]


def battle():
    m = machine_turn()
    p = player_turn()
    print(f'\n\n----------\nMachine turn: {m}\n{name} turn: {p}\n---------')
    if m==p:
        return 0
    else:
        for i,j in list_hands:
            if i == m and j == p:
                return 1
        return 2

playerwins = 0
machinewins = 0
def results(playerwins,machinewins):
        print(f'\nPlayer: {playerwins}  /  Machine: {machinewins}')

#Game Starts!        
print('\n'*100)
print('Welcome to the Rock Paper Scissors game!')
name = input('What is your name? ' )

while True:
    try:
        max_games = int(input('How many games do you wanna play? '))
        while max_games%2==0:
            max_games = int(input(f'Please, type a odd number: '))
        break
    except:
        print('Please type a integer and odd number ')

i=1
win = max_games//2 + 1

while i<=max_games:
    print(f'\n\n--> GAME NUMBER: {i}/{max_games} <--')
    B = battle()
    i+=1
    if B == 1:
        machinewins+=1
        if machinewins >= win or (max_games-i+1 < abs(machinewins-playerwins)):
            break
        else:
            results(playerwins,machinewins)
        
    elif B == 2:
        playerwins+=1
        if playerwins >= win or (max_games-i < abs(machinewins-playerwins)):
            break
        else:
            results(playerwins,machinewins)
    elif B == 0:
        print('Tie Game!')
        results(playerwins,machinewins)

if playerwins>machinewins:
    print('\n\nYou Win! :)')
elif playerwins<machinewins:
    print('\n\nMACHINE WINS! :(')
else:
    print('\n\nDraw Game')
