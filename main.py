def main():
    game_field = ['n' for _ in range(0, 9)]


    def game_field_draw(): # draw a 3x3 game field
        c = 1
        for ch in game_field:
            if c % 3 != 0:
                print(ch, end=' ')
            else:
                print(ch)
            c += 1

    def player_choice(player):  # checks valid of user choice and draws it on field
        symbol = player
        choice = input('Choose cell from 1 to 9: ')
        if choice not in [str(num) for num in range(1, 10)]:
            print('Incorrect value')
            player_choice(symbol)
        else:
            choice = int(choice)
            choice = choice - 1
            if game_field[choice] == 'n':
                if symbol == 'x':
                    game_field[choice] = 'x'
                else:
                    game_field[choice] = 'o'
            else:
                print('That cell is already taken, choose another.')
                player_choice(symbol)

    def win_checker(): # checks win and update status of the game
        x_plr = ['x', 'x', 'x']
        o_plr = ['o', 'o', 'o']
        status = True
        if game_field[0:3] == x_plr \
                or game_field[3:6] == x_plr \
                or game_field[6:9] == x_plr \
                or game_field[0:7:3] == x_plr \
                or game_field[1:8:3] == x_plr \
                or game_field[2:9:3] == x_plr \
                or game_field[2:7:2] == x_plr \
                or game_field[0:9:4] == x_plr:
            status = False
        elif game_field[0:3] == o_plr \
                or game_field[3:6] == o_plr \
                or game_field[6:9] == o_plr \
                or game_field[0:7:3] == o_plr \
                or game_field[1:8:3] == o_plr \
                or game_field[2:9:3] == o_plr \
                or game_field[2:7:2] == o_plr \
                or game_field[0:9:4] == o_plr:
            status = False
        return status

    def game(): # starts game
        game_field_draw()
        moves_to_draw = 9 # variable for draw checker
        while True:
            player_choice('x')
            moves_to_draw -= 1
            game_field_draw()
            if win_checker() is False:
                print('X player won')
                break
            if moves_to_draw == 0: # draw checker
                print('Draw!')
                break
            player_choice('o')
            moves_to_draw -= 1
            game_field_draw()
            if win_checker() is False:
                print('O player won')
                break
        if input('Do you want play again? \n y/n \t') == 'y':
            main()

    game()


main()
