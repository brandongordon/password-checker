passwordHistory = []    #This is where passwords are stored.
rules = {'MaxLength': 16, 'MinLength': 8, 'MustUpper': True, 'MustLower': True, 'MustNum': True, 'MustSpecial': True}    #Hopefully gonna store rules here 

def checkPassword(pword):    #New function to check if password satisfies rules. Initialize to "False". When triggered they will toggle to "True" and can't re-toggle
    shortEnough = False
    longEnough = False
    hasUpper = False
    hasLower = False
    hasNumber = False
    hasSpecial = False
    specialChars = "\'~!#$%^*()_+-={}|[]\\:<>?,./"    #Store all special characters in a string so we can see if the individual letters are "in" specialChars

    if len(pword) <= rules['MaxLength']:
        shortEnough = True
    if len(pword) >= rules['MinLength']:
        longEnough = True
    for n in pword:
        if n.isupper():
            hasUpper = True
        if n.islower():
            hasLower = True
        if n.isdigit():
            hasNumber = True
        if n in specialChars:
            hasSpecial = True

    runDebug(shortEnough, longEnough, hasUpper, hasLower, hasNumber, hasSpecial)

    if shortEnough and longEnough and hasUpper == rules['MustUpper'] and hasLower == rules['MustLower'] and hasNumber == rules['MustNum'] and hasSpecial == rules['MustSpecial']:
        return True
    else:
        return False

def runDebug(dshortEnough, dlongEnough, dhasUpper, dhasLower, dhasNumber, dhasSpecial):
    if showDebug == True:
        print ("\nShort Enough? = ", dshortEnough, "\nLong Enough? = ", dlongEnough, "\nHas Upper-Case? = ", dhasUpper, rules['MustUpper'], "\nHas Lower-Case? = ", dhasLower, rules['MustLower'], "\nHas Number(s)? = ", dhasNumber, rules['MustNum'], "\nHas Special Character(s)? = ", dhasSpecial, rules['MustSpecial'])

###########################################################################################################################################################################################################################

showDebug = True

print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print ("\n\t Welcome to 'Password Rule Creator and Validator'!")
print ("\n\t\t   A Program by Brandon Gordon")
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
print ("By Default, Debug information is shown. You can toggle this option in the menu!")
    
while True:
    print ("\nChoose from the following menu options: ")
    menuChoice = input("\t[M]odify Rules\n\t[C]heck Password\n\t[H]istory\n\t[T]oggle Debug Messages\n\t[Q]uit\n>").upper()

    if menuChoice == "M":
        print ("Current Password Rules:\n\
        [-] Maximum of", rules['MaxLength'], "characters\n\
        [-] Minimum of", rules['MinLength'], "character(s)\n\
        [-] Must contain an upper-case character?", rules['MustUpper'], "\n\
        [-] Must contain a lower-case character?", rules['MustLower'], "\n\
        [-] Must contain a number?", rules['MustNum'], "\n\
        [-] Must contain a special character? '~!#$%^*()_+-={}|[]\:<>?,./?", rules['MustSpecial'])
        
        rules['MaxLength'] = int(input("\nNew maximum character length: "))
        rules['MinLength'] = int(input("New minimum character length: "))
        rules['MustUpper'] = bool(int(input("At least 1 upper-case character required? 0 or 1: ")))
        rules['MustLower'] = bool(int(input("At least 1 lower-case character required? 0 or 1: ")))    #Try clean the boolean process up to make it more friendly
        rules['MustNum'] = bool(int(input("At least 1 number required? 0 or 1: ")))
        rules['MustSpecial'] = bool(int(input("At least 1 special character required? 0 or 1: ")))            
        
        
    elif menuChoice == "C":
        print ("Current Password Rules:\n\
        [-] Maximum of", rules['MaxLength'], "characters\n\
        [-] Minimum of", rules['MinLength'], "character(s)\n\
        [-] Must contain an upper-case character?", rules['MustUpper'], "\n\
        [-] Must contain a lower-case character?", rules['MustLower'], "\n\
        [-] Must contain a number?", rules['MustNum'], "\n\
        [-] Must contain a special character? '~!#$%^*()_+-={}|[]\:<>?,./?", rules['MustSpecial'])
        
        password = input("\n\nEnter your password: ")
        passwordHistory.append(password)
        if checkPassword(password):
            print("\nYour password is valid.")
        else:
            print("\nYour password is not valid.")



    elif menuChoice == "H":
        for passwordTry, password in enumerate(passwordHistory, 1):
            print ("Password", passwordTry, "-", password)
    elif menuChoice == "T":
        showDebug = not showDebug
        print ("Debug messages now set to", showDebug)

    elif menuChoice == "Q":
        print ("You have quit the program")
        break
        


    
    
