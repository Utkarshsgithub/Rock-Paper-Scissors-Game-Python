# ----------------------------< R O C K - P A P E R - S C I S S O R >----------------------------

import random

import time

# -----------  G l o b a l   V a r i a b l e s  ----------------

player_choice = None

computer_choice = None

winner = None

total_plays = 0

computer_points = 0

player_points = 0

ties = 0

# --------------------------------------------------------------


game_data = open('rps data.txt', 'a')  # local database that will save your all data

play_time = time.asctime(time.localtime(time.time()))

print('>----------------------< ROCK - PAPER - SCISSORS [GAME] >----------------------<')

# r = Rock, p = Paper, s = Scissor
choices = ['r', 'p', 's']

rps = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor'}


def check_win():

    player()

    # checking for int input by user
    if type(player_choice) == 'int':

        print('\nYou entered a no.')

    else:

        computer()

        # to change value of global variables
        global winner

        global computer_points


        global player_points

        global ties

        if computer_choice == 'r' and player_choice == 's' or computer_choice == 'p' and player_choice == 'r'\
                or computer_choice == 's' and player_choice == 'p':

            winner = 'Computer'

            computer_points += 1

            return winner

        elif player_choice == 'r' and computer_choice == 's' or player_choice == 'p' and computer_choice == 'r'\
                or player_choice == 's' and computer_choice == 'p':

            winner = 'You'

            player_points += 1

            return winner

        elif player_choice == computer_choice:

            winner = 'Tie'

            ties += 1

            return winner


def computer():

    # to change value of global var 'computer_choice'
    global computer_choice

    computer_choice = random.choice(choices)

    return computer_choice


def player():

    # to change value of global var 'player_choice'
    global player_choice

    print('''Rock:    R 
Paper:   P
Scissor: S
Quit:    Q''')

    print('------------------------------------------------')

    player_choice = input('\nYour choice: ').lower()

    valid = ['r', 'p', 's']

    while player_choice not in valid:
        player_choice = input('\nYour choice: ').lower()

    return player_choice


def game_over():

    print('~~~~~~~~~~ F I N A L   R E S U L T S  ~~~~~~~~~~')

    print(f'\nTotal -\t{total_plays} plays\nComputer won -\t{computer_points} plays\n'
          f'You won -\t{player_points} plays\nTie -\t{ties}')

    if computer_points > player_points:

        print('\nCOMPUTER IS THE WINNER!!')

    elif player_points > computer_points:

        print('\nCOMPUTER IS THE WINNER!!')

    else:

        print('\nIT"S A TIE!!')

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    return


def play_game():

    global total_plays

    no_of_turns = int(input('\nHow many turns do you wanna play: '))

    total_plays = no_of_turns

    game_data.write(f'\nPlayed on -\t{play_time}\n')

    while no_of_turns != 0:

        print('------------------------------------------------')

        check_win()

        game_data.write(f'\n{rps[player_choice]}\t\t{rps[computer_choice]} \t->\t {winner}')

        no_of_turns = no_of_turns - 1

        if player_choice == 'r' or 'p' or 's':

            print(f"Conputer choice: {rps[computer_choice]}")

            print('\n------------------------------------------------')

            print(f'{rps[computer_choice]} V/S {rps[player_choice]}')

            print('Result - ', end='')

            if winner == 'Tie':

                print('< Tie >')

            elif winner != None:

                print(f'< {winner} won >')

        elif player_choice == 'q':

            exit()

    game_over()


if __name__ == '__main__':

    try:

        game_data.write('\n\n----------------------------------------------------------')

        play_game()

        game_data.write(f'Winner -> {winner}')

        game_data.write('\n----------------------------------------------------------')

    except Exception as e:

        print('\n', e)

        print('\nINVALID INPUT (please check your input)')


