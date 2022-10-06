## This is Python3, not Python2 which was learned from Codecademy
from os.path import exists

codeDict = { 
  'A': '`',
  'a': '~',
  'B': '1', 
  'b': '!',
  'C': '2',
  'c': '@',
  'D': '3',
	'd': '#',
  'E': '4',
  'e': '$',
  'F': '5',
  'f': '%',
  'G': '6',
  'g': '^',
  'H': '7',
  'h': '&',
	'I': '8',
  'i': '*',
  'J': '9',
  'j': '(',
  'K': '0',
  'k': ')',
  'L': '-',
  'l': '_',
  'M': '=',
	'm': '+',
  'N': '[',
  'n': '{',
  'O': ']',
  'o': '}',
  'P': ';',
  'p': ':',
  'Q': ',',
  'q': '<',
	'R': 'ø',
  'r': '>',
  'S': '/',
  's': '?',
  'T': '|',
  't': '¢',
  'U': '£',
  'u': '¥',
  'V': 'ƒ',
	'v': '¿',
  'W': '¬', 
  'w': 'ß',
  'X': 'µ',
  'x': '±',
  'Y': '€',
  'y': '†',
  'Z': '‡',
  'z': 'þ',
	' ': '.' 
}
#Get user input
print ("Hello, Welcome to my Decryption and Encryption Program!")
userChoice = 'a'
menuString = """Select an option:
1. Encrypt a Message to a file (Message can only contain letters)
2. Decrypt a Message to a file
x. Exit the program
"""
string1 = ""
string2 = ""
menu1D = "Please enter a file to encrypt: "
menu1E = "Enter a file to write encryption to: "
menu2E = "Enter an encrypted file: "
menu2D = "Enter a file to write decrytion to: "
#Ask for user input until valid input entered
while (userChoice != '1') and (userChoice != '2') and (userChoice != 'x') and (userChoice != "X"):
  userChoice = input(menuString)
  if (userChoice != '1') and (userChoice != '2') and (userChoice !=   'x') and (userChoice != "X"):
    print ("Error: Please enter valid menu option")
  #Exit program if user wants to exit
  if userChoice == 'x' or userChoice == 'X':
    print("Have a nice day!")
    break
  #Do what the user selected
  elif userChoice == '1':
    string1 = ""
    string2 = ""
    #Get user files and make sure they are txt files
    while (string1.endswith(".txt") == False):
      string1 = input(menu1D)
      if (string1.endswith(".txt") == False):
        print ("Error: Please enter txt file!")
      #Check to see if user file exists
      if (exists(string1) == False):
        string1 = ""
        print ("Error: Please enter existing file!")
    while (string2.endswith(".txt") == False):
      string2 = input(menu1E)
      if (string2.endswith(".txt") == False):
        print ("Error: Please enter txt file!")
    #Open and read valid file
    inputFile = open(string1, "r")
    decrypted =  str(inputFile.read())
    encrypted = ''
    #Use the map to find corresponding characters to replace with
    for i in decrypted:
      encrypted = encrypted + (codeDict[i])
      #Write encrypted string newly created file with the name
    with open(str(string2), "x") as outputFile1:
      outputFile1.write(encrypted)
    userChoice = "0"

  elif userChoice == '2':
    string1 = ""
    string2 = ""
    while (string1.endswith(".txt") == False):
      string1 = input(menu2E)
      if (string1.endswith(".txt") == False):
        print ("Error: Please enter txt file!")
      #Check to see if user file exists
      if (exists(string1) == False):
        string1 = ""
        print ("Error: Please enter existing file!")
    while (string2.endswith(".txt") == False):
      string2 = input(menu2D)
      if (string2.endswith(".txt") == False):
        print ("Error: Please enter txt file!")
    #Start Decryption
    inputFile = open(string1, "r")
    encrypted =  str(inputFile.read())
    decrypted = ''
    #compare encrypted to each value in map, if so, get the              decrypted version and append it to string
    for i in encrypted:
      for j in codeDict:
        if(codeDict[j] == i):
          decrypted = decrypted + j
    #Write decrypted string newly created file with the name
    with open(str(string2), "x") as outputFile2:
      outputFile2.write(decrypted)
    userChoice = "0"
