from tkinter import *
import GameScene as game_scene
import MenuScene as menu_scene

main = Tk()
#side of ui
main.geometry('300x450')

main.title('Hangman')
#initial the root of menu scene
menu_scene.SetUpMenuScene(main)
#initial the root of game scene
game_scene.SetUpGameScene(main)

#initial the component in menu scene and display out.
menu_scene.InitialMainContent()
#display ui in center screen
main.eval('tk::PlaceWindow . center')
#execute ui
main.mainloop()  