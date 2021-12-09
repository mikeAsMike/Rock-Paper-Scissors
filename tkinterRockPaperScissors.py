# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:54:20 2021

@author: mike
"""
# Play Rock, Paper, Scissors against your computer.

import tkinter as tk
from tkinter import StringVar
import time 
import random

root = tk.Tk()
root.title('Rock, Paper, Scissors Game')
root.geometry('600x300+100+100')

output_string = StringVar() 
you_chose = int()
query = random.randint(0,2)
list_hand = ['rock', 'paper', 'scissors']
winner = StringVar()

computer_score = int()
player_score = int()

# These three functions get called by whichever choice the player makes.
def rock():
    global you_chose
    you_chose = 0
    ready_set_go()
   
def paper():
    global you_chose
    you_chose = 1
    ready_set_go()
    
def scissors():
    global you_chose
    you_chose = 2
    ready_set_go()

# Countdown resembles the 1, 2, 3 count that people do prior to showing their hand
def ready_set_go(): 
    winner.set('')
    list_countdown = ['One', 'Two', 'Three']
    
    for i in list_countdown:
        print(i)         
        output_string.set(str(i))
        root.update()
        print(you_chose)
        time.sleep(.5)
        
    computer_turn()

# Shows the player's and computer's choice in label_output
def computer_turn():    
    global query
    query = random.randint(0,2)
    output_string.set('You chose {} and the computer chose {} .'.format(list_hand[you_chose], list_hand[query]))
    
    who_won()

# Shows who won the round in label_winner         
def who_won():
    global player_score
    global computer_score
    
    if you_chose == query:         
        winner.set("It's a tie!")
                
    elif you_chose == 0 and query == 2:           
        winner.set('You won!')
        player_score += 1
               
    elif you_chose == 1 and query == 0:        
        winner.set('You won!')
        player_score += 1
                
    elif you_chose == 2 and query == 1:
        winner.set('You won!')
        player_score += 1
        
    elif you_chose == 0 and query == 1:
        winner.set('The computer wins, Better luck next time.')
        computer_score += 1
        
    elif you_chose == 1 and query == 2:
        winner.set('The computer wins. Better luck next time.')
        computer_score += 1  
        
    elif you_chose == 2 and query == 0:
        winner.set('The computer wins. Better luck next time.')
        computer_score += 1
   
    else:
        winner.set('Scoring error')
        
    label_player_score.config(text = 'Your score: ' + str(player_score))
    label_computer_score.config(text = "The computer's score: " + str(computer_score))

# Widgets        
frame_top = tk.Frame(root, bg='silver')
frame_top.pack(side='top', fill='x')

label_choose = tk.Label(frame_top, text='Choose rock, paper, or scissors.', bg='silver')
label_choose.config(font=(30))
label_choose.pack(padx=4, pady=2)

frame_buttons = tk.Frame(root)
frame_buttons.pack(side='top')

button_rock = tk.Button(frame_buttons, text='Rock', width=15, command=rock, bg='#009999', fg='white', font=10, borderwidth=0)
button_rock.pack(side='left', padx=10, pady=5)

button_paper = tk.Button(frame_buttons, text='Paper', width=15, command=paper, bg='#009999', fg='white', font=10, borderwidth=0)
button_paper.pack(side='left', padx=10, pady=5)

button_scissors = tk.Button(frame_buttons, text='Scissors', width=15, command=scissors, bg='#009999', fg='white', font=10, borderwidth=0)
button_scissors.pack(side='right', padx=10, pady=5)

frame_output = tk.Frame(root)
frame_output.pack(fill='x')

label_output = tk.Label(frame_output, textvariable=output_string)
label_output.config(font=50)
label_output.pack()

label_winner = tk.Label(frame_output, textvariable=winner)
label_winner.config(font=60, fg='blue')
label_winner.pack()

frame_score = tk.Frame(root)
frame_score.pack(side='bottom')

label_player_score = tk.Label(frame_score)
label_player_score.config(font=40)
label_player_score.pack(side='left', padx=30, pady=20)

label_computer_score = tk.Label(frame_score)
label_computer_score.config(font=40, padx=30, pady=20)
label_computer_score.pack()

root.mainloop()