# Hangman
## Description
* A simple Hangman game implemented using Python!
* Contains a simple UI for player to play it!
## Table of Contents
* [Preview](#Preview)
* [Installation](#Installation)
* [About The Application](#About-The-Application)
* [Development Concept](#Development-Concept)
## Preview
![main](https://user-images.githubusercontent.com/100736557/157576943-c9576d97-e1a5-4816-b310-29aab4af0724.PNG)
* The first scene open the application. 
* Player able to guess the alphabet by enter in the field provided. 
* Player can click on submit button to submit their answer.

![lose](https://user-images.githubusercontent.com/100736557/157577833-ed9dfc66-c619-4a20-a536-3aeff51e76c2.PNG)
* When player submit a wrong answer, player life will be deducted.
* The game image will changed.
* It will also shows out what alphabet player had input below the question.

![correct](https://user-images.githubusercontent.com/100736557/157577883-ebc2876d-b95f-467f-a86b-b59b8ea75f5e.PNG)
* When player submit a correct answer, player life will remain unchange.
* The question will changed and shows the correct alphabet entered.

![win](https://user-images.githubusercontent.com/100736557/157578088-91a4fba6-3011-4169-8514-6b4ed9dbd361.PNG)
* When player successfully guess all the alphabet
* Player able to restart the game by clicking the restart button

![lose](https://user-images.githubusercontent.com/100736557/157578168-9999a405-10fc-44f6-a0d1-40bf828a4a35.PNG)
* When player failed to guess the alphabet, the question text will review the correct answer. 
* Player able to restart the game by clicking the restart button.


## Installation
* You can download the file using ```git clone``` using HTTPS or 
```https://github.com/DaveHo19/Python-Hangman.git```
* The python library required will be:
  * Tkinter
## About The Application
The hangman application is developed using Python programming language in Visual Studio Code. The GUI of the application is constructed using tkinter. The main concept applied to implement hangman is random, which applied to random select a sentences based on vocabulary list provided. For more details, check on [Development Concept](#Development-Concept)

## Development Concept
The concept of develop the 'Hangman' application is based on the step below:
* Create a list of words 
* Create player lifes to indicate how many chances to enter wrong answer. 
* Randomly choose one of the words from the list created and store into ```selectedWord```
* Create a ```displayedWord``` and set the string value to list of ```*``` based on ```selectedWord``` length 
  * Example: if ```selectedWord``` is ```apple```, then the ```displayWord``` will be ```*****```.  
* Implement player input checking method to avoid player enter unrelevant character such as number or symbols, and avoid enter repeated character. 
  * Examples of unrelevant character: *, /, =, 1, 3 etc
* Implement checking answer method after the alphabet entered by player and check it with selected word.
  * If the alphabet entered is matched, replace the ```*``` in ```displayWord``` to the correct alphabet, the life will remain unchange.
  * If the alphabet entered is not matched, decrease the player lifes. 
* Next, check on the player lifes.
  * If the player lifes reach 0, the correct answer will shown and player able to play next game. 
  * If the player lifes above 0, proceed to next step.
* Then, check if there is still a ```*``` in ```displayedWord``` to determine player able to enter next character or not. 
  * If there are no ```*``` in the ```displayedWord```, the correct answer will shown and player able to play next game.

