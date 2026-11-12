def is_win(game):
    win = False
    # rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win


def print_board(game):
    print(game[0][0] + " | " + game[0][1] + " | " + game[0][2])
    print("-" * 9)
    print(game[1][0] + " | " + game[1][1] + " | " + game[1][2])
    print("-" * 9)
    print(game[2][0] + " | " + game[2][1] + " | " + game[2][2])


def main():
    # Initialize the game board
    game = [[' ' for _ in range(3)] for _ in range(3)]
    player1 = 'X'
    player2 = 'O'
    turn = True  # False for player 1's turn, True for player 2's turn. Player 1 first.
    
    print("X = Player 1")
    print("O = Player 2")
    print_board(game)
    
    for n in range(9):
        turn = not turn  # Toggle turn

        if turn == False:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")

        print("Which cell to mark? Enter row and column from 1 to 3 (for example: 1 1): ", end="")
        i, j = map(int, input().split())

        if not (1 <= i <= 3 and 1 <= j <= 3):
            print("Invalid input! Please enter row and column numbers from 1 to 3.")
            n -= 1
            continue

        i -= 1
        j -= 1

        if turn == False:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'

        print_board(game)

        if is_win(game):
            print("Win!")
            break
    
    if n == 8 and not is_win(game):  # All 9 cells were filled without a winner
        print("Tie!")


if __name__ == "__main__":
    main()
