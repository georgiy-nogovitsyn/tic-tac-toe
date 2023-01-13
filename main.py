import random


def main():
    while True:
        try:
            game_mode = int(
                input('Choose a game mode: 1 - Player vs Player, 2 - Player vs Machine, 3 - Machine vs Machine: '))
            if game_mode not in range(1, 4):
                print('Only 1, 2, 3 integers')
            else:
                break
        except ValueError:
            print('Only 1, 2, 3 integers')

    game_field = ['n' for _ in range(0, 9)]

    def game_field_draw():  # draw a 3x3 game field
        for counter, char in enumerate(game_field):
            if (counter + 1) % 3 != 0:
                print(char, end=' ')
            else:
                print(char)

    def player_choice(symbol):  # checks valid of user choice and draws it on field
        while True:
            try:
                choice = int(input('Choose cell from 1 to 9: ')) - 1
                if game_field[choice] == 'n':
                    game_field[choice] = symbol
                    break
                else:
                    print('That cell is already taken, choose another.')
                    continue
            except ValueError:
                print('Value Error, only integers in are allowed.')
            except IndexError:
                print('Cell number error. Only integers from 1 to 9')

    def machine_choice(symbol):
        print(f'"{symbol}" Computer is thinking...')
        choice = random.randrange(0, 9)
        while game_field[choice] != 'n':
            choice = random.randrange(0, 9)
        game_field[choice] = symbol

    def winner(symbol):  # checks win and update status of the game
        win_combination = list(symbol * 3)
        status = False
        if game_field[0:3] == win_combination \
                or game_field[3:6] == win_combination \
                or game_field[6:9] == win_combination \
                or game_field[0:7:3] == win_combination \
                or game_field[1:8:3] == win_combination \
                or game_field[2:9:3] == win_combination \
                or game_field[2:7:2] == win_combination \
                or game_field[0:9:4] == win_combination:
            status = True
        return status

    def game(game_mode):  # starts game
        game_field_draw()
        if game_mode == 1:
            while True:
                player_choice('x')
                game_field_draw()
                if winner('x') is True:
                    print('X player won')
                    break
                if 'n' not in game_field:
                    print('It\'s draw!')
                    break
                player_choice('o')
                game_field_draw()
                if winner('o') is True:
                    print('O player won')
                    break
        elif game_mode == 2:
            while True:
                player_choice('x')
                game_field_draw()
                if winner('x') is True:
                    print('X player won')
                    break
                if 'n' not in game_field:
                    print('It\'s draw!')
                    break
                machine_choice('o')
                game_field_draw()
                if winner('o') is True:
                    print('Computer won!')
                    break
        elif game_mode == 3:
            while True:
                machine_choice('x')
                game_field_draw()
                if winner('x') is True:
                    print('"x" Computer won!')
                    break
                if 'n' not in game_field:
                    print('It\'s draw!')
                    break
                machine_choice('o')
                game_field_draw()
                if winner('o') is True:
                    print('"o" Computer won!')
                    break

    game(game_mode)

    if input('Do you want play again? \n y/n \t') == 'y':
        main()


main()
