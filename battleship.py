from random import randint

#using a class here allows me to reset the board
class Battleship:

    def __init__(self):
        self.score = 0
        self.board = []

#this function will reset the board each time so we always have the right amount of columns and rows
    def reset_board(self):
        for X in range(0, 5):
            self.board.append(["O"] * 5)

    #printing board so the user can visualize
    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def random_row(self):
        return randint(0, len(self.board)-1)

    def random_col(self):
        return randint(0, len(self.board)-1)

    #user input is validated, for row and column
    def user_guess(self, direction):
        while True:
            try:
                return int(input("Guess a " + direction + ": " ))
            except ValueError:
                print("that's not a number!")



    #starting the game:
    def play_battleShip(self):
        print("Let's play Battleship!")
        self.reset_board()
        self.print_board()
        ship_row = self.random_row()+1
        ship_col = self.random_col()+1
        print("You have four chances")
        for turn in range(4) :
            print("turn", turn+1)
            guess_row = self.user_guess("row")
            guess_col = self.user_guess("column")


            if guess_row==ship_row and guess_col==ship_col :
                print("Congratulations! You sank my battleship!")
                self.score += 1
                break
            else :
                if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5) :
                    print("Oops, that's not even in the ocean.")
                elif self.board[guess_row-1][guess_col-1]== "X" :
                    print("You guessed that one already.")
                else :
                    print("You missed my battleship!")
                    self.board[guess_row-1][guess_col-1]= "X"
                    if turn ==3 :
                        print("Sorry, game over")
            self.print_board()
        print("the answer was row:", ship_row, "column:", ship_col)
        print("your score is:", self.score)
        self.play_again()



    def play_again(self):
        answer = input("Want to play again? y/n ")
        if answer == "n" :
            print("Alright, bye!")
        elif answer == "y":
            self.board = []
            self.play_battleShip()
        else:
            print("Sorry, I didn't get that. See you next time!")


if __name__ == "__main__":
    bs = Battleship()
    bs.play_battleShip()
