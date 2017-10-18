def print_matrix(matrix):
    for element in matrix:
        matrix_output = ""
        for subel in element:
            matrix_output += str(subel)
        print(matrix_output)


def verify_input(inpt, player, matrix):
    inpt = inpt.upper()
    if inpt == "END":
        print("Game was terminated!")
        exit(12)
    elif inpt == "11" and matrix[0][0] == " ":
        if player == "Player_1":
            matrix[0][0] = "O"
        else:
            matrix[0][0] = "X"
        return matrix
    elif inpt == "12" and matrix[0][2] == " ":
        if player == "Player_1":
            matrix[0][2] = "O"
        else:
            matrix[0][2] = "X"
        return matrix
    elif inpt == "13" and matrix[0][4] == " ":
        if player == "Player_1":
            matrix[0][4] = "O"
        else:
            matrix[0][4] = "X"
        return matrix
    elif inpt == "21" and matrix[2][0] == " ":
        if player == "Player_1":
            matrix[2][0] = "O"
        else:
            matrix[2][0] = "X"
        return matrix
    elif inpt == "22" and matrix[2][2] == " ":
        if player == "Player_1":
            matrix[2][2] = "O"
        else:
            matrix[2][2] = "X"
        return matrix
    elif inpt == "23" and matrix[2][4] == " ":
        if player == "Player_1":
            matrix[2][4] = "O"
        else:
            matrix[2][4] = "X"
        return matrix
    elif inpt == "31" and matrix[4][0] == " ":
        if player == "Player_1":
            matrix[4][0] = "O"
        else:
            matrix[4][0] = "X"
        return matrix
    elif inpt == "32" and matrix[4][2] == " ":
        if player == "Player_1":
            matrix[4][2] = "O"
        else:
            matrix[4][2] = "X"
        return matrix
    elif inpt == "33" and matrix[4][4] == " ":
        if player == "Player_1":
            matrix[4][4] = "O"
        else:
            matrix[4][4] = "X"
        return matrix
    else:
        print("\n")
        print("OUTPUT:: {}:Invalid input, you wasted your turn.".format(player))
        print("\n")
        return matrix


def main():
    help_matrix = [[11, "|", 12, "|", 13], ["---", "---", "--"], [21, "|", 22, "|", 23], ["---", "---", "--"], [31, "|", 32, "|", 33]]
    ttt_matrix = [[" ", "|", " ", "|", " "], ["---", "---", "--"], [" ", "|", " ", "|", " "], ["---", "---", "--"], [" ", "|", " ", "|", " "]]
    current_player = "Player_1"
    while True:
        print("Here are the coordinations in the Tic Tac Toe matrix")
        print_matrix(help_matrix)
        print("\n")
        print("Player 1 has O")
        print("Player 2 has X")
        print("\n")
        print("Tic Tac Toe game matrix")
        print_matrix(ttt_matrix)
        if current_player == "Player_1":
            pick = input("Player 1: Please pick your your field")
            ttt_matrix = verify_input(pick, current_player, ttt_matrix)
            current_player = "Player_2"
        else:
            pick = input("Player 1: Please pick your your field")
            ttt_matrix = verify_input(pick, current_player, ttt_matrix)
            current_player = "Player_1"


if __name__ == '__main__':
    main()
