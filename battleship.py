from random import randint

#using a class here allows me to reset the board
class Battleship:

    def __init__(self):
        self.score = 0
        self.board = []

    #this function will reset the board each time so we always have the right amount of columns and rows
    def reset_board(self):
        for x in range(0, 5):
            self.board.append(["O"] * 5)

    #printing board so the user can visualize
    def print_board(self):
        for row in self.board:
            print " ".join(row)

    def random_row(self):
        return randint(0, len(self.board) - 1)

    def random_col(self):
        return randint(0, len(self.board) - 1)

    #starting the game:
    def play_battleShip(self):
        print "Let's play Battleship!"
        self.reset_board()
        self.print_board()
        print "You have four chances"
        for turn in range(4) :
            print "turn", turn+1
            ship_row = self.random_row()+1
            ship_col = self.random_col()+1
            guess_row = int(raw_input("Guess Row:"))
            guess_col = int(raw_input("Guess Col:"))


            if guess_row==ship_row and guess_col==ship_col :
                print "Congratulations! You sank my battleship!"
                self.score += 1
                break
            else :
                if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5) :
                    print "Oops, that's not even in the ocean."
                elif self.board[guess_row-1][guess_col-1]== "X" :
                    print "You guessed that one already."
                else :
                    print "You missed my battleship!"
                    self.board[guess_row-1][guess_col-1]= "X"
                    if turn ==3 :
                        print "Sorry, game over"
            self.print_board()
        print "the answer was row:", ship_row, "column:", ship_col
        print "your score is:", self.score
        self.play_again()



    def play_again(self):
        answer = raw_input("Want to play again? y/n ")
        if answer == "n" :
            print "Alright, bye!"
        elif answer == "y":
            self.board = []
            self.play_battleShip()
        else:
            print "Sorry, I didn't get that. See you next time!"



bs = Battleship()
bs.play_battleShip()
