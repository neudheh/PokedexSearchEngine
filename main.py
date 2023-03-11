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
  again untill it is"""
    userInput = input(f"Please enter the {stat}: ")
    while not userInput.isnumeric():
        print("Please enter a valid value")
        userInput = input(f"Please enter the {stat}: ")
    return userInput

def typesInput(stat = "type"):
    """Acepts an input from a user and if it is an invalid type, it asks the user to enter again
  untill it is valid"""
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

#Formatting fucntions
#converts CSV file to list
with open("Pokemon.csv", "r") as file:
    reader = csv.reader(file)
    csvList = []
    for i in reader:
        csvList.append(i)

#finds the number of columns
headers = csvList[0]
numberOfColumns = len(headers)
content = csvList[1:]

#finds the length of each cell and returns it as list
cellLengths = []
for column in range(numberOfColumns):
    highestLength = 0
    for row in csvList:
        if len(row[column]) + 3 > highestLength:
            highestLength = len(row[column]) + 3
    cellLengths.append(highestLength)

def tableify(list):
    """Function to print the list from the csv file as a table"""
    output = ""
    for index in range(len(list)): # We dont want to print the legendary status
        currentItem = str(list[index])
        while len(currentItem) < cellLengths[index]:
            currentItem += " "
        output += currentItem
    return output
    
def output(results):
    """Outputs the results form a list as a table"""
    print(tableify(headers))
    for i in results:
        print(tableify(i))

# Search Functions
def numberOfPokemon():
    """Displays n number of Pokémon according to user input"""
    numberToDisplay = int(numberInput("number of Pokémon to display"))
    if numberToDisplay > len(content):
        print("Please enter a number lesser than or equal to number of Pokémon (800)")
        numberToDisplay = int(numberInput("number of Pokémon to display"))

    results = []
    for i in range(numberToDisplay):
        results.append(content[i])

    output(results)

def pokemonWithType():
    """Displays the first pokemon with a specified type"""
    pokemonType = typesInput()
    for i in content:
        type1 = i[2].lower()
        type2 = i[3].lower()
        if type1 == pokemonType or type2 == pokemonType:
            results = [i]
            break
    output(results)

def pokemonWithTotalStat():
    """Displays all the pokemon with a specified total base stat"""
    userTotalBaseStat = numberInput("total base stat")
    results = []
    while not results: 
        for i in content:
            totalBaseStat = i[4]
            if totalBaseStat == userTotalBaseStat:
                results.append(i)
        if not results:
            print("There are no Pokémon with the minimum total base stat speicfied!")
        else:
            output(results)

def pokemonWithMinStats():
    """Returns the number of pokemon special attack, special defence and speed above those specified"""
    userSpecialAttack = int(numberInput("special attack"))
    userSpecialDefence = int(numberInput("special defence"))
    userSpeed = int(numberInput("speed"))
    results = []
    for i in content:
        specialAttack = int(i[8])
        specialDefence = int(i[9])
        speed = int(i[10])
        if specialAttack >= userSpecialAttack and specialDefence >= userSpecialDefence and speed >= userSpeed:
            results.append(i)
    if not results:
        print("There are no pokemon with the values specified!")
    else:
        output(results)
        
def legendaryPokemonWithTypes():
    """Displays all the legendary pokemon with two types specified"""
    userType1 = typesInput("first type")
    userType2 = typesInput("second type")
    results = []
    for i in content:
        LegendaryStaus = i[-1].lower()
        if LegendaryStaus == "true":
            LegendaryBool = True
        else:
            LegendaryBool = False
        type1 = i[2].lower()
        type2 = i[3].lower()
        matchingTypes = userType1 == type1 and userType2 == type2 or userType1 == type2 and userType2 == type1
        if matchingTypes and LegendaryBool:
            results.append(i)
    if not results:
        print("There are no legendary pokemon with the types specified!")
    else:
        output(results)

def surpriseMe():
    """Displays a random pokemon"""
    randomPokemon = [random.choice(content)] # chooses a random pokemon from the list of pokemon
    output(randomPokemon)
#event loop
print("Pokédex Search Engine")
while True:
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
        break
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
    print("")