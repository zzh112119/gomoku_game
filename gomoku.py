import Board as b
import ast
import Eval_funcs as ef
import Queue as q
import time

class Gomoku:

    def __init__(self):
        self.white_list = []
        self.black_list = []
        self.cam_list = []
        self.playerInput = []

    def trans(self,(y,x)):
        return [x,y]

    def readFile(self):
        self.cam_list=[]
        f = open("game.txt","r")
        contents = f.readlines()
        for content in contents:
            coordinates = content.rstrip().split(',')
            self.cam_list.append([int(coordinates[0]),int(coordinates[1])])
        f.close()
        print(self.cam_list)

    def checkNewMove(self):
        checker = 0

        for elem in self.cam_list:
            if (elem not in self.white_list and elem not in self.black_list):
                checker+=1
                self.playerInput = elem

        if checker>1:
            print("More than one plays detected!!!")
            return False

        elif checker==1:
            print("Player moves at:", self.playerInput)
            return True

        else:
            print("No new plays detected")
            return False

    def playerNewMove(self):
        self.readFile()

        while not self.checkNewMove():
            self.readFile()
            time.sleep(0.5)

        return self.playerInput

    def enterPosition(self,board):
        while True:
            while True:
                try:    
                    move = ast.literal_eval(raw_input("Please enter your move in format '(x,y)': "))
                    break
                except(ValueError,SyntaxError,TypeError):
                    print("error")
                    continue
            piece = self.trans(move)
            if(board._isValidMove((piece[0],piece[1]))):
                print(piece[0])
                break
            else:
                print("enter valid position")
                continue
        print("Black moved {0}".format(move))
        return piece


    def gomoku(self):
        board = b.Board()

        board.printBoard()

        tlimit = 2;
        print("player 1 moves first")
        piece = self.enterPosition(board)
        # board._isBlack = True
        board.updateBoard((piece[0],piece[1]))
        self.black_list.append([piece[0],piece[1]])

        print("GomoBot moves")
        # board._isBlack = False
        move = ef.secondmove(board, piece[0], piece[1])
        piece = self.trans(move)
        board.updateBoard((piece[0],piece[1]))
        self.white_list.append([piece[0],piece[1]])

        while not board.win:

            print("Player moves")
            raw_input('Press enter to continue: ')
            # piece = self.enterPosition(board)
            piece = self.playerNewMove()
            # board._isBlack = True
            board.updateBoard((piece[0],piece[1]))
            self.black_list.append([piece[0],piece[1]])

            if(board.win):
                break

            print("GomoBot moves")
            move = ef.nextMove(board,tlimit,3)
            board.updateBoard(move)
            self.white_list.append([move[0],move[1]])
            print("Black:", self.black_list)
            print("White:", self.white_list)

        print("GAME OVER")

if __name__=="__main__":
    G = Gomoku()
    # G.readFile()
    G.gomoku()







# class piece:
#     def __init__(self,isBlack):
#         if isBlack:
#             self.isBlack = True
#             self.color = "BLACK"
#             self.symbol = "x"
#         else:
#             self.isBlack = False
#             self.color = "WHITE"
#             self.symbol = "o"

#     def trans(self,(y,x)):
#         arr = [x,y]
#         return arr


# import ast

# def gomoku():
#     board_size = 8
#     connect_size = 5

#     print(board_size)
#     h = 8
#     w = 8
#     p = piece(True)

#     game_over = False;

#     board = [['.' for x in range(w)] for y in range(h)]
#     print("player 1 moves first")
#     for i in range(8):
#         print(board[i])
#     while True:
#         try:    
#             move = ast.literal_eval(raw_input("Please enter your move in format '(y,x)': "))
#             break
#         except(ValueError,SyntaxError,TypeError):
#             continue
#     # move = board(move)
#     print("Black moved {0}".format(move))
#     update = p.trans(move)
#     board[update[0]][update[1]] = 'x'


#     while not game_over:
#         print("player 2 moves") 
#         for i in range(8):
#             print(board[i])
#         while True:
#             try:    
#                 move = ast.literal_eval(raw_input("Please enter your move in format '(y,x)': "))
#                 break
#             except(ValueError,SyntaxError,TypeError):
#                 continue
#         # move = board(move)
#         print("white moved {0}".format(move))
#         update = p.trans(move)
#         board[update[0]][update[1]] = 'o'   

#         print("player 1 moves") 
#         for i in range(8):
#             print(board[i])
#         while True:
#             try:    
#                 move = ast.literal_eval(raw_input("Please enter your move in format '(y,x)': "))
#                 break
#             except(ValueError,SyntaxError,TypeError):
#                 continue

#         # move = board(move)
#         print("black moved {0}".format(move))
#         update = p.trans(move)
#         print(update[0])
#         print(update[1])
#         board[update[0]][update[1]] = 'x'

#         game_over = True

#     print("Game over")

# if __name__=="__main__":
#     gomoku()

