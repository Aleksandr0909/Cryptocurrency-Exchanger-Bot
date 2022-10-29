board = list(range(1, 10))

wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (3, 5, 7), (1, 5, 9)]


def drow_greetings():
    print('----------------------------------------')
    print('ДОБРО ПОЖАЛОВАТЬ '
          'В ИГРУ КРЕСТИКИ НОЛИКИ!')
    print('-------------')


def draw_board():
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(player_token):
    value = input('куда поставить:' + player_token + ' ? ')
    if not (value in '123456789') or not value:
        print('Ошибка ввода,повторите попытку!')

    value = int(value)
    if str(board[value - 1]) in 'XO':
        print('Эта клетка уже занята,повторите попытку!')
    else:
        board[value - 1] = player_token


def check_win():
    for each in wins_coord:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:

        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        winner = check_win()
        if counter > 3 and winner:
            draw_board()
            print(winner, 'Победа!')
            break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья!')
            break


main()
