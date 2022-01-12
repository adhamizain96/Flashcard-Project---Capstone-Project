#!/usr/bin/env python
# coding: utf-8

# In[4]:


#tkinter - standard Python interface to the Tcl/Tk GUI toolkit               
from tkinter import *
import pandas as p
import random

#constant is a type of variable whose value cannot be changed
FONT_1 = ('Courier', 40, 'italic')
FONT_2 = ('Courier', 40, 'bold')

#{} - an empty dictionary without any items is written
#current_card - random choice of the to_learn deck
current_card = {}
#to_learn - all the original french words
to_learn = {}

#try block - lets you test a block of code for errors
#except block - lets you handle the error
#finally block - lets you execute code, regardless of the result of the try and except blocks
try:
    data_2 = p.read_csv('words_to_learn.csv')
except:
    data_1 = p.read_csv('french_words.csv')
    print(data_1)
    #to_dict() - convert the DataFrame to a dictionary
    #orient - indication of expected JSON string format
    #records - list like [{column -> value}, … , {column -> value}] - converts it to a dictionary
    to_learn = data_1.to_dict(orient = 'records')
else:
    to_learn = data_2.to_dict(orient = 'records')

def next_card():
    #global - variables that are created outside of a function
    global current_card, flip_timer
    #after_cancel - stop the after function
    window.after_cancel(flip_timer)
    #this creates a second dictionary current_card
    current_card = random.choice(to_learn)
    #canvas - rectangular area intended for drawing pictures or other complex layouts
    #fill = 'black' - color
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(card_word, text = current_card['French'], fill = 'black')
    canvas.itemconfig(card_front_image, image = card_front_img)
    #after() - calls the callback function once after a delay milliseconds (ms) within Tkinter’s main loop
    flip_timer = window.after(5000, func = flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text = 'English', fill = 'white')
    canvas.itemconfig(card_word, text = current_card['English'], fill = 'white')
    canvas.itemconfig(card_front_image, image = card_back_img)
    
def correct_card():
    #remove() - takes a single element as an argument and removes it from the list
    to_learn.remove(current_card)
    data_2 = p.DataFrame(to_learn)
    #to_csv() - write object to a comma-separated values (csv) file
    #note - do not want the index to be stored in csv file - 1,2,3...
    data_2.to_csv('words_to_learn.csv', index = False)
    next_card()

#Tk() - allows you to register and unregister a callback function which will be called from the Tk mainloop
window = Tk()
window.title('French → English Flashcards')
#padx and pady - a distance - designating external padding on each side of the slave widget
#bg - background color
window.config(padx = 50, pady = 50, bg = '#B1DDC6')

#note - wait 5 seconds before flipping the card
flip_timer = window.after(5000, func = flip_card)

canvas = Canvas(width = 800, height = 526)
#front and back image
card_front_img = PhotoImage(file = 'card_front.png')
card_back_img = PhotoImage(file = 'card_back.png')
#create_image() - places the image
card_front_image = canvas.create_image(400, 263, image = card_front_img)
#card_title - french and english title
#note - the x/y positions are relative to the canvas
card_title = canvas.create_text(400, 150, text = '', font = FONT_1)
#card_word - french and english words
#note - the x/y positions are relative to the canvas
card_word = canvas.create_text(400, 263, text = '', font = FONT_2)
#highlightthickness = 0 - gets rid of the border
canvas.config(bg = '#B1DDC6', highlightthickness = 0)
#columnspan = 2 - to make space for the check_image and cross_image
canvas.grid(row = 0, column = 0, columnspan = 2)

#creating buttons and giving commands to those buttons
cross_image = PhotoImage(file = 'wrong.png')
incorrect_answer_button = Button(image = cross_image, highlightthickness = 0, command = next_card)
incorrect_answer_button.grid(row = 1, column = 0)
check_image = PhotoImage(file = 'right.png')
correct_answer_button = Button(image = check_image, highlightthickness = 0, command = correct_card)
correct_answer_button.grid(row = 1, column = 1)

#need to call the function before the mainloop is executed
next_card()

#mainloop() - method in the main window that executes what we wish to execute in an application
window.mainloop() 


# In[ ]:




