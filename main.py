# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                 tic tac toe X_O game                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# 1- import the packages
from tkinter import *
import random

# 2. start of all functions


def next_true(row,col):
    global player

    if game_btns[row][col]['text'] == ""  and  cheak_winner()== False :
        # player number 1
        if player == players[0] :
            game_btns[row][col]["text"] =player  # put x in this position

            if cheak_winner() == False : # still playing
                #1. make the turen on anoter player
                lable.config(text=players[1] + " turn")
                player=players[1]
            elif  cheak_winner() == True:
                lable.config(text=players[0] + " is the winner ^_^")

            elif cheak_winner() == 'tie':
                lable.config(text="No one is the winner *_*")
        # player number 2
        elif player == players[1]:
            game_btns[row][col]["text"] = player  # put x in this position

            if cheak_winner() == False:  # still playing
                # 1. make the turen on anoter player
                lable.config(text=players[0] + " turn")
                player = players[0]
            elif cheak_winner() == True:
                lable.config(text=players[1] + " is the winner ^_^")

            elif cheak_winner() == 'tie':
                lable.config(text= "No one is the winner *_*")

def cheak_winner():
    # check all 3 horizontal conditions
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg="cyan")
            game_btns[row][1].config(bg="cyan")
            game_btns[row][2].config(bg="cyan")
            return True

    # check all 3 vertical conditions
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg="cyan")
            game_btns[1][col].config(bg="cyan")
            game_btns[2][col].config(bg="cyan")
            return True

    # check diagonals conditions
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][2].config(bg="cyan")
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][0].config(bg="cyan")
        return True

    # if there are no empty spaces left
    if cheak_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')

        return 'tie'

    else:
        return False

def cheak_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def start_new_game():
    global player
    player = random.choice(players)
    lable.config(text=(player + " turn"))


    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")


#3- the GUI  of the game
window = Tk()
window.title ('tic tac toe X O game')

players = ["X" ,"O"]                  # what is the name of all players (who are the players )
player = random.choice(players)       # to select randomly  one player from all players in the game
# create all Button that we will play with and put zeros as initial values
game_btns =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# design the top title and restart Button

lable = Label(text= player +' turn'  , font=('consolas' ,40) )
lable.pack(side='top')

restart_btn =Button(text="Restart" , font=('consolas' ,20) , command=start_new_game ) #command=start_new_game  not command=start_new_game()
restart_btn.pack(side='top')

# design the  frame of the game Buttons
frame_btn= Frame(window)
frame_btn.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] =Button(frame_btn , text="" ,font=('consolas' ,20), width= 4 , height=2 , command=lambda col=col ,row=row : next_true(row,col) )
        game_btns[row][col].grid(row=row , column =col)


window.mainloop() #