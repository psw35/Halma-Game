import tkinter as tk
from tkinter import messagebox

# create a board GUI class
class Board:
    def __init__(self, boardsize):
        # initialize window
        self.window = tk.Tk()
        # initialize an array to hold the grid squares
        self.grid = []
        # create a variable to hold the player who had the last turn
        self.prevPlayer = ""
        self.replay = False

        for index in range(boardsize):
            self.grid.append([])

        # adjust dimensions, add a title
        self.window.geometry("500x500")
        self.window.title("Halma")

        # create a frame for the grid
        canvasFrame = tk.Frame(self.window)
        canvasFrame.pack()

        # create grid of canvases
        for rowIndex in range(boardsize):
            for colIndex in range(boardsize):
                # create a grid square
                square = tk.Canvas(canvasFrame, width=25, height=25, bg="white")

                # boolean for if a piece occupies the square
                square.occupied = tk.BooleanVar()
                square.occupied = False

                # boolean for if the square can be moved into
                square.moveable = tk.BooleanVar()
                square.moveable = False

                # variable to hold the player color
                square.player = tk.StringVar()
                square.player = ""

                # create starting pieces if in a square in either player's camp
                if rowIndex == 0 and colIndex < 4:
                    square.create_oval((10, 10, 20, 20), fill="black")
                    square.occupied = True
                    square.player = "black"
                elif rowIndex == 1 and colIndex < 3:
                    square.create_oval((10, 10, 20, 20), fill="black")
                    square.occupied = True
                    square.player = "black"
                elif rowIndex == 2 and colIndex < 2:
                    square.create_oval((10, 10, 20, 20), fill="black")
                    square.occupied = True
                    square.player = "black"
                elif rowIndex == 3 and colIndex < 1:
                    square.create_oval((10, 10, 20, 20), fill="black")
                    square.occupied = True
                    square.player = "black"
                elif rowIndex == boardsize - 4 and boardsize - 2 < colIndex < boardsize:
                    square.create_oval((10, 10, 20, 20), fill="white")
                    square.occupied = True
                    square.player = "white"
                elif rowIndex == boardsize - 3 and boardsize - 3 < colIndex < boardsize:
                    square.create_oval((10, 10, 20, 20), fill="white")
                    square.occupied = True
                    square.player = "white"
                elif rowIndex == boardsize - 2 and boardsize - 4 < colIndex < boardsize:
                    square.create_oval((10, 10, 20, 20), fill="white")
                    square.occupied = True
                    square.player = "white"
                elif rowIndex == boardsize - 1 and boardsize - 5 < colIndex < boardsize:
                    square.create_oval((10, 10, 20, 20), fill="white")
                    square.occupied = True
                    square.player = "white"
                # otherwise, do nothing
                else:
                    pass

                # add to the grid array
                self.grid[rowIndex].append(square)

                # if square contains one of the player's(black) pieces, allow a click
                if square.occupied:
                    # listen for a click
                    # when clicked, pass in the event and variables pertaining to the square and grid
                    square.bind("<Button-1>", 
                                lambda event, oldRow=0, oldCol=0, rowIndex=rowIndex,
                                colIndex=colIndex, player=square.player,
                                grid=self.grid: self.move(event, oldRow, oldCol, rowIndex, colIndex, player, grid))

                # add to the frame grid
                square.grid(row=rowIndex, column=colIndex)

        # run the window
        self.window.mainloop()

    # movement function
    def move(self, event, oldRow, oldCol, row, col, player, grid):
        # find the square that was clicked
        square = grid[row][col]
        # get the board size
        boardsize = len(grid)

        # wipe away any highlights on the board already
        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid)):
                if (rowIndex, colIndex) != (row, col):
                    grid[rowIndex][colIndex].configure(bg="white")
                    grid[rowIndex][colIndex].moveable = False

        # if a piece was clicked
        if square.occupied:
            # highlight the piece's grid square
            square.configure(bg="yellow")

            # for row in grid
            for rowIndex in range(len(grid)):
                # for column in grid
                for colIndex in range(len(grid)):
                    # determine available squares to move to:

                    # check northwest of highlighted square
                    if rowIndex == row - 1 and colIndex == col - 1:
                        # if an empty grid square, allow movement
                        if not grid[rowIndex][colIndex].occupied:
                            grid[rowIndex][colIndex].configure(bg="red")
                            grid[rowIndex][colIndex].moveable = True
                        # else if an occupied grid square, allow a hop if within boundaries of board
                        elif 0 < rowIndex - 1 and 0 < colIndex - 1:
                            if grid[rowIndex - 1][colIndex - 1].occupied == False:
                                grid[rowIndex - 1][colIndex - 1].configure(bg="red")
                                grid[rowIndex - 1][colIndex - 1].moveable = True
                    # check north of highlighted square
                    elif rowIndex == row - 1 and colIndex == col:
                        # if an empty grid square, allow movement
                        if not grid[rowIndex][colIndex].occupied:
                            grid[rowIndex][colIndex].configure(bg="red")
                            grid[rowIndex][colIndex].moveable = True
                        # else if an occupied grid square, allow a hop if within boundaries of board
                        elif 0 < rowIndex - 1:
                            if grid[rowIndex - 1][colIndex].occupied == False:
                                grid[rowIndex - 1][colIndex].configure(bg="red")
                                grid[rowIndex - 1][colIndex].moveable = True
                    # check northeast of highlighted square
                    elif rowIndex == row - 1 and colIndex == col + 1:
                        # if an empty grid square, allow movement
                        if not grid[rowIndex][colIndex].occupied:
                            grid[rowIndex][colIndex].configure(bg="red")
                            grid[rowIndex][colIndex].moveable = True
                        # else if an occupied grid square, allow a hop if within boundaries of board
                        elif 0 < rowIndex - 1 and colIndex + 1 < boardsize:
                            if grid[rowIndex - 1][colIndex + 1].occupied == False:
                                grid[rowIndex - 1][colIndex + 1].configure(bg="red")
                                grid[rowIndex - 1][colIndex + 1].moveable = True
                    # check west of highlighted square
                    elif rowIndex == row and colIndex == col - 1:
                        # if an empty grid square, allow movement
                        if not grid[rowIndex][colIndex].occupied:
                            grid[rowIndex][colIndex].configure(bg="red")
                            grid[rowIndex][colIndex].moveable = True
                        # else if an occupied grid square, allow a hop if within boundaries of board
                        elif 0 < colIndex - 1:
                            if grid[rowIndex][colIndex - 1].occupied == False:
                                grid[rowIndex][colIndex - 1].configure(bg="red")
                                grid[rowIndex][colIndex - 1].moveable = True
                    # check east of highlighted square
                    elif rowIndex == row and colIndex == col + 1:
                        # if an empty grid square, allow movement
                        if not grid[rowIndex][colIndex].occupied:
                            grid[rowIndex][colIndex].configure(bg="red")
                            grid[rowIndex][colIndex].moveable = True
                        # else if an occupied grid square, allow a hop if within boundaries of board
                        elif colIndex + 1 < boardsize:
                            if grid[rowIndex][colIndex + 1].occupied == False:
                                grid[rowIndex][colIndex + 1].configure(bg="red")
                                grid[rowIndex][colIndex + 1].moveable = True
                    # check southwest of highlighted square
                    elif rowIndex == row + 1 and colIndex == col - 1:
                        # if an empty grid square, allow movement
                        if not grid[rowIndex][colIndex].occupied:
                            grid[rowIndex][colIndex].configure(bg="red")
                            grid[rowIndex][colIndex].moveable = True
                        # else if an occupied grid square, allow a hop if within boundaries of board
                        elif rowIndex + 1 < boardsize and 0 < colIndex - 1:
                            if grid[rowIndex + 1][colIndex - 1].occupied == False:
                                grid[rowIndex + 1][colIndex - 1].configure(bg="red")
                                grid[rowIndex + 1][colIndex - 1].moveable = True
                    # check south of highlighted square
                    elif rowIndex == row + 1 and colIndex == col:
                        # if an empty grid square, allow movement
                        if not grid[rowIndex][colIndex].occupied:
                            grid[rowIndex][colIndex].configure(bg="red")
                            grid[rowIndex][colIndex].moveable = True
                        # else if an occupied grid square, allow a hop if within boundaries of board
                        elif rowIndex + 1 < boardsize:
                            if grid[rowIndex + 1][colIndex].occupied == False:
                                grid[rowIndex + 1][colIndex].configure(bg="red")
                                grid[rowIndex + 1][colIndex].moveable = True
                    # check southeast of highlighted square
                    elif rowIndex == row + 1 and colIndex == col + 1:
                        # if an empty grid square, allow movement
                        if not grid[rowIndex][colIndex].occupied:
                            grid[rowIndex][colIndex].configure(bg="red")
                            grid[rowIndex][colIndex].moveable = True
                        # else if an occupied grid square, allow a hop if within boundaries of board
                        elif rowIndex + 1 < boardsize and colIndex + 1 < boardsize:
                            if grid[rowIndex + 1][colIndex + 1].occupied == False:
                                grid[rowIndex + 1][colIndex + 1].configure(bg="red")
                                grid[rowIndex + 1][colIndex + 1].moveable = True
                    # otherwise, do nothing
                    else:
                        pass

                    # if grid square not occupied by a player or AI piece, allow a click to move
                    if not grid[rowIndex][colIndex].occupied or grid[rowIndex][colIndex].player == player:
                        # on click, call the function with old and new coordinates of piece
                        grid[rowIndex][colIndex].bind("<Button-1>", lambda event, oldRow=row, oldCol=col, rowIndex=rowIndex, colIndex=colIndex, player=player, grid=grid: self.move(event, oldRow, oldCol, rowIndex, colIndex, player, grid))
        
        # else if a grid square able to be moved to was clicked
        elif square.moveable and self.prevPlayer != player:
            # get the old grid square
            oldSquare = grid[oldRow][oldCol]
            # delete the canvas's contents
            oldSquare.delete("all")
            # change occupied boolean to reflect no piece
            oldSquare.occupied = False
            oldSquare.player = ""
            
            # add a piece to the new square
            square.create_oval((10, 10, 20, 20), fill=player)
            # set that it's occupied
            square.occupied = True
            # set the square's player
            square.player = player
            # get rid of red highlight
            square.configure(bg="white")
            # set player as previous player, then check for game win
            self.prevPlayer = player
            self.checkGame(grid)

        # else if player clicks on a valid square, but it's not their turn yet
        elif square.moveable and self.prevPlayer == player:
            # give an error popup
            tk.messagebox.showinfo("Error", "Please wait your turn.")

        # otherwise, player clicked on an invalid square
        else:
            # give an error popup
            tk.messagebox.showinfo("Error", "Error! Invalid move.")

    # win/lose checking function
    def checkGame(self, grid):
        # create booleans for each color's win
        whiteWin = False
        blackWin = False
        # get the board size
        boardsize = len(grid)

        # check if all white pieces in the black camp
        if grid[0][0].player == "white" and grid[0][1].player == "white" and grid[0][2].player == "white" and grid[0][3].player == "white":
            if grid[1][0].player == "white" and grid[1][1].player == "white" and grid[1][2].player == "white":
                if grid[2][0].player == "white" and grid[2][0].player == "white":
                    if grid[3][0].player == "white":
                        # set a white win to true
                        whiteWin = True
                    # otherwise can't be a white win
                    else:
                        whiteWin = False
                # otherwise can't be a white win
                else:
                    whiteWin = False
            # otherwise can't be a white win
            else:
                whiteWin = False
        # otherwise can't be a white win
        else:
            whiteWin = False
        
        # check if all black pieces in the white camp
        if grid[boardsize - 1][boardsize - 4].player == "black" and grid[boardsize - 1][boardsize - 3].player == "black" and grid[boardsize - 1][boardsize - 2].player == "black" and grid[boardsize - 1][boardsize - 3].player == "black":
            if grid[boardsize - 2][boardsize - 3].player == "black" and grid[boardsize - 2][boardsize - 2].player == "black" and grid[boardsize - 2][boardsize - 1].player == "black":
                if grid[boardsize - 3][boardsize - 2].player == "black" and grid[boardsize - 3][boardsize - 1].player == "black":
                    if grid[boardsize - 4][boardsize - 1].player == "black":
                        # set a black win to true
                        blackWin = True
                    # otherwise can't be a black win
                    else:
                        blackWin = False
                # otherwise can't be a black win
                else:
                    blackWin = False
            # otherwise can't be a black win
            else:
                blackWin = False
        # otherwise can't be a black win
        else:
            blackWin = False

        # if all black pieces in white camp
        if blackWin:
            # print game over message, and ask player if they wish to go again
            # if yes
            if messagebox.askyesno("Game Over", "Black wins! Play again?"):
                # set replay to true
                self.replay = True
            # destroy old board
            self.window.destroy()
        # else if all white pieces in black camp
        elif whiteWin:
            # print game over message, and ask player if they wish to go again
            # if yes
            if messagebox.askyesno("Game Over", "White wins! Play again?"):
                # set replay to true
                self.replay = True
            # destroy old board
            self.window.destroy()

# main function
def main():
    # create initial board
    newBoard = Board(8)

    # while player wants to keep playing, keep making new boards
    while newBoard.replay:
        newBoard = Board(8)

# call main function
main()