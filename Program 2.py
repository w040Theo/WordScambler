## Author: Theoren Hayne
## Date: 2020-11-22
## Description: a program that presents the user with a “Mad Libs” type
#  game, where a random choice of words are read from a file, then interjected into a story read from another file.

print("The Itsy Bitsy Aardvark")
print("")

def inputValidation(_input): #Validation for user input
    global correctInput

    if (_input == "a" or _input == "b" or _input == "c" or _input == "d" or _input == "e"):
        correctInput = True
    else:
        correctInput = False #accepts the letters above if not say Bad Letter!
        print("Bad Letter!")
    return (correctInput)



def DisplayStory(animal,actionEd,adjective,noun,actionTwo,actionThree,adverb):

    print("Your Completed Story: ")
    story = open("the_story_file.txt") #Basic Printing and writing in story file
    storyRead = story.readlines()

    for x in range(len(storyRead)):#putting the line to uppercase if it is chosen
        storyRead[x] = storyRead[x].replace("\n","")
        storyRead[x] = storyRead[x].replace("_","")
        storyRead[x] = storyRead[x].replace("1",animal.upper())
        storyRead[x] = storyRead[x].replace("2",actionEd.upper())
        storyRead[x] = storyRead[x].replace("3",adjective.upper())
        storyRead[x] = storyRead[x].replace("4",noun.upper())
        storyRead[x] = storyRead[x].replace("5",actionTwo.upper())
        storyRead[x] = storyRead[x].replace("6",actionThree.upper())
        storyRead[x] = storyRead[x].replace("6",adverb.upper())
        print(storyRead[x])
    
choices = open("the_choices_file.csv") #writing in CSV file
choicesLines = choices.readlines()
translation = {"a":1,"b":2,"c":3,"d":4,"e":5} 
        

correctInput = False 
for i in range(len(choicesLines)):
    choicesLines [i]=choicesLines[i].replace("\n","")
    linesSplit = choicesLines[i].split(",")#splitting lines with a comma
    sectionTitle = linesSplit [0]
    print("Please choose ", sectionTitle)

    for option in range (len(linesSplit)): #Displaying options using for loop
        if option == 1:
            print("a)",linesSplit[option])     
        if option == 2:
            print("b)",linesSplit[option])
        if option == 3:
            print("c)",linesSplit[option])
        if option == 4:
            print("d)",linesSplit[option])
        if option == 5:
            print("e)",linesSplit[option])
       

    userInput = ""
    

    while userInput == "" or correctInput == False:
        userInput = input("Enter choice (a-e): ") #Entering input and tracking choice
        userInput = userInput.lower()
        correctInput = inputValidation(userInput) #Validating choice
    if correctInput == True:
        correctInput = False
    indx = translation[userInput]
    if i == 0:
        animal = linesSplit[indx]
    elif i == 1:
        actionEd = linesSplit[indx]
    elif i == 2:
        adjective = linesSplit[indx]
    elif i == 3:
        noun = linesSplit[indx]
    elif i == 4:
        actionTwo = linesSplit[indx]
    elif i == 5:
        actionThree = linesSplit[indx]
    elif i == 6:
        adverb = linesSplit[indx]

DisplayStory(animal,actionEd,adjective,noun,actionTwo,actionThree,adverb)

