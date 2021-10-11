import random
import sys
import time

#creating an empty list for the board
print("welcome to tictac toe,")
print("a python project created by Hugh Signoriello \nto learn python programming")
time.sleep(2)
print("I hope you enjoy playing!")
rows, cols = (3, 3)
# board = [["-"]*cols]*rows
board = [["-" for i in range(cols)] for j in range(rows)]
print("_______")
print("|"+board[0][0] + "|" + board[0][1]+ "|" + board[0][2]+"|")
print("|"+board[1][0] + "|" + board[1][1]+ "|" + board[1][2]+"|")
print("|"+board[2][0] + "|" + board[2][1]+ "|" + board[2][2]+"|")

moves = 0
play = True
win = False

 #display game
def display_board():
    print("     ")
    print("______")
    print("|"+board[0][0] + "|" + board[0][1]+ "|" + board[0][2]+"|")
    print("|"+board[1][0] + "|" + board[1][1]+ "|" + board[1][2]+"|")
    print("|"+board[2][0] + "|" + board[2][1]+ "|" + board[2][2]+"|")

def user_turn():
    global moves
    row = int(input("choose a row from 1-3: "))
    col = int(input("choose a col from 1-3: "))
    #default pyton inputs are string so we need to type cast input to integer via int();
    # if((row or col) < 1 or (row or col) > 3):
    if(row <1 or col<1 or row > 3 or col > 3 or board[row-1][col-1] != "-"):
        print("invalid index plese try again")
        user_turn()
    else:
        board[row-1][col-1] = 'X'
        #print("you chose board["+str(row)+"]["+str(col)+"]")
        moves+=1
        return

#computer choice:
def computer_turn():
    
    if(moves<=9):
        comp_r, comp_c = random.randint(0,2), random.randint(0,2) 
        if(str(board[comp_r][comp_c]) == "-"):
            print("computer turn: ")
            time.sleep(2)
            board[comp_r][comp_c] = 'O'
            return
        else:
            computer_turn()

#check win\

def evaluate_win():
    global win
    if(win==True):
        print("Game over!")
        print(check_win()+" is the winner!")
        play_again()
    #print("no winner yet!")
       

def check_win():
    global win
    global moves
    if(moves == 9):
        print("Tie")
        win = True;
        return "No one"
    for r in range(3):
        #check row
        if (board[r][0] == 'X' and board[r][1] == 'X'  and board[r][2] == 'X'):
            win = True;
            return 'X'
        if (board[r][0] == 'O' and board[r][1] == 'O'  and board[r][2] == 'O'):
            win = True;
            return 'O'
        if (board[0][r] == 'X' and board[1][r] == 'X'  and board[2][r] == 'X'):
            win = True;
            return 'X'
        if (board[0][r] == 'O' and board[1][r] == 'O'  and board[2][r] == 'O'):
            win = True;
            return 'O'

    if (board[0][0] == 'O' and board[1][1] == 'O'  and board[2][2] == 'O'):
        win = True;
        return 'O'

    if (board[0][0] == 'X' and board[1][1] == 'X'  and board[2][2] == 'X'):
        win = True;
        return 'X'
    
    if (board[0][2] == 'O' and board[1][1] == 'O'  and board[2][0] == 'O'):
        win = True;
        return 'O'

    if (board[0][2] == 'X' and board[1][1] == 'X'  and board[2][0] == 'X'):
        win = True;
        return 'X'

def play_again():
    global play
    global win
    global board

    play_again = str(input("would you like to play again? yes/no: "))
    if(play_again == "yes"):
        board = board = [["-" for i in range(cols)] for j in range(rows)]
        win = False
        return
    elif(play_again == "no"):
        print("thankyou for playing")
        print("closing game...")
        play = False;
        time.sleep(10)
        sys.exit()
    print("please type either yes or no")
    play_again()

#now running the the game
while(play==True):
    user_turn()
    display_board()
    check_win()
    evaluate_win()

    computer_turn()
    display_board()
    check_win()
    evaluate_win()

    
    

   