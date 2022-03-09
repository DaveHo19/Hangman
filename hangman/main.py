from fileinput import filename
from queue import Empty
from tkinter import *
import random
import tkinter
import WordList as word_list
import MainImage as main_image
import PlayerInput as player_input


def CheckInput():
    
    if len(inputData.get())>1:
        return False
    else:
        if inputData.get().isdigit():
            return False
        elif inputData.get() == '':
            return False
        elif inputData.get() in inputList:
            return False
        else:
            return True
    
def CheckAnswer():
    stritem = selectedWord
    global displayedWord
    global inputList
    if CheckInput():
        userdata = inputData.get()
        inputList.append(userdata)
        labelEntered.config(text=GetEnteredValue())
        userInput.delete(0, 'end')
    else:
        userInput.delete(0, 'end')
        return
    
    checkstr = stritem.replace(userdata[0], '-')
    
    if checkstr != stritem:
        templist = list(displayedWord)
        for i in range(0, len(stritem)):
            if (checkstr[i] == '-'):
                templist[i] = stritem[i]
        
        displayedWord = "".join(templist)        
        labelQuestion.config(text=displayedWord)
        if displayedWord == selectedWord:
            result = "You Win!\n The Answer Is " + displayedWord
            labelLife.config(text=result)
            GameResultScene()

        
    else:
        global life
        life -= 1
        labelQuestion.config(text=displayedWord)
        labelLife.config(text=life)
        UpdateImage()
        if life == 0:
            result = "You Lose!\n The Answer Is " + selectedWord; 
            labelLife.config(text=result)
            GameResultScene()
        

def GetEnteredValue():
    if len(inputList) <= 0:
        return ""
    else:
        data = ""
        for item in inputList:
            data = data + item + " "
        return data
    
def ConvertQuestionToSpecialChar(stritem):
    strdata = ''
    for i in stritem:
        strdata += "-"
    return strdata

def UpdateImage():
    global gameImage
    initialLife = 7
    main_image.MainImage.displayCanvasImage(gameImage, initialLife - life)
    
def InitialContent():
    global life 
    global words
    global selectedWord
    global displayedWord
    global inputData
    global inputList
    inputData = StringVar()
    life = 7
    words = word_list.GetAnimalList()
    selectedWord = random.choice(words)
    displayedWord = len(selectedWord) * "-"
    inputList = []

def GameScene():
    global labelTitle
    global gameImage
    global labelQuestion
    global labelEntered
    global userInput
    global btnSubmit
    global labelLife
    
    labelTitle = Label(main, text='Hangman')
    labelTitle.pack()
    gameImage = main_image.MainImage(main)
    main_image.MainImage.displayCanvasImage(gameImage, 0)
    InitialContent()
    labelQuestion = Label(main, text=displayedWord)
    labelLife = Label(main, text='Current Life: ' + str(life))
    labelEntered = Label(main, text=GetEnteredValue())
    userInput = Entry(main, textvariable=inputData, width=10)
    btnSubmit = Button(main, text='Submit Answer', command=CheckAnswer)
    labelLife.pack()
    labelQuestion.pack()
    labelEntered.pack()
    userInput.pack()
    btnSubmit.pack()

def GameResultScene():
    global btnRestart
    btnSubmit.pack_forget()
    btnRestart = Button(main, text='Restart', command=RestartGameScene)
    btnRestart.pack()

def RestartGameScene():
    btnRestart.pack_forget()
    ResetGameScene()
    GameScene()

def ResetGameScene():
    gameImage.mainCanvas.pack_forget()
    labelTitle.pack_forget()
    labelQuestion.pack_forget()
    labelEntered.pack_forget()
    labelLife.pack_forget()
    userInput.pack_forget()
    btnSubmit.pack_forget()
    

main = Tk()
main.geometry('300x400')
GameScene()
main.mainloop()  