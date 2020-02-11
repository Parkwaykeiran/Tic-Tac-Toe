# ~~~~~ GLOBAL VARIABLES ~~~~~ #


# create board as a variable and use a list to define positions 0-8 as -
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# if game is still in play
game_in_play = True

# is there a winner?
winner = None

# whos turn is it (X goes first)?
current_player = "X"


# ~~~~~ FUNCTIONS ~~~~~ #


# function to run the game
def play_game():

  # display initial empty board
  display_board()

  # loop game play until winner or tie
  while game_in_play:

   # handle a single turn
   handle_turn(current_player)

   # check if the game has ended
   check_if_game_over()

   # flip to the other player
   flip_player()

  # the game has ended, print winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie!")


# function to create and display the board
def display_board():
  print("")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("")


#function to play a turn of a player
def handle_turn(player):

  # geta postion to play from the player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # make sure the input is valid and the position is empty
  valid = False
  while not valid:

   # make sure input is 1-9
   while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid choice. Choose a position from 1-9: ")

   # translate input into int and take away 1 as board begins at 0
   position = int(position) - 1

   # ensure position is available
   if board[position] == "-":
     valid = True
   else:
      print("You can't play here. Try again.")

  # if valid, put the players name (X or O) onto the chosen input
  board[position] = player

  # show the updated board
  display_board()


# function to check if there is a winner or a tie
def check_if_game_over():
  check_if_win()
  check_if_tie()


# check if there is a winner
def check_if_win():

  # allows writing to a global variable defined outside the function
  global winner

 # check rows, columns and diagonals
  row_winner = check_rows()
  column_winner = check_columns()
  diagonals_winner = check_diagonals()

  # write to winner based on who won
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonals_winner:
    winner = diagonals_winner
  else:
    winner = None

  return


# check rows for a winner
def check_rows():

  # allow writing to variable outside this function
  global game_in_play

  # check if rows are equal not including a dash
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  # if any row does have a match then set game still going to false
  if row_1 or row_2 or row_3:
    game_in_play = False

  # check position for what player and return who won
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


# check columns for a winner
def check_columns():

  # allow writing to variable outside this function
  global game_in_play

  # check if columns are equal not including a dash
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  # if any column does have a match then set game still going to false
  if column_1 or column_2 or column_3:
    game_in_play = False

  # check position for what player and return who won
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return


# check diagonals for a winner
def check_diagonals():

  # allow writing to variable outside this function
  global game_in_play

  # check if diagonals are equal not including a dash
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"

  # if any diagonal does have a match then set game still going to false
  if diagonals_1 or diagonals_2:
    game_in_play = False

  # check position for what player and return who won
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  return


# check if tie
def check_if_tie():

  #global variable outside function
  global game_in_play

  # check board for any - (empty slots) and if there's none then end the game
  if "-" not in board:
    game_in_play = False
    return True
  else:
    return False


#change from player x - O or O - X
def flip_player():

  # global to write to variable stored outside this function
  global current_player

  # if current player is X then change it to O
  if current_player == "X":
    current_player = "O"

  # if current player is X then change it to O
  elif current_player =="O":
    current_player = "X"


# ~~~~~ START THE GAME ~~~~~ #
play_game()

# ~~~~~ END OF CODE ~~~~~ #
