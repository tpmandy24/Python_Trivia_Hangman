import random
def playGame():
    print("Pom Pom Purin Adventure") #fill in the name of the game --> feel free to add a font to make your game more fancy!
    startGame = input("Welcome to Pom Pom Purin's Cafe!\nPress '!' to begin the adventure that awaits you! (make sure to press enter after each input :)") # Welcome message --> Feel free to change any of the dialogue to
    # personalize your game!
    if startGame == "!":
        firstChoice()
def firstChoice(): #these are the options the players can pick from at the start of the game --> after the player picks one, each option leads to a different game
    print("Pom Pom Purin doesn't have his flan! Help him find his flan!")
    prompt = input("\nPress 1 to look in the kitchen and 2 to look in Pom Pom Purin's house") #write a prompt that allows the player to pick option 1 or option 2
    prompt = int(prompt)
    if prompt == 1: #the player chooses option 1
        print("Oh no! Pom Pom Purin is deathly scared of the kitchen!") #what happened when the player picked option 1? write it out!
        print("Play hangman to help Pom Pom Purin find a friend to go with him") #because the player picked option 1, they now have to play hangman
        play_hangman()
    if prompt == 2: #the player chooses option 2
        print("Pom Pom Purin decides to look in Pom Pom Purin's house, but Pom Pom Purin's house is messy!") #what happened when the player picked option 2? write it out!
        print("Play trivia to help Pom Pom Purin organize the house")
        odds_and_evens()

def play_hangman():
    possibleWords = ["hello kity", "kuromi", "keroppi", "melody", "pekkle"] #write out possible words for hangman that go with the theme of your game --> the word that users will have  
    # to guess is one of these words
    answer = random.choice(possibleWords) #picks one of the above words (possibleWords) for users to guess for hangman
    user = input("Guess a letter! Make sure all the letters are lowercase :)")
    ctr = 0 # helps with the indexing
    answerCtr = 0 # helps with indexing --> both ctr and answerCtr are used to update the word after the user guesses a letter
    showUp = "" # controls what is outputted to the user
    showUpCtr = 0 # helps with outputting the default string (_ _ _ )
    letterAnswers = 0 #counts how many letters the user has guessed correctly
    guessed = False # boolean displaying if the whole word has been guessed
    while showUpCtr < len(answer): # prints the default string (_ _ _ _ )
            showUp += "_ "
            showUpCtr += 1
    guesses = 0
    guessed = False
    while guessed == False and guesses<= len(answer)+3: # the user only has a limited number of guesses that is equal to the length of the word plus three
        while answerCtr < len(answer): # goes through every character in the word and updates all letters in the word based on what letter the user guessed
            if user == answer[answerCtr]: 
                showUp = showUp [0: ctr] + user + showUp [ctr+1:]
                letterAnswers += 1 
            ctr += 2
            answerCtr +=1
        print (showUp)
        if letterAnswers != len(answer): # this means that the user hasn't guessed all the correct characters
            user = input("Guess another letter")
            ctr = 0
            answerCtr = 0
            guesses +=1
        else: # all the words have been guessed
            guessed = True
    if guessed == True: #win hangman
        print("Yay! You won! Pom Pom Purin sees a pile of left over flan in the distance. Help Pom Pom Purin sort through them by playing a fun trivia :) \n") #after winning hangman, the players now have to play odds and evens
        playTrivia()
    else: #lose hangman
        print("Oh no! Pom Pom Purin can't find a friend to go to the kitchen with him.") #the user has lost --> what happens when they lose hangman?
        print("Pom Pom Purin is too scared to continue. Hopefully he can find his flan next time!") #let the user now that it is the end of the game now 

def odds_and_evens():
    choice = input("Type 'e' for evens and 'o' for odds") #the user will pick whether they want evens or odds
    possible = [1,2,3,4,5] 
    comp = random.choice(possible)
    print("\nPick a number: 1,2,3,4,5. Pom Pom Purin will also pick a number\nIf both your numbers add to what you previously chose (odd or even) then you win") 
    #instructions for the game
    num = input ("Type a num")
    num = int(num)
    sum = num + comp
    if sum%2 == 0 and choice == "e": #the user chose evens and wins the game
        print("\nYay! You won! Pom Pom Purin picked the number:", comp, "Pom Pom Purin finds the Flan on Pom Pom Purin's desk after he organized it! \n Pom Pom Purin thanks you so much for helping him find his flan!") #let user know what number the computer picked, 
        #and end the game
    elif sum%2 !=0 and choice == "o": #the user chose odds wins the game
        print("\nYay! You won! Pom Pom Purin picked the number:", comp, "Pom Pom Purin finds the honey on Pom Pom Purin's desk after he organized it! \n Pom Pom Purin thanks you so much for helping him find his flan!") #let user know what number the computer picked, 
        #and end the game
    else: #the user has lost the game
        print("\nOh no! You lost :(, Pom Pom Purins picked the number:", comp, "Pom Pom Purin gets too tired from organizing Pom Pom Purin's house and decides to go take a nap. \n He hopes that you can come back and help him find his flan next time!") #let user know what number the computer picked, and end the game

def playTrivia():
    print("First, pick a number. Then, a statement will appear and you will have to decide if it's true or false! type 't' for True or 'f' for False ")
    choice = input("Choose one of these numbers to determine your question: 1, 2, 3, 4, 5")
    choice = int(choice)
    user = ""
    answer = False
    if(choice == 1):
        user = input("Berkeley was founded in 1865") #feel free to replace this with a statement that is false!
        answer = False
    if (choice == 2):
        user = input("There are underground steam tunnels at Berkeley") #feel free to replace this with a statement that is true!
        answer = True
    if (choice == 3):
        user = input("Winnie the Pooh met Queen Elizabeth and sang her a special song for her birthday!") #replace with a statement that is true!
        answer = True
    if (choice == 4):
        user = input("Winnie the Pooh has two older brothers!") #replace with a statement that is false!
        answer = False
    if (choice == 5):
        user = input("There is a Poohsticks championships held every year in England!") #replace with a statement that is true!
        answer = True
    if user == 't' and answer: #the user correctly chose true --> game is over and the user has won
        print("\n Yay! You won! Winnie the Pooh finds his honey in the the pile of logs! Winnie the Pooh thanks you so much for helping him find his honey :)") #tell the user they won the game! 
    elif user == 'f' and answer == False: #the user correctly chose false- -> game is over and the user has won
        print("\n Yay! You won! Winnie the Pooh finds his honey in the the pile of logs! Winnie the Pooh thanks you so much for helping him find his honey :)") #tell the user they won the game! 
    else:#the user picked the wrong answer --> game is over and the user has lost
        print("\n Oh no! Winnie the Pooh just remembered that Tiger's party is starting soon so he has to go prepare for the party! \n Winnie the Pooh hopes that you can come back and help him find his honey next time!") #tell the user they lost the game
    

    

playGame() # runs the game