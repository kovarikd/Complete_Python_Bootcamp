import random

def print_matrix(matrix):
    for element in matrix:
        matrix_output = ""
        for subel in element:
            matrix_output += str(subel)
        print(matrix_output)

def main():
    example = [[11, "|", 12, "|", 13], ["-", "-", "-", "-", "-","-", "-", "-"], [21, "|", 22, "|", 23], ["-", "-", "-", "-", "-", "-", "-", "-"], [31, "|", 32, "|", 33]]
    print_matrix(example)


if __name__ == '__main__':
    main()

