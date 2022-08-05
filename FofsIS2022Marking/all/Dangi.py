############### ############### ############### ############### ############### ############### ############### ############### ############### 100
#Exam Version 5 October 2021 by Chris Horan

##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Rajendra Dangi
##Course Number: SIMR 22/001
##Student Number: 30120262

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
fltThree = float(fltTwo * fltOne)


#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
stringOne = "The product of fltOne and fltTwo = "


#5) On the console, output stringOne and fltThree (in that order) (3)
print("Task 5:", stringOne, fltThree)

#6) increment fltOne  (3)
fltOne += 1

#7)  prompt the user to provide an input to fltFour with the message "Please provide another number for fltFour". Ensure a float is given (4)
fltFour = float(input("Please provide another number for fltFour"))

#8) on the console, output the product of fltThree and fltFour with a suitable message showing this is task 8(3)
print("Task 8:", "The product of fltThree and fltFour =", (fltThree * fltFour))

#####################################################
#Section 2 30 Marks

#9) Prompt the user to say a greeting. Apply a decision based on the greeting inputted. 
#If the user types "Hello", respond by outputting to the console "Good greeting"
#If the user types "hello", respond by outputting to the console "Good greeting, but capital letter?"
#If the user types anything else, respond by outputting to the console "Not what I was expecting" (10)
user_input = input("Say a greeting: ")
if user_input == "Hello":
    print("Good greeting")
elif user_input == "hello":
    print("Good greeting, but capital letter?")
else:
    print("Not what I was expecting")


#10) create a list called listOfStrings (4)
listOfStrings = []

# 11 part a) populate the list with the following strings:
# Hello, Hi, Salut, Good Day, Bon Dia, Howdy
# Output the list to the console with a suitable message(4)
listOfStrings = ["Hello", "Hi", "Salut", "Good Day", "Bon Dia", "Howdy"]
print("Task 11(a):","The elements in the list, listOfStrings, are:", listOfStrings)

#11 part b) create a for loop to iterate through the above list and 
#output to the console the length of the shortest greeting (12)
#for example, for the above list, the output should be 2
shortest = len(listOfStrings[0])
for i in range (len(listOfStrings)):
    if i + 1 < len(listOfStrings):
        if len(listOfStrings[i]) < shortest:
            shortest = len(listOfStrings[i])
        elif shortest > len(listOfStrings[i+1]):
           shortest = len(listOfStrings[i+1])
print("Task 11(b)", "The lenght of the shortest greeting is:", shortest)   

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
def calcForc (Mass, Acceleration = 9.81):
    return Mass * Acceleration
print("Task 12:", calcForc(100), "Newtons")

#13) create a function called caseChanger which takes a string argument written all in lower case
#It will return the word with all letters in the same case except 'a' which it will convert to 'A'
#For example, caseChanger("case") would return "cAse". another example caseChanger("casE") returns "cAse"
#Write a suitable print statement to show this working (15)
def caseChanger (word):
    word = word.lower()
    new_word =""
    for letter in word:
        if letter != "a":
            letter = letter
        if letter == "a":
            letter = "A"
        new_word += letter
    return new_word   
print("Task 13:", "The word casE will be changed to:",caseChanger("casE"))





##################################################### 
#Section 4 20 marks

#14 a) Create a list that represents a set of cars. The list should contain the following
#cars: Focus,Up,Golf,Robin,Fiesta,Astra,Tiguan,Leaf (4 marks)
cars = ["Focus", "Up", "Golf", "Robin", "Fiesta", "Astra", "Tiguan", "Leaf"]

#14 part b) use a method to order the cars so that they are in alphabetical order (3 marks)
#print this to the screen
cars.sort()

#15) Populate a tuple that represents top speeds of the cars (4 marks)
#These are the respective speeds for the alphabetically ordered car list
# 120,100,125,126,78,40,105,93
top_speed = (120,100,125,126,78,40,105,93)

#16) Dictionary question (9 marks)
#create a dictionary which joins the cars with their corresponding speed. 
#write a suitable print statement which prints all cars, with their speeds
dict = {}
i = 0
for elem in cars:
    dict[elem] = top_speed[i]
    i += 1

print("Task 16: ", "The dictionary with car and their respective top speed is:\n", dict, sep="")