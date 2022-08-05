############### ############### ############### ############### ############### ############### ############### ############### ############### 85

#Exam Version 5 October 2021 by Chris Horan

##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Sgt Ian Harvey
##Course Number: SMIR 21/001
##Student Number: 25231968

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
print(stringOne, fltThree, sep="")

#6) increment fltOne  (3)
fltOne += 1

#7)  prompt the user to provide an input to fltFour with the message "Please provide another number for fltFour". Ensure a float is given (4)
#print("Please provide another number for fltFour" )
fltFour = float(input("Please provide another number for fltFour: "))
print(fltFour)

#8) on the console, output the product of fltThree and fltFour with a suitable message showing this is task 8(3) 
print("The product of fltThree and fltFour = ", fltThree + fltFour)

print()
#####################################################
#Section 2 30 Marks

#9) Prompt the user to say a greeting. Apply a decision based on the greeting inputted. 
#If the user types "Hello", respond by outputting to the console "Good greeting"
#If the user types "hello", respond by outputting to the console "Good greeting, but capital letter?"
#If the user types anything else, respond by outputting to the console "Not what I was expecting" (10)
greeting = str(input("Please say a greeting: "))
print(greeting)
if greeting == "Hello":
    print("Good greeting")
elif greeting == "hello":
    print("Good greeting, but capital letter?")
else:
    print("Not what I was expecting")

print()
#10) create a list called listOfStrings (4)
listOfStrings = []

# 11 part a) populate the list with the following strings:
# Hello, Hi, Salut, Good Day, Bon Dia, Howdy
# Output the list to the console with a suitable message(4)
listOfStrings = ["Hello", "Hi", "Salut", "Good Day", "Bon Dia", "Howdy"]
print(listOfStrings)

print()
#11 part b) create a for loop to iterate through the above list and
#output to the console the length of the shortest greeting (12)
#for example, for the above list, the output should be 2
############### ############### ############### ############### ############### ############### ############### ############### ############### -12
#not achiieved so lose 12 marks

for i in range (0,7):
    listOfStrings.sort()    # sort via size of word, how???
    #return i = shortest    # how??
    #a = listOfStrings.find("hi")    # find via size of word, how???
    #

print(listOfStrings)
#print(a)

#for i in len(listOfStrings):

print()
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
############### ############### ############### ############### ############### ############### ############### ############### ############### -3
#the default acceleration was required to be 9.81, and no default was required for mass. Lose 3 marks

def calcForce(Mass=500, Acceleration=2):
    result = Mass * Acceleration
    return result
print(calcForce(500, 2))
print()

acceleration = 9.81
print(calcForce(50,2) * acceleration)

print()
#13) create a function called caseChanger which takes a string argument written all in lower case 
#It will return the word with all letters in the same case except 'a' which it will convert to 'A'
#For example, caseChanger("case") would return "cAse". another example caseChanger("casE") returns "cAsE"
#Write a suitable print statement to show this working (15) exp for elem in list if cond
def caseChanger(word="case"):
    result = word.replace("a", "A")
    return result
print(caseChanger("case"))
print(caseChanger("casE"))
print(caseChanger("apples and oranges"))

print()
##################################################### 
#Section 4 20 marks

#14 a) Create a list that represents a set of cars. The list should contain the following
#cars: Focus,Up,Golf,Robin,Fiesta,Astra,Tiguan,Leaf (4 marks)
carList = ["Focus","Up","Golf","Robin","Fiesta","Astra","Tiguan","Leaf"]

#14 part b) use a method to order the cars so that they are in alphabetical order (3 marks)
#print this to the screen
carList.sort()
print(carList)

print()
#15) Populate a tuple that represents top speeds of the cars (4 marks)
#These are the respective speeds for the alphabetically ordered car list
# 120,100,125,126,78,40,105,93
topSpeeds = tuple(['120', '100', '125', '126', '78', '40', '105', '93'])
print(topSpeeds)

print()
#16) Dictionary question (9 marks)
#create a dictionary which joins the cars with their corresponding speed. 
#write a suitable print statement which prints all cars, with their speeds
carsAndSpeeds = dict(zip(carList, topSpeeds))
print("Cars and their speeds: \n", carsAndSpeeds)

print()
