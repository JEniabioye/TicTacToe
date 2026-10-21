import math

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board):
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board):
    return " " not in board

def human_move(board):
    while True:
        try:
            choice = int(input("Your move (1-9): "))
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if choice < 1 or choice > 9:
            print("Please enter a number from 1 to 9.")
            continue

        index = choice - 1
        if board[index] != " ":
            print("That square is already taken.")
            continue

        return index

def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def computer_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def show_menu():
    print("=== TIC-TAC-TOE ===")
    print("1. Play vs Computer")
    print("2. Exit")
    print("===================")

def play_game():
    board = [" "] * 9

    print("You are X. The computer is O.")
    print("Board positions are 1-9:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")

    while True:
        print_board(board)

        move = human_move(board)
        board[move] = "X"

        winner = check_winner(board)
        if winner == "X":
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print("Computer is thinking...")
        move = computer_move(board)
        board[move] = "O"

        winner = check_winner(board)
        if winner == "O":
            print_board(board)
            print("Computer wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()