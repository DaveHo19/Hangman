from email import message
from tkinter import *
import WordList as word_list


def buttonCommand(alphabet):
    message(alphabet)
    
class PlayerInput:
    def __init__(self, location):
        alphabetlist = word_list.GetAlphabetList()
        frame = Frame(location)
        buttonDict = {}
        for i in range(0, 26):
            buttonDict[i] = Button(frame, text=alphabetlist[i], command=lambda: buttonCommand(alphabetlist[i]))
        
        frame.pack()