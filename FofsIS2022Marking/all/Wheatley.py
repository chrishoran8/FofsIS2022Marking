############### ############### ############### ############### ############### ############### ############### ############### ############### 80

#Exam Version 5 October 2021 by Chris Horan

##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Wheatley
##Course Number: SIMR 21/001
##Student Number: 25227528

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
fltThree = fltOne + fltTwo

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
stringOne = "The product of fltOne and fltTwo = "

#5) On the console, output stringOne and fltThree (in that order) (3)
print(stringOne)
print(fltThree)

#6) increment fltOne  (3)
fltOne = fltOne + 1

#7)  prompt the user to provide an input to fltFour with the message "Please provide another number for fltFour". Ensure a float is given (4)
fltFour = float(input("Please provide another number for fltFour: "))

#8) on the console, output the product of fltThree and floatFour with a suitable message showing this is task 8(3) 
print(fltThree * fltFour)

#####################################################
#Section 2 30 Marks

#9) Prompt the user to say a greeting. Apply a decision based on the greeting inputted. 
#If the user types "Hello", respond by outputting to the console "Good greeting"
#If the user types "hello", respond by outputting to the console "Good greeting, but capital letter?"
#If the user types anything else, respond by outputting to the console "Not what I was expecting" (10)
goodGreeting = input("Please enter a greeting: ")

for response in goodGreeting:
    if goodGreeting == "Hello":
        print("Good greeting")
        break
    elif goodGreeting == "hello":
        print("Good greeting, but a capital letter?")
        break
    else:
        print ("Not what I was expecting...")
        break

#10) create a list called listOfStrings (4)
listOfStrings = []

# 11 part a) populate the list with the following strings:
# Hello, Hi, Salut, Good Day, Bon Dia, Howdy
# Output the list to the console with a suitable message(4)
listOfStrings = ["Hello", "Hi", "Salut", "Good Day", "Bon Dia", "Howdy"]
print("These are common greetings: ", listOfStrings)

#11 part b) create a for loop to iterate through the above list and 
#output to the console the length of the shortest greeting (12)
#for example, for the above list, the output should be 2
############### ############### ############### ############### ############### ############### ############### ############### ############### -8
#the below only works for the given strings. The if cascade and logic is all dependent on the given number of strings and lenght of strings. 
#it is therefore very innefficient and not dissimilar from you simply outputing the number 2 because you can visually see that "Hi" is the shortest
#that said, it does peform some logic which gets you to your result. Lose 8 marks

for x in listOfStrings:
    if x[0] < x[1]:
        print(len(listOfStrings[1]))
        break
    elif x[1] < x[2]:
        print (len(listOfStrings[1]))
        break
    elif x[2] < x[3]:
        print (len(listOfStrings[2]))
        break
    elif x[3] < x[4]:
        print (len(listOfStrings[3]))
        break
    elif x[4] < x[5]:
        print (len(listOfStrings[4]))
        break
    else:
        print (len(listOfStrings[5]))




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

def calcForc (m, a=9.81):
    return m*a
calcForc (100)

#13) create a function called caseChanger which takes a string argument written all in lower case
#It will return the word with all letters in the same case except 'a' which it will convert to 'A'
#For example, caseChanger("case") would return "cAse". another example caseChanger("casE") returns "cAsE"
#Write a suitable print statement to show this working (15)
############### ############### ############### ############### ############### ############### ############### ############### ############### -12
#the below does not do anything other than set up the function header and return. Lose 12 marks
word = input("Please enter a word: ")
def caseChanger (a):
    return a
caseChanger(word)


##################################################### 
#Section 4 20 marks

#14 a) Create a list that represents a set of cars. The list should contain the following
#cars: Focus,Up,Golf,Robin,Fiesta,Astra,Tiguan,Leaf (4 marks)
carModels = ["Focus", "Up", "Golf", "Robin", "Fiesta", "Astra", "Tiguan", "Leaf"]

#14 part b) use a method to order the cars so that they are in alphabetical order (3 marks)
#print this to the screen
list.sort(carModels)
print(carModels)

#15) Populate a tuple that represents top speeds of the cars (4 marks)
#These are the respective speeds for the alphabetically ordered car list
# 120,100,125,126,78,40,105,93
carSpeed = (120, 100, 125, 126, 78, 40, 105, 93)


#16) Dictionary question (9 marks)
#create a dictionary which joins the cars with their corresponding speed. 
#write a suitable print statement which prints all cars, with their speeds

carSpec ={}
for i in range (8):
    carSpec[carModels[i]]=carSpeed[i]
print("This list compares vehicle models and their speed", carSpec)