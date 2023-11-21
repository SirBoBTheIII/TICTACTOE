board = [['_', '_', '_'], 
         ['_', '_', '_'], 
         ['_', '_', '_']]
turn = "X"
won = False
numberOfMoves = 1

def printBoard():
  print("Tic-Tac-Toe Board")
  print("    0    1    2")
  count = 0
  while count <= 2:
    print(count, board[count])
    count += 1

def makeMove():
  xPos = 3
  yPos = 3
  while(xPos < 0 or xPos > 2 or yPos < 0 or yPos > 2 or board[yPos][xPos] != '_'):
    xPos = int(input("Enter X coordinate of your piece: "))
    yPos = int(input("Enter Y coordinate of your piece: "))
  
  board[yPos][xPos] = turn



def checkWinner():
  rowNumber = 0
  while rowNumber < 3:
    if (board[rowNumber][0] == board[rowNumber][1] and board[rowNumber][1] == board[rowNumber][2] == turn):
      print("Winner Detected Horizontally ")
      return True
    rowNumber += 1
    
  columnNumber = 0
  while columnNumber < 3:
    if (board[0][columnNumber] == board[1][columnNumber] and board[1][columnNumber] == board[2][columnNumber] == turn):
      print("Winner Detected Vertically ")
      return True
    columnNumber += 1
    
  if board[0][0] == board[1][1] == board[2][2] == turn or board[0][2] == board[1][1] == board[2][0] == turn:
    print("Winner Detected Diagonally ")
    return True

  return False

def checkTie():
  printBoard()
  if numberOfMoves >= 9 and not checkWinner():
    print("The players have tied!")

while not won:
  printBoard()
  print("It is " + turn + "'s turn.")
  makeMove()
  numberOfMoves += 1
  
  if checkWinner():
    print(turn + " has won!")
    won = True
  elif numberOfMoves == 9:
    print("The players have tied!")
    won = True
  else:
    if turn == "X":
      turn = "O"
    else:
      turn = "X"