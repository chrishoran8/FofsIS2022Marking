############### ############### ############### ############### ############### ############### ############### ############### ############### 92

#Exam Version 5 October 2021 by Chris Horan

##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Sgt Trishna Gurung
##Course Number:SIMR 21/001
##Student Number: 30085128

##complete each task which is shown as a comment. 
#complete each task directly below the comment
#each task shows a task number, and number of marks awarded
#on each task requiring an output, ensure the task goes on a separate line (unless stated)
#and ensure that it states the task number prior to any output e.g. Task 11 
#upload your final file to your assigned folder share on class.net
# \\192.168.0.207\regiNumber

#####################################################
#Section 1 25 marks


#1) Create and Assign a type float variable called fltOne the value 2 (3)

print("1) Create and Assign a type float variable called fltOne the value 2")
fltOne=float(2)
print("\nOutput of flttwo: ",fltOne)

#2) Create and Assign a type float variable called fltTwo the value 200 (3)

print("\n 2) Create and Assign a type float variable called fltTwo the value 200")
fltTwo=float(200)
print("\nOutput of flttwo: ",fltTwo)

#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)

print("\n3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne")
fltThree=float(fltTwo * fltOne)
print("\nOutput of fltThree: ",fltThree)

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)

print('\n4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo ="')
stringOne=fltTwo * fltOne
print("\nOutput of stringOne: ",stringOne)
 
#5) On the console, output stringOne and fltThree (in that order) (3)

print("\n5) On the console, output stringOne and fltThree (in that order)")
print("\nOutput of stringOne: ",stringOne)
print("\nOutput of fltThree: ",fltThree)

#6) increment fltOne  (3)

print("\n6) increment fltOne")
fltOne+=1
print("\nincrement for fltOne: ",fltOne)

#7)  prompt the user to provide an input to fltFour with the message "Please provide another number for fltFour". Ensure a float is given (4)

print('\n7)  prompt the user to provide an input to fltFour with the message "Please provide another number for fltFour". Ensure a float is given')
fltFour=float(input("Please provide another number for fltFour: "))
print(fltFour)

#8) on the console, output the product of fltThree and flotFour with a suitable message showing this is task 8(3) 

print("\n8) on the console, output the product of fltThree and flotFour with a suitable message showing this is task 8")
print("product of fltThree and fltFour : ",fltThree,"*",fltFour,"=",fltThree*fltFour)

#####################################################
#Section 2 30 Marks

#9) Prompt the user to say a greeting. Apply a decision based on the greeting inputted. 
#If the user types "Hello", respond by outputting to the console "Good greeting"
#If the user types "hello", respond by outputting to the console "Good greeting, but capital letter?"
#If the user types anything else, respond by outputting to the console "Not what I was expecting" (10)

print("\n9) Prompt the user to say a greeting. Apply a decision based on the greeting inputted.")
greeting=input("Enter your greeting word: ")
if greeting=="Hello":
    print("\nGood greeting")
elif greeting=="hello":
    print("\nGood greeting, but capital letter?")
else:
    print("\nNot what I was expecting")

#10) create a list called listOfStrings (4)

print("\n10) create a list called listOfStrings")
listofStrings=[]
print("\n listofStrings= ",listofStrings)

# 11 part a) populate the list with the following strings:
# Hello, Hi, Salut, Good Day, Bon Dia, Howdy
# Output the list to the console with a suitable message(4)

print("""\n11 part a) populate the list with the following strings
Hello, Hi, Salut, Good Day, Bon Dia, Howdy
Output the list to the console with a suitable message""")

listofStrings=['hello','Hi','Salut','Good Day','Bon Die','Howdy']

print("\nOutput of the list listofString: ",listofStrings)

#11 part b) create a for loop to iterate through the above list and 
#output to the console the length of the shortest greeting (12)
#for example, for the above list, the output should be 2

print("""\n11 part b) create a for loop to iterate through the above list and 
output to the console the length of the shortest greeting (12)
for example, for the above list, the output should be 2""")

count1=[]
for i in listofStrings:
    count=len(i)
    count1.append(count)
count1.sort()
shortestGreeting=count1[0]
print("\nThe length of shortest greeting in the list listofString= ",shortestGreeting)
    

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
############### ############### ############### ############### ############### ############### ############### ############### ############### -4
#this function should return the force, not print it out. Currently it returns None. It needs to return the force. You lose 4 marks

print("""\n12) Sir Isaac Newton created the three laws of motion. The second of these laws 
#links force with mass and acceleration. The formula is as follows:
#Force = Mass x Acceleration. Force is measured in Newtons
#Write a function called calcForc which takes two arguments (Mass and Acceleration) and returns
# the product of these two arguments
#Therefore a call of calcForce(500,2) should returnn 1000
#Give the default acceleration as 9.81 (Gravity). a call of calcForce(100) should return 981""")

def calcForce(mass,acceleration=9.81):
    print("\nForce for the mass of",mass,"and acceleration",acceleration,"=", mass*acceleration,"Newton")

calcForce(500,2)
calcForce(100)

#13) create a function called caseChanger which takes a string argument written all in lower case
#It will return the word with all letters in the same case except 'a' which it will convert to 'A'
#For example, caseChanger("case") would return "cAse". another example caseChanger("casE") returns "cAsE"
#Write a suitable print statement to show this working (15)
############### ############### ############### ############### ############### ############### ############### ############### ############### -4
#this function should return the string, not print it out. therefore, you lose 4 marks

print("""\n#13) create a function called caseChanger which takes a string argument written all in lower case
#It will return the word with all letters in the same case except 'a' which it will convert to 'A'
#For example, caseChanger("case") would return "cAse". another example caseChanger("casE") returns "cAsE"
#Write a suitable print statement to show this working""")

def caseChanger(ca):
    print("\n Case change for the given string is:",end="")
    for i in ca:
        if i=="a":
            i="A"
        print(i,end="")
inpStr=input("\nEnter the string written all in lower case: ")
lowerinpStr=inpStr.lower()
caseChanger(lowerinpStr)


##################################################### 
#Section 4 20 marks

#14 a) Create a list that represents a set of cars. The list should contain the following
#cars: Focus,Up,Golf,Robin,Fiesta,Astra,Tiguan,Leaf (4 marks)

print("""\n\n 14 a) Create a list that represents a set of cars. The list should contain the following
#cars: Focus,Up,Golf,Robin,Fiesta,Astra,Tiguan,Leaf""")

carList=['Focus','Up','Golf','Robin','Fiesta','Astra','Tiguan','Leaf']
print("\nList of car, carList: ",carList)

#14 part b) use a method to order the cars so that they are in alphabetical order (3 marks)
#print this to the screen

print("""\n14 part b) use a method to order the cars so that they are in alphabetical order (3 marks)
#print this to the screen""")

carList.sort()
print("\ncarList in alphabetical order: ",carList)


#15) Populate a tuple that represents top speeds of the cars (4 marks)
#These are the respective speeds for the alphabetically ordered car list
# 120,100,125,126,78,40,105,93

print("""\n15) Populate a tuple that represents top speeds of the cars (4 marks)
#These are the respective speeds for the alphabetically ordered car list
# 120,100,125,126,78,40,105,93""")

topSpeed=(120,100,125,126,78,40,105,93)
print("\nTop Speed tuple:",topSpeed)

#16) Dictionary question (9 marks)
#create a dictionary which joins the cars with their corresponding speed. 
#write a suitable print statement which prints all cars, with their speeds

print("""\n16) Dictionary question (9 marks)
#create a dictionary which joins the cars with their corresponding speed. 
#write a suitable print statement which prints all cars, with their speeds""")

carDict=dict(zip(carList,topSpeed))
print("\nDictionary with the car and their corresponding top speed: ",carDict)