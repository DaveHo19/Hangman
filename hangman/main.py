from tkinter import *
import GameScene as game_scene
import MenuScene as menu_scene

main = Tk()
main.geometry('300x450')
main.title('Hangman')
menu_scene.SetUpMenuScene(main)
game_scene.SetUpGameScene(main)

menu_scene.InitialMainContent()
main.eval('tk::PlaceWindow . center')
main.mainloop()  