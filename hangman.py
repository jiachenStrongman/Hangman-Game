#PA 1 - Hangman
#Jiachen Zhao SID 1545047 JISZHAO
#CSE 30 Spring 2022

#This is my submission for the hangman game.

#I loosely followed the template but the objective for this program
#was to first sort the dictionary file of all of its words by length
#and store each word into a dictionary of words by length
#so it would be like {3:[are, can, bat], 4:[rare, blow, four], etc.}
#so then by user choice, or default, the random can pick a word by length
#i kind of went overboard with time.sleep but i wanted to give the game some life while you played

import random
import time


def import_dictionary(fileName):
    wordList = [] #list of words to store

    #populate wordList
    with open(fileName, 'r') as words:
        wordList = words.read().splitlines()

    #dictinary with empty lists ready to be populated with corresponding words by length
    wordDict = {3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}

    for i in range(3,13):
        for j in wordList:
            if (i == (len(j.strip()))): #for each word that has 3 spaces in front
               wordDict[i].append(j.strip()) #woo hoo dictionary is sorted
    return(wordDict)
    

def giveBuffer(x):
    #this is to add my personal touch to the program
    #the text buffer makes it less cluttered
    for i in range(x):
        print('.')
        time.sleep(.03)

def get_game_options():
    size = 0
    lives = -1
    #function to get the word size and the lives the player wants
    try:
        print("Please chose a word length between 3 to 12: ")
        length = int(input())
        #setting the input to being an integer will cause the program to raise an exception if user inputs non-int
        if ((length > 12) or (length < 3)):
            raise Exception("Okay, looks like I'm going to choose for you")
            length = int(random.randrange(3, 13, 1))
    except:
        #i just want to give the user a second chance
        #just in case there was a mis inuput or anything like that
        print("Hey do this right") 
        time.sleep(2)
        giveBuffer(2)
        print("Please chose a word length between 3 to 12: ")
        try:
            length = int(input())
            if ((length > 12 or length < 3)):
                raise Exception("Okay, looks like I'm going to choose for you")
                time.sleep(1)
                giveBuffer(3)
                length = int(random.randrange(3, 13, 1))
        except:
            print("Okay, looks like I'm going to choose for you")
            time.sleep(1)
            giveBuffer(3)
            length = int(random.randrange(3, 13, 1))
    finally:
        size = length
        print("Your word size is " + str(size) + " letters.")
    giveBuffer(3)
    #it will perform essentially the same thing as word size but instead of random it will stick to default value
    lives = 5 #default lives value
    try:
        print("Please chose the number of lives between 1 to 10. Default is 5")
        lives = int(input())
        if((lives > 10) or (lives < 1)):
            raise Exception("Looks like we're going with the default.")
            time.sleep(1)
            giveBuffer(3)
            lives = 5
    except:
        print("Looks like we're going with the default.")
        time.sleep(1)
        giveBuffer(3)
        lives = 5
    finally:
        print("You have " + str(lives) + " lives.")
        time.sleep(1)
        giveBuffer(5)
        print("Good luck, you might need it")
    return (size, lives)

def checkWord(x, word):
    position = [] #placeholder for which position in the word the letter is
    if(not x.isalpha()):
        print("My guy, that's not even a letter...")
        return [99]
    else:
        if (x.upper() in word.upper()):
            for i in range(len(word)):
                if(word[i].upper() == x.upper()):
                    position.append(i)
            return position
        else:
            return [99]
    
#this function will check to see if the letter guessed is in the word or not and give the position of the letter



        
def letsPlay(size, lives, dictionary): #perform game functions and will give proper output
    
    guesses = 0 #sets the amount of guesses to comapre with lives

    letters = [] #list of letters that will store guessed letters

    guessBoard = [] #this is a list that will store the string that is the board of the game

    word = dictionary[size][int(random.randrange(0, len(dictionary[size]), 1))] #pulls a random word from its specific word size list


    for i in range(size):
        guessBoard.append('__')
    if('-' in word): #this replaces the blank letter for a hyphen 
        for i in range(len(word)):
            if(word[i] == '-'):
                guessBoard[i] = '-'
                break
    while (guesses < lives):
        whereWord = []
        letters = list(dict.fromkeys(letters)) #this removes the any duplicates that would form in the guessed list
        for i in letters:
            #makes sure that non-letter guesses are stored
            if (not i.isalpha()):
                letters.remove(i)
            if(len(i) > 1):
                letters.remove(i)
        #corresponds to where the correct letter would be in the word
        #if whereWord still returns 99 then the guess is wrong thus removing the need for a true false value as well, we can do both in one
        print("letters chosen:",end=" ")
        for i in range(len(letters)):
            print(letters[i] + ',', end=" ")
        print('') #newline
        for j in guessBoard:
            time.sleep(0.02)
            print(j, end=" ")
        time.sleep(0.02)
        print("Lives: " + str(lives), end=" ")
        for x in range(guesses):
            time.sleep(0.02)
            print("X", end="")
        for y in range(lives - guesses):
            time.sleep(0.02)
            print(("O"), end="")
        print("") #new line
        print("Please chose a new letter >>>")
        newLetter = input()
        whereWord = checkWord(newLetter, word)
        if(whereWord[0] < len(word)):
            for i in range(len(whereWord)):
                guessBoard[whereWord[i]] = newLetter.lower()
                letters.append(newLetter.lower())
            if(''.join(guessBoard) == word):
                print("Nice job! You got the word. The word is " + str(word) + "!")
                guesses = 999
                break
            print('.')
            print("You guessed right!")
            print(".")
            
        elif(guesses == lives - 1):
            print('.')
            print("Out of lives. GG EZ")
            giveBuffer(3)
            print("The word to guess was " + str(word))
            guesses = 99
            
        else:
            print(".")
            print("You guessed wrong, it's gonna cost you a life")
            print(".")
            letters.append(newLetter)
            guesses = guesses + 1
                   

#main game performing all functions

wordDict = import_dictionary('dictionary.txt') #populate word dictionary

keepPlaying = True #keeps the while loop going if the player wants to keep playing

while(keepPlaying):
    print("Welcome to the Hangman Game!")
    time.sleep(2)
    giveBuffer(10)
    print("Guess Wisely...")
    time.sleep(2)
    giveBuffer(3)
    wordSize, lives = get_game_options() #set lives and word size
    letsPlay(wordSize, lives, wordDict)
    playAgain = '2332'

    while(not playAgain.isalpha()):
        print("Would you like to play again? [Y/N]")
        playAgain = input()
        playAgain = playAgain.upper() 
        if((not playAgain == 'Y') and (not playAgain == 'N')):
            playAgain = '000'
            print("That wasn't one of the choices. Please chose [Y/N]")
        
    if(playAgain == 'N'):
        keepPlaying = False
        print("Goodbye")

#the Y/N doesnt work right and you have to make the players responses all upper and the word to work with so that letters match
