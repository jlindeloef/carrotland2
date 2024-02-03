from random import randint


class Board:
    def __init__(self, board):
        self.board = board

    def letters_to_numbers(self):
        """
        Transform letters to numbers to our boardgame column.
        """
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        """
        Printing letters to the board.
        Adding numbers as rows in our boardgame.
        Creating and defying the inputs on the board.
        Make our board start with number 1.
        """
        print("")
        print("  A B C D E")
        row_num = 1
        for row in self.board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1


class Carrots:
    def __init__(self, board):
        self.board = board

    def create_carrots(self):
        """
        Random displacement of carrots on game board.
        Give the carrot the mark of "X".
        """
        for _ in range(5):
            carrot_row, carrot_column = randint(0, 4), randint(0, 4)
            while self.board[carrot_row][carrot_column] == "X":
                carrot_row, carrot_column = randint(0, 4), randint(0, 4)
            self.board[carrot_row][carrot_column] = "X"

    def get_user_input(self):
        """
        Get users inputs in the game and responding to the inputs.
        """
        try:
            row = input("Look for carrot on row(1-5)...: \n")
            while row not in '12345':
                print("Not valid! Select a valid row(1-5).")
                row = input("Try again, look for carrot on row(1-5)...: \n")

            column = input("Choose a column(A-E): \n").upper()
            while column not in "ABCDE":
                print("Not valid! Select a valid column(A-E).")
                column = input("Choose a column(A-E): \n").upper()
            return int(row) - 1, \
                Board.letters_to_numbers(self)[column]
        except (ValueError, KeyError):
            print("Not a valid input")
            return self.get_user_input()

    def find_carrots(self):
        """
        Tells what happens on the board when finding carrot.
        """
        find_carrots = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    find_carrots += 1
        return find_carrots


def game_over():

    """
    End game or loose
    """
    user_input = input("Play again (Y/N)? \n").upper()
    if user_input == "Y":
        play_game()
    if user_input == "N":
        print("Thank you for playing!")
        exit()


def play_game():
    """
    Loops through the game.
    """
    print('''
========================================================================
                        Welcome to Carrotland!
The rowdy rabbit has almost taken all of the carrots from the garden from
underground. He left the leaves sticking up so you don't know if there is
a carrot attached to it.
There are 5 carrots left! Find them before the rowdy rabbit does!

        X = Found a carrot!
        - = Only leaves!
                            Good Luck!
======================================================================
''')
    """
    Creating board for game
    """
    print("Find the carrots! You have 10 turns!\n")
    game_board = Board([[" "] * 5 for i in range(5)])
    guess_board = Board([[" "] * 5 for i in range(5)])
    Carrots.create_carrots(game_board)
    """
    Tells turns and how many remains.
    The users input and checks for same guess.
    """
    turns = 10
    while turns > 0:
        Board.print_board(guess_board)
        print(f"You have {turns} turns remaining")
        user_row, user_column = Carrots.get_user_input(object)
        if guess_board.board[user_row][user_column] == "-"\
                or guess_board.board[user_row][user_column] == "X":
            print("You searched there already")
            user_row, user_column = Carrots.get_user_input(object)
            """
            Checks for if user find/not find carrot.
            """
        if game_board.board[user_row][user_column] == "X":
            print("YEAH! You found a carrot!")
            guess_board.board[user_row][user_column] = "X"
        else:
            print("Sorry! No carrot!")
            guess_board.board[user_row][user_column] = "-"
            """
            If user win or loose.
            """
        if Carrots.find_carrots(guess_board) == 5:
            print("CONGRATULATION! You found all 5 carrots! Yum! carrotcake!")
            game_over()
        else:
            turns -= 1
            if turns == 0:
                print("Sorry! The rabbit found the carrots before you did!")
                print("Game Over")
                game_over()


if __name__ == "__main__":
    play_game()

