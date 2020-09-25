import random
def printAList(a_list):
    print()
    for charecter in a_list:
        print(charecter, end="")
    print()
def reveals(guess, word, reveal):
    c = 0
    for alphabet in word:
        if guess == alphabet:
            reveal[c] = guess
        c += 1
def hasLost(reveal, tries, guessed, word):
    if tries == 8 and set(guessed) != set(word):
            print("You lost!")
    else: 
        printAList(reveal)  
def mainMenu():  
    words = ['java', 'kotlin', 'python', 'javascript', "flutter", "dart", "github", "object"]
    print("Guess a word from the following -\njava,kotlin,python,javascript,flutter,dart,github,object\nYou have 8 Chances!\nLet's Go!")
    word = list(random.choice(words))
    guessed = list()
    guessed_but_not_in_word = list()
    reveal = list(["-"]) * len(word)
    printAList(reveal) 
    tries = 0
    while True:
        if tries < 8:
            while True:
                print("Input a letter: ", end=" ")
                guess = input()
                if guess.isalpha() and guess.islower() and len(guess) == 1:
                    break
                elif guess.isalpha() == False or guess.islower() == False or len(guess) != 1:
                    if len(guess) != 1:
                        print("You should input a single letter")
                        printAList(reveal)
                    elif guess.isupper() or guess.isalpha() == False:
                        print("It is not an ASCII lowercase letter")
                        printAList(reveal)
        else:
            break
        if guess in word and guess not in guessed :
            reveals(guess, word, reveal)
            guessed.append(guess)
            hasLost(reveal, tries, guessed, word)
        elif guess not in word and guess not in guessed_but_not_in_word:
            tries += 1
            print("No such letter in the word")
            guessed_but_not_in_word.append(guess)
            hasLost(reveal, tries, guessed, word)
        elif guess in word and guess in guessed or guess not in word and guess in guessed_but_not_in_word:
            print("You already typed this letter")
            printAList(reveal)
        if set(guessed) == set(word):
            print("You guessed the word!")
            print("You survived!")
            break 
print("Instruction - Enter alphabets to guess a random word selected from a pool of words!")
print()
print("H A N G M A N")
print()
while True:
    print('Type "play" to play the game, "exit" to quit:', end = " ")
    play = input()
    print()
    if play != "play":
        break
    else:
        mainMenu()
        print()


 



    

     
