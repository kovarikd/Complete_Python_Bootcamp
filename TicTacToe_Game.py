ttt_matrix = [[" ", "|", " ", "|", " "], ["---", "---", "--"], [" ", "|", " ", "|", " "], ["---", "---", "--"], [" ", "|", " ", "|", " "]]


def print_matrix(matrix):
    for element in matrix:
        matrix_output = ""
        for subel in element:
            matrix_output += str(subel)
        print(matrix_output)


def verify_input(inpt, player):
    inpt = inpt.upper()
    global ttt_matrix
    if inpt == "END":
        print("Game was terminated!")
        exit(12)
    elif inpt == "11" and ttt_matrix[0][0] == " " and player == "Player_1":
        ttt_matrix[0][0] = "O"
    elif inpt == "11" and ttt_matrix[0][0] == " " and player == "Player_2":
        ttt_matrix[0][0] = "X"
    elif inpt == "12" and ttt_matrix[0][2] == " " and player == "Player_1":
        ttt_matrix[0][2] = "O"
    elif inpt == "12" and ttt_matrix[0][2] == " " and player == "Player_2":
        ttt_matrix[0][2] = "X"
    elif inpt == "13" and ttt_matrix[0][4] == " " and player == "Player_1":
        ttt_matrix[0][4] = "O"
    elif inpt == "13" and ttt_matrix[0][4] == " " and player == "Player_2":
        ttt_matrix[0][4] = "X"
    elif inpt == "21" and ttt_matrix[2][0] == " " and player == "Player_1":
        ttt_matrix[2][0] = "O"
    elif inpt == "21" and ttt_matrix[2][0] == " " and player == "Player_2":
        ttt_matrix[2][0] = "X"
    elif inpt == "22" and ttt_matrix[2][2] == " " and player == "Player_1":
        ttt_matrix[2][2] = "O"
    elif inpt == "22" and ttt_matrix[2][2] == " " and player == "Player_2":
        ttt_matrix[2][2] = "X"
    elif inpt == "23" and ttt_matrix[2][4] == " " and player == "Player_1":
        ttt_matrix[2][4] = "O"
    elif inpt == "23" and ttt_matrix[2][4] == " " and player == "Player_2":
        ttt_matrix[2][4] = "X"
    elif inpt == "31" and ttt_matrix[4][0] == " " and player == "Player_1":
        ttt_matrix[4][0] = "O"
    elif inpt == "31" and ttt_matrix[4][0] == " " and player == "Player_2":
        ttt_matrix[4][0] = "X"
    elif inpt == "31" and ttt_matrix[4][0] == " " and player == "Player_1":
        ttt_matrix[4][2] = "O"
    elif inpt == "31" and ttt_matrix[4][0] == " " and player == "Player_2":
        ttt_matrix[4][2] = "X"
    elif inpt == "33" and ttt_matrix[4][4] == " " and player == "Player_1":
        ttt_matrix[4][4] = "O"
    elif inpt == "33" and ttt_matrix[4][4] == " " and player == "Player_2":
        ttt_matrix[4][4] = "X"
    else:
        print("\n")
        print("OUTPUT:: {}:Invalid input, you wasted your turn.".format(player))
        print("\n")
        return ttt_matrix


def game_resoution():
    if ttt_matrix[0][0] and ttt_matrix[0][2] and ttt_matrix[0][4]:


def main():
    help_matrix = [[11, "|", 12, "|", 13], ["---", "---", "--"], [21, "|", 22, "|", 23], ["---", "---", "--"], [31, "|", 32, "|", 33]]
    global ttt_matrix
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
            verify_input(pick, current_player)
            current_player = "Player_2"
        else:
            pick = input("Player 1: Please pick your your field")
            verify_input(pick, current_player)
            current_player = "Player_1"


if __name__ == '__main__':
    main()
