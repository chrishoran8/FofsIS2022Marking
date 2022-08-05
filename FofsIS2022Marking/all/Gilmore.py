############### ############### ############### ############### ############### ############### ############### ############### ############### 100
#Exam Version 5 October 2021 by Chris Horan

##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Gilmore LM
##Course Number: SIMR 21/001
##Student Number: 30107802 

##complete each task which is shown as a comment. 
#complete each task directly below the comment
#each task shows a task number, and number of marks awarded
#on each task requiring an output, ensure the task goes on a separate line (unless stated)
#and ensure that it states the task number prior to any output e.g. Task 11 
#upload your final file to your assigned folder share on class.net
# \\192.168.0.207\test\regiNumber

#####################################################
#Section 1 25 marks


#1) Create and Assign a type float variable called fltOne the value 2 (3)
fltOne = 2.0

#2) Create and Assign a type float variable called fltTwo the value 200 (3)
fltTwo = 200.0

#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)
fltThree = fltOne * fltTwo
# print(fltThree) # This command verifies the configuration of fltThree
# print(type(fltThree)) # This function confirms that fltThree is type float

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
stringOne = "The product of fltOne and fltTwo = "
# print(stringOne) # This function will confirm that stringOne is correct

#5) On the console, output stringOne and fltThree (in that order) (3)
print(stringOne, fltThree)

#6) increment fltOne  (3)
fltOne += 1
# print(fltOne) #This function confirms that fltOne has been incremented by 1

#7)  prompt the user to provide an input to fltFour with the message "Please provide another number for fltFour". Ensure a float is given (4)
fltFour = float(input("Please provide another number for fltFour"))
# print(fltFour) # This function will output the user's float to the console

#8) on the console, output the product of fltThree and floatFour with a suitable message showing this is task 8(3) 
print("This is Task 8 which will output the product of fltThree and fltFour:",fltThree * fltFour)

#####################################################
#Section 2 30 Marks

#9) Prompt the user to say a greeting. Apply a decision based on the greeting inputted. 
#If the user types "Hello", respond by outputting to the console "Good greeting"
#If the user types "hello", respond by outputting to the console "Good greeting, but capital letter?"
#If the user types anything else, respond by outputting to the console "Not what I was expecting" (10)
greeting = input("Say a greeting: ")

if greeting == "Hello":
    print("Good greeting")
elif greeting == "hello":
    print("Good greeting, but capital letter?")
else:
    print("Not what I was expecting")

#10) create a list called listOfStrings (4)
listOfStrings = []

# 11 part a) populate the list with the following strings:
# Hello, Hi, Salut, Good Day, Bon Dia, Howdy
# Output the list to the console with a suitable message(4)
listOfStrings += "Hello", "Hi", "Salut", "Good Day", "Bon Dia", "Howdy"
print("There are many ways to say hello, depending on the language you are speaking: ", listOfStrings)

#11 part b) create a for loop to iterate through the above list and 
#output to the console the length of the shortest greeting (12)
#for example, for the above list, the output should be 2
shortestGreeting = "longStringPlaceholder" # This creates a variable called shortestString and assigns a long string which is longer than the strings contained in listOfStrings
for greeting in listOfStrings: # This for conditional statement will iterate through the listOfStrings list
    if len(greeting) < len(shortestGreeting): # This if conditional statement will compare the length of each greeting with the shortestGreeting variable. If the greeting length is less than shortestGreeting, the body of the if statement will execute
        shortestGreeting = greeting # This replaces the shortestGreeting with the greeting which has less length
    
print("The greeting with the shortest length is 'Hi', which has a length of: ", len(shortestGreeting))


#####################################################
#Section 3 25 marks

#12) Sir Isaac Newton created the three laws of motion. The second of these laws 
#links force with mass and acceleration. The formula is as follows:
#Force = Mass x Acceleration. Force is measured in Newtons
#Write a function called calcForc which takes two arguments (Mass and Acceleration) and returns
# the product of these two arguments
#Therefore a call of calcForce(500,2) should returnn 1000
#Give the default acceleration as 9.81 (Gravity). a call of calcForce(100) should return 981
#(10)
def calcForc(Mass,Acceleration=9.81): # This creates the function defined as calcForc, which accepts two arguments in the parameters, called Mass and Acceleration. Acceleration is assigned a default value of 9.81
    return Mass * Acceleration # When the function is invoked, it will return the product of Mass and Acceleration

# print(calcForc(500,2)) # This will test the calcForc function with the arguments 500 and 2, respectively
# print(calcForc(100)) # This will test the calcForc function with the argument 100 for paramater Mass, and the default of 9.81 for Acceleration



#13) create a function called caseChanger which takes a string argument written all in lower case
#It will return the word with all letters in the same case except 'a' which it will convert to 'A'
#For example, caseChanger("case") would return "cAse". another example caseChanger("casE") returns "cAsE"
#Write a suitable print statement to show this working (15)
def caseChanger(userWord): # The function caslled caseChanger is created with the userWord parameter which will accept one argument
    newUserWord = "" # This creates an variable named newUserWord, which is assigned an empty string which acts as a placeholder
    for letter in userWord: # This for conditional statement will iterate through each letter in the userWord argument
        if letter != "a": # if the letter in the userWord string is not a lower case letter a, the body of the if statement will be executed
            newUserWord += letter # The letter will be added to the newUserWord in its current format
        else: # If the letter in userWord is a lower case letter a, the body of the else statement will be executed
            newUserWord += letter.upper() # The letter will be changed to uppercase and added to the newUserWord in its new format
    return newUserWord # newUserWord will be returned

print(caseChanger(input("Enter a word: "))) # This prompts the user to enter a word which will invoke the caseChanger function. caseChanger("case") would return "cAse". another example caseChanger("casE") returns "cAsE" 



##################################################### 
#Section 4 20 marks

#14 a) Create a list that represents a set of cars. The list should contain the following
#cars: Focus,Up,Golf,Robin,Fiesta,Astra,Tiguan,Leaf (4 marks)
carList = ["Focus","Up","Golf","Robin","Fiesta","Astra","Tiguan","Leaf"] # This creates the variable named carList and assigns the list of cars to it
# print(carList) # This function checks the carList was created properly

#14 part b) use a method to order the cars so that they are in alphabetical order (3 marks)
#print this to the screen
alphabeticalCarList = sorted(carList) # This creates a new variable called alphabeticalCarList and assigns the sorted carList to it
print(alphabeticalCarList) # This prints the alphabeticalCarList to the console



#15) Populate a tuple that represents top speeds of the cars (4 marks)
#These are the respective speeds for the alphabetically ordered car list
# 120,100,125,126,78,40,105,93
carTopSpeeds = (120,100,125,126,78,40,105,93) # This creates a variable called carTopSpeeds and assigns the tuple to it
# print(carTopSpeeds) # This prints the carTopSpeeds variable to the console
# print(type(carTopSpeeds)) # This confirms the carTopSpeeds variable is type tuple


#16) Dictionary question (9 marks)
#create a dictionary which joins the cars with their corresponding speed. 
#write a suitable print statement which prints all cars, with their speeds
carsAndSpeeds = dict(zip(alphabeticalCarList, carTopSpeeds)) # This creates a dictionary called carsAndSpeeds and inserts the alphabeticalCarList and carTopSpeeds in parallel
print(carsAndSpeeds) # This print statement will output the carsAndSpeeds dictionary to the console

