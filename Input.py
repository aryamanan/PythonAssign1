print('Welcome to my Assignment1 [Copyright Aryan Arora(21103007), all rights reserved]\n\n' )

def ques1():
    
    print('Question 1 program \n')
     
    num1 = float(input("enter marks of student 1: "))
    num2 = float(input("enter marks of student 2: "))
    num3 = float(input("enter marks of student 3: "))
 
    
 #finds the average of these numbers

    avg=(num1+num2+num3)/3

    print("The average of", num1, num2, num3, "is", avg, "\n")
    cont = input("Press R to proceed: ")
    if cont.upper() == "R":
      ques2()
      
    else:
      print("your input ", cont, " is invalid")
      cont
    

def ques2():
    #program to compute income tax

    #assigning constants first by user input
    
    print('Question 2 program \n')


    inc=float(input("Enter your gross income in dollars: "))
    dep=int(input("Enter total dependents: "))
    inc_tax=(inc-10000-(dep*3000))


    final_tax=inc_tax*0.2
    final_tax=round(final_tax,2)

    if final_tax<0:
        final_tax=0
        
    else:
        final_tax=final_tax


    print("Your income tax is: ", final_tax, "\n")
    cont = input("Press R to proceed: ")
    if cont.upper() == "R":
      ques3()
      
    else:
      print("your input ", cont, " is invalid")
      cont

def ques3():
    
    print('Question 3 program \n')
     
    sid=input("Enter SID: ")
    name=input("Enter name: ")

    gender=input("Enter Gender (M or F): ")

    course=input("Enter course name: ")
    cgpa=float(input("Enter CGPA: "))

    student=[sid,name,gender,course,cgpa]

    print(student, "\n")
    cont=input("Press R to proceed: ")
    if cont.upper() == "R":
      ques4()
      
    else:
      print("your input ", cont, " is invalid")
      cont

def ques4():
    print('Question 4 program \n')
     
    marks_list=[]
    for i in range (5):
        mark=float(input("Enter mark of Student:" ))
        marks_list.append(mark)
        
    #arranges marks in an array style list
    marks_list.sort()
    
    print(marks_list, "\n")
    cont=input("Press R to proceed: ")
    if cont.upper() == "R":
      ques5a()
      
    else:
      print("your input ", cont, " is invalid")
      cont

def ques5a():
    print('Question 5 program \n')
     
    color=['red','Green', "White",'Black', 'Pink', 'Yellow']

    #removes 4th input from array
    color.pop(3)
    print(color, "\n")
    cont=input("Press R to proceed: ")
    if cont.upper() == "R":
      ques5b()
      
    else:
      print("your input ", cont, " is invalid")
      cont

def ques5b():
    print('Question 5b program \n')
     
    color=['red','Green', "White",'Black', 'Pink', 'Yellow']
    color[color.index("Black")]="Purple"; color[color.index("Pink")]="Purple"
    print(color, "\n")

    Print("thank you")
 
def Input():
 firstInp=input("Run programs from Ques1 to Ques5b in order [Y or N]: ")

 if firstInp.upper() == "Y":
   print("\n\n")
   ques1()
   
 elif firstInp.upper() == "N":
   print("choose which one you want directly from here [1, 2, 3 , 4, 5a, 5b]\n")
   
 else:
   print("invalid input, please pick between Y and N")
   print("reconfirm your choice correctly this time!!\n")
   Input()
   
   
Input()
