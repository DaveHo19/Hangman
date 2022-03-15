from tkinter import *
import random
import WordList as word_list
import MainImage as main_image
import MenuScene as menu_scene

#return to main menu
def ReturnMenu():
    #delete every game scene component
    DestroyGameScene()
    #generate menu component
    menu_scene.InitialMainContent()

#check the player input
def CheckInput():
    #if player input more than 1 character, e.g. abc, return false
    if len(inputData.get())>1:
        return False
    else:
        #if player input is digit, e.g. 0-9, return false
        if inputData.get().isdigit():
            return False
        #if player input is empty, return false
        elif inputData.get() == '':
            return False
        #if player input is repeated alphabet, return false
        elif inputData.get() in inputList:
            return False
        else:
            return True

#check player input with selected word
def CheckAnswer():
    #access variable from everywhere, which allow to modify the variables
    global displayedWord
    global inputList
    stritem = selectedWord
    
    if CheckInput():
        #get player input
        userdata = inputData.get()
        #insert player input to inputList (for avoid repeated alphabet purpose)
        inputList.append(userdata)
        #update repeated alphabet ui
        labelGameEntered.config(text=GetEnteredValue())
        #clear player input box
        userInput.delete(0, 'end')
    else:
        userInput.delete(0, 'end')
        return
    #replace player alphabet with '-' if exists
    checkstr = stritem.replace(userdata[0], '-')
    
    #if there is differences between checkstr(the replaced str) and stritem(the actual answer)
    if checkstr != stritem:
        #convert displayedWord into list
        templist = list(displayedWord)
        for i in range(0, len(stritem)):
            #if checkstr(the replaced str) is '-'
            if (checkstr[i] == '-'):
                #tempList(the converted list) will replace with stritem(the actual answer)
                templist[i] = stritem[i]
                
        #displayedWord will assign the joined tempList
        displayedWord = "".join(templist)        
        #update displayedWord in ui
        labelGameQuestion.config(text=displayedWord)
        #if displayedWord equal to selectedWord, which mean there is no '-' in displayedWord
        if displayedWord == selectedWord:
            result = "You Win!\n The Answer Is " + displayedWord
            labelGameLife.config(text=result)
            GameResultScene()
    else:
        global life
        #decrease life
        life -= 1
        labelGameQuestion.config(text=displayedWord)
        #update life ui
        labelGameLife.config(text='Life(s):' + (life*"\u2764"), width=50)
        #update phaes
        UpdateImage()
        if life == 0:
            result = "You Lose!\n The Answer Is " + selectedWord; 
            labelGameLife.config(text=result)
            GameResultScene()
        
#get repeated word list
def GetEnteredValue():
    if len(inputList) <= 0:
        return ""
    else:
        data = ""
        for item in inputList:
            data = data + item + " "
        return data
    
#convert selectedWord to list of special characters
def ConvertQuestionToSpecialChar(stritem):
    strdata = ''
    for i in stritem:
        strdata += "-"
    return strdata

#update image phases 
def UpdateImage():
    global gameImage
    initialLife = 7
    main_image.MainImage.displayCanvasImage(gameImage, initialLife - life)

#initial game scene component
def InitialContent():
    #access variable from everywhere, which allow modify on these variables with global keyword
    global life 
    global words
    global selectedWord
    global displayedWord
    global inputData
    global inputList
    
    inputData = StringVar()
    life = 7
    #get word list
    words = word_list.GetWordList()
    #random choose 1 word from word list
    selectedWord = random.choice(words)
    displayedWord = len(selectedWord) * "-"
    inputList = []

def GameScene():
    #access variable from everywhere, which allow modify on these variables with global keyword
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
    
    #UI creation, design and settings
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
    btnBack = Button(btmNavFrame, text='Back', width=10, command=ReturnMenu).pack(side=LEFT, padx = 50)
    btnRestart = Button(btmNavFrame, text='Restart', width=10, command=RestartGameScene).pack(side=RIGHT, padx = 50)
    btmNavFrame.pack(fill=BOTH)
    
def RestartGameScene():
    #release bottom navigation frame in root
    btmNavFrame.pack_forget()
    ResetGameScene()
    GameScene()

def ResetGameScene():
    #release game scene component in root
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
    #get and assign the root 
    global mainRoot 
    mainRoot = main
    
def DestroyGameScene():
    #delete game scene components
    gameImage.mainCanvas.destroy()
    labelTitle.destroy()
    labelGameQuestion.destroy()
    labelGameEntered.destroy()
    labelGameLife.destroy()
    userInput.destroy()
    btnSubmit.destroy()
    topNavFrame.destroy()
    btmNavFrame.destroy()