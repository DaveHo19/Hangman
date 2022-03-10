from tkinter import *
import random
import WordList as word_list
import MainImage as main_image
import MenuScene as menu_scene

def ReturnMenu():
    DestroyGameScene()
    menu_scene.InitialMainContent()

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
        labelGameEntered.config(text=GetEnteredValue())
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
        labelGameQuestion.config(text=displayedWord)
        if displayedWord == selectedWord:
            result = "You Win!\n The Answer Is " + displayedWord
            labelGameLife.config(text=result)
            GameResultScene()
    else:
        global life
        life -= 1
        labelGameQuestion.config(text=displayedWord)
        labelGameLife.config(text='Life(s):' + (life*"\u2764"), width=50)
        UpdateImage()
        if life == 0:
            result = "You Lose!\n The Answer Is " + selectedWord; 
            labelGameLife.config(text=result)
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
    words = word_list.GetWordList()
    selectedWord = random.choice(words)
    displayedWord = len(selectedWord) * "-"
    inputList = []

def GameScene():
    global gameImage
    global labelTitle
    global labelGameQuestion
    global labelGameEntered
    global userInput
    global btnSubmit
    global labelGameLife
    global btnReturn
    global topNavFrame 
    global btmNavFrame
    
    topNavFrame = Frame(mainRoot)
    btnReturn = Button(topNavFrame, text="\u2b05", command=ReturnMenu).pack(side=LEFT)
    topNavFrame.pack(fill=BOTH, side=TOP)
    
    labelTitle = Label(mainRoot, text='Game', font=("Times New Roman", 16))
    labelTitle.pack()
    gameImage = main_image.MainImage(mainRoot)
    main_image.MainImage.displayCanvasImage(gameImage, 0)
    InitialContent()
    labelGameQuestion = Label(mainRoot, text=displayedWord)
    labelGameLife = Label(mainRoot, text='Life(s):' + (life*"\u2764"), width=50)
    labelGameEntered = Label(mainRoot, text=GetEnteredValue())
    userInput = Entry(mainRoot, textvariable=inputData, width=10)
    btnSubmit = Button(mainRoot, text='Submit Answer', command=CheckAnswer)
    labelGameLife.pack()
    labelGameQuestion.pack()
    labelGameEntered.pack()
    userInput.pack()
    btnSubmit.pack()
    btmNavFrame = Frame(mainRoot)
    btmNavFrame.pack(fill=BOTH)

def GameResultScene():
    global btnRestart
    global btnBack
    btnSubmit.pack_forget()
    topNavFrame.pack_forget()
    btnBack = Button(btmNavFrame, text='\u2b05', width=10, command=ReturnMenu).pack(side=LEFT, padx = 50)
    btnRestart = Button(btmNavFrame, text='Restart', width=10, command=RestartGameScene).pack(side=RIGHT, padx = 50)
    btmNavFrame.pack(fill=BOTH)
    
def RestartGameScene():
    btmNavFrame.pack_forget()
    ResetGameScene()
    GameScene()

def ResetGameScene():
    gameImage.mainCanvas.pack_forget()
    labelTitle.pack_forget()
    labelGameQuestion.pack_forget()
    labelGameEntered.pack_forget()
    labelGameLife.pack_forget()
    userInput.pack_forget()
    btnSubmit.pack_forget()
    topNavFrame.pack_forget()
    btmNavFrame.pack_forget()

def SetUpGameScene(main):
    global mainRoot 
    mainRoot = main
    
def DestroyGameScene():
    gameImage.mainCanvas.destroy()
    labelTitle.destroy()
    labelGameQuestion.destroy()
    labelGameEntered.destroy()
    labelGameLife.destroy()
    userInput.destroy()
    btnSubmit.destroy()
    topNavFrame.destroy()
    btmNavFrame.destroy()