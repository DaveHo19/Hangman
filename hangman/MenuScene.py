from tkinter import *
import GameScene as game_scene

def OpenGameScene():
    ClearMenu()
    game_scene.GameScene()

def ExitApplication():
    main.destroy()

def InitialMainContent():
    global applicationTitle
    global frameForBtn
    global btnPlay
    global btnExit
    applicationTitle = Label(main, text='Hangman', font=("Times New Roman", 16))   
    frameForBtn = Frame(main, width=100, height=100)
    btnPlay = Button(frameForBtn, text='Play', height=2, width=20, command=OpenGameScene).pack(pady=15)
    btnExit = Button(frameForBtn, text='Exit', height= 2, width=20, command=ExitApplication).pack(pady=15)

    applicationTitle.pack(side=TOP, pady=25)
    frameForBtn.pack(side=TOP, pady=10)

def ClearMenu():
    applicationTitle.destroy()
    frameForBtn.destroy()
    
def SetUpMenuScene(mainRoot):
    global main
    main = mainRoot
