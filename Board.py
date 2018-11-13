

class Board:

	def __init__(self, size):

		self.size = size
		self.white = []
		self.black = []
		self.win = False
		self.board = [['.' for i in size] for i in size]
		self.winLog = "Win!"
		self._isBlack = True

	def _inBoard(self,x,y):

		return x>=0 and x<self.size and y>=0 and y<self.size

	def _isValidMove(self,x,y):

		return self._inBoard(x,y) and self.board[x][y]=='.'

	def printBoard(self):

		for i in range(self.size):
			print(board[i])

	def updateBoard(self,x,y):

		if self._isBlack:
			if self._isValidMove(x,y):
				self.black.append([x,y])
				self.board[x][y] = 'x'
				self._isBlack = False
			else:
				print("Error input, please enter a valid coordinate")

		else:
			if self._isValidMove(x,y):
				self.white.append([x,y])
				self.board[x][y] = 'o'
				self._isBlack = True
			else:
				print("Error input, please enter a valid coordinate")

		printBoard()
		if self.checkWin(x,y):
			print("Black") if self._isBlack else print("White")
			print(welf.winLog)
			self.win = True

	def checkWin(self,x,y,c):

		if _checkH(x,y,c) or _checkV(x,y,c) or _checkL(x,y,c) or _checkR(x,y,c):
			return True
		else: 
			return False

	def checkH(self,x,y,cmp):
		temp_count = 1
		tempx = x
		tempy = y
		for i in range(4):
			tempy += 1
			if self._inBoard(tempx,tempy) && self.board[tempx][tempy] == c:
				temp_count +=1
			else:
				break
		tempy = y
		for i in range(4):
			tempy-=1
			if self._inBoard(tempx,tempy) && self.board[tempx][tempy] == c:
				temp_count +=1
			else:
				break

		if temp_count>4: 
			return True
		else:
			return False 




