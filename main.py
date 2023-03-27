import csv, random

#Input functions
def MainMenu(options):
    """Accepts a list of options, converts it into a dictionary and prints
  out each item with a number. Then it accepts user input. If the input
  is invalid, it loops untill the users enters a valid input"""
    # converts the options list into a dictonary for easy comparison later
    optionDict = {}
    counter = 1
    for i in options:
        optionDict[str(counter)] = i
        counter += 1

    #prints out options
    for i in optionDict:
        print(f"{i} : {optionDict[i]}")

    #Accepts user input
    userInput = input("Please enter the number of your desired selection: ")
    while userInput not in optionDict.keys():
        print("Please enter a valid option")
        userInput = input(
            "Please enter the number of your desired selection: ")
    return int(userInput)

def numberInput(stat):
    """Accepts an input from a user and if it is numeric, if not it just makes user enter 
  again untill it is, and returns input as a str"""
    userInput = input(f"Please enter the {stat}: ")
    while not userInput.isnumeric():
        print("Please enter a valid value")
        userInput = input(f"Please enter the {stat}: ")
    return userInput

def typesInput(stat = "type"):
    """Acepts an input from a user and if it is an invalid type, it asks the user to enter again
  untill it is valid, and returns input as a str"""
    userInput = input(f"Please enter the {stat}: ").lower()
    types = [
        "normal", "fire", "water", "grass", "flying", "fighting", "poison",
        "electric", "ground", "rock", "psychic", "ice", "bug", "ghost",
        "steel", "dragon", "dark", "fairy",""
    ]
    while userInput not in types:
        print("Please enter a valid type")
        userInput = input(f"Please enter the {stat}: ").lower()
    return userInput

#Formatting
#converts CSV file to list
with open("Pokemon.csv", "r") as file:
    reader = csv.reader(file)
    csvList = []
    for i in reader:
        csvList.append(i)

# gets the list for the headers
headers = csvList[0]
# finds the number of clumns
numberOfColumns = len(headers)
# nested list of pokemon with stats
content = csvList[1:]

#finds the length of each cell and returns it as list
cellLengths = []
for column in range(numberOfColumns):
    highestLength = 0
    for row in csvList:
        if len(row[column]) + 3 > highestLength: # goes through each option in the column and sees if it the longest
            highestLength = len(row[column]) + 3 
            #updates the cell length
            # 3, because i think it looks very nice when it is 3
    cellLengths.append(highestLength) #adds the longest cell length into the list

def tableify(list):
    """Function to print the list from the csv file as a table"""
    output = ""
    for index in range(len(list)): #loops through the cells for the pokemon in the list
        currentItem = str(list[index])
        while len(currentItem) < cellLengths[index]: #adds spaces to each string untill it is of the desired length
            currentItem += " "
        output += currentItem # adds the current cell to a str
    return output
    
def output(results):
    """Outputs the results form a list as a table"""
    print(tableify(headers)) #prints table headers
    outputStr = ""
    for i in results: #loops through  the list of pokemon
        outputStr += tableify(i) # converts it to a str and adds it
        if not i == results[-1]:
            outputStr += "\n" #adds a new line if it is not the last pokemon
    print(outputStr) #print

# Search Functions
def numberOfPokemon():
    """Displays n number of Pokémon according to user input"""
    numberToDisplay = int(numberInput("number of Pokémon to display")) #user input
    # if the user asks for more pokemon than in the database
    if numberToDisplay > len(content):
        print("Please enter a number lesser than or equal to number of Pokémon")
        numberToDisplay = int(numberInput("number of Pokémon to display"))

    results = [] #adds the pokemon to the list of results
    for i in range(numberToDisplay):
        results.append(content[i])

    output(results)

def pokemonWithType():
    """Displays the first pokemon with a specified type"""
    pokemonType = typesInput() # user input
    results = []
    counter = 0
    while not results:
        #loops through each pokemon in the list, and sees if the types match those specified
        type1 = content[counter][2].lower()
        type2 = content[counter][3].lower()
        if type1 == pokemonType or type2 == pokemonType:
            results += [content[counter]]
            print(bool(results))
        counter += 1
    output(results)

def pokemonWithTotalStat():
    """Displays all the pokemon with a specified total base stat"""
    results = []
    while not results:
        userTotalBaseStat = numberInput("total base stat") #user input
        for i in content: #loops through each pokemon anc compares total base stat
            totalBaseStat = i[4]
            if totalBaseStat == userTotalBaseStat:
                results.append(i) #if it matches, adds it to the list of results
        if not results: #if there are no pokemon with the total base stat, it loops again and asks for user input
            print("There are no Pokémon with the minimum total base stat speicfied!")
        else:
            output(results)

def pokemonWithMinStats():
    """Returns the number of pokemon special attack, special defence and speed above or equal to those specified"""
    results = []
    while not results:
        userSpecialAttack = int(numberInput("special attack")) # user input
        userSpecialDefence = int(numberInput("special defence"))
        userSpeed = int(numberInput("speed"))
        for i in content: #loops through the pokemon and adds those with stats above those specified to the reuskts list
            specialAttack = int(i[8])
            specialDefence = int(i[9])
            speed = int(i[10])
            if specialAttack >= userSpecialAttack and specialDefence >= userSpecialDefence and speed >= userSpeed:
                results.append(i)
        if not results: # if there are no pokemon with the values specified, it loops and asks for new input
            print("There are no pokemon with the values specified!")
        else:
            output(results)
        
def legendaryPokemonWithTypes():
    """Displays all the legendary pokemon with two types specified"""
    results = []
    while not results:
        userType1 = typesInput("first type") #user input
        userType2 = typesInput("second type")
        for i in content:
            LegendaryStaus = i[-1].lower() #check to see if it is legendary
            if LegendaryStaus == "true":
                LegendaryBool = True
            else:
                LegendaryBool = False
            type1 = i[2].lower()
            type2 = i[3].lower() #condition to see if the types of the pokemon match those specified
            matchingTypes = (userType1 == type1 and userType2 == type2) or (userType1 == type2 and userType2 == type1)
            if matchingTypes and LegendaryBool: # adds it to the list or results if it matches
                results.append(i)
        if not results: #if there are no matching pokemon, it loops and asks for input again
            print("There are no legendary pokemon with the types specified!")
        else:
            output(results)

def surpriseMe():
    """Displays a random pokemon"""
    randomPokemon = [random.choice(content)] # chooses a random pokemon from the list of pokemon
    output(randomPokemon)
    
#event loop
print("Pokédex Search Engine")
done = False
while not done:
    options = [
        "Display Pokémon with their types and statistics",
        "Display the first Pokémon of a Type of your choice",
        "Display all Pokémon with Total Base stat of your choice",
        "Display all Pokémon with a minimum set of stats",
        "Display all lengendary Pokémon of specific Type1 and Type2",
        "Surprise me!",
        "Quit",
    ]
    option = MainMenu(options)
    if option == 7:
        done = True
    elif option == 1:
        numberOfPokemon()
    elif option == 2:
        pokemonWithType()
    elif option == 3:
        pokemonWithTotalStat()
    elif option == 4:
        pokemonWithMinStats()
    elif option == 5:
        legendaryPokemonWithTypes()
    elif option == 6:
        surpriseMe()  
print("Bye!")
