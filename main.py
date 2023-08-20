import datetime
employees={}

#read employees line by line from users.txt file
def readEmployees(employees):#time complexity=O(n) where n= number of lines in the users file
    with open("users.txt", "r") as f: #https://www.w3schools.com/python/python_file_open.asp
      for x in f:
          line=x.split(",")
          employees[line[0].strip().lower()]={
          "username":line[1].strip().lower(),
          "timeStamp":int(line[2].strip()),
          "gender":line[3].strip().lower(),
          "salary":float(line[4].strip())
        }
          


#display number of male and female employees registered in the system
def statistics(employees):# time complexity: O(n) where n= number of employees (i.e number of lines in the users file)
    countMale=0
    countFemale=0
    for emp in employees.values():
        if emp['gender'] == 'male':
            countMale+=1
        elif emp['gender'] == 'female':
           countFemale+=1
    return f"Female Employees: {countFemale} \nMale Employees: {countMale} "



#add a new employee to the empolyees dictionary
def addEmployee(employees):# time complexity: O(1) fixed time for adding 1 employee at a time
    username = input("Enter Username: ")
    gender = input("Enter Gender (male/female): ")
    while gender!="male" and gender!="female":
       gender = input("please enter correct gender (male/female): ")
    salary = int(input("Enter salary: "))
    while salary<0:
       salary = int(input("Please enter correct salary: "))
    length=len(employees)
    if length<9:
       id="emp00"+str(length+1)
    elif length>8 and length<99:
       id="emp0"+str(length+1)
    else:
       id="emp"+str(length+1)
    today = datetime.datetime.today().strftime("%Y%m%d")
    employees[id]={
       "username":username,
            "timeStamp":int(today),
            "gender":gender,
            "salary":int(salary)
       
    }
    print("Successfully added!")



#display all employees in cecreasing order based on timestamp
def displayAll(employees):
    res = sorted(employees.items(), key = lambda x: x[1]['timeStamp'], reverse=True)#sorted method: https://www.geeksforgeeks.org/python-sort-nested-dictionary-by-key/

    #reversed: https://www.programiz.com/python-programming/methods/built-in/sorted#:~:text=The%20sorted()%20function%20accepts,iterable%20in%20the%20descending%20order.
    for key, value in res:
       print(f"{key}, {employees[key]['username']},  {employees[key]['timeStamp']}, {employees[key]   ['gender']}, {employees[key]['salary']}\n")



#change the salary of an employee that exists
def salaryChange(employees): #time complexity: O(1) considering we are changing the salary of 1 employee at a time and the dictionary look has also a fixed time complexity of O(1)
  id=input("Enter employee ID: ")
  if id in employees:
    salary=int(input("Enter new salary: "))
    while salary<0:
      salary = int(input("Please enter correct salary: "))
    employees[id]["salary"]=salary
    print("The salary is changed")
  else:
    print("Employee not found")




#remove an employee from the employees dictionary
def removeEmployee(employees): #time complexity: O(1) considering we are removing 1 employee at a time and the dictionary look has also a fixed time complexity of O(1)
  id=input("Enter employee ID: ")
  if id in employees:
    del employees[id]
    print("Employee has been deleted")
  else:
     print("Employee not found")



#increase the salary of an existing employee by a specific perventage
def raiseSalary(employees): #time complexity: O(1) considering we are raising the salary of 1 employee at a time and the dictionary look has also a fixed time complexity of O(1)
  id=input("Enter employee ID: ")
  if id in employees:
    percent=float(input("Enter raise percentage: "))/100
    while percent<=0:
      percent= float(input("Please enter correct raise percentage: "))/100
    increase= employees[id]["salary"]*percent
    employees[id]["salary"]+=round(increase,2)
    print(f"{employees[id]['username']} Salary was increased by {percent*100} %")
  else:
    print("Employee not found")



#save the changes made by admit after exit into the users file
def exitNow(employees):# time complexity: O(n) where n is the number of employees
  with open("users.txt", "w") as file:#https://www.w3schools.com/python/python_file_write.asp
    for key in employees:
        file.write(f"{key}, {employees[key]['username']},  {employees[key]['timeStamp']}, {employees[key]   ['gender']}, {employees[key]['salary']}\n")




#Normal user(employee) menu
def userMenu(key, value): #time complexity O(1), although we are intentially repeating a branch of the function( showing the menu of choices)
  enterTime=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") #https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
  if  value["gender"]=="male":
      greeting="Mr."
  else:
     greeting="Ms."
  print(f"Hi {greeting} {value['username']}")
  while True:
    print("Menu:")
    print("1. Check my Salary")
    print("2. Exit")
    choice=input("Enter choice: ")
    if choice == "1":
      print(f"your salary is {value['salary']}")
    elif choice=="2":
      leaveTime=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      message=f"Employee id: {key}, of username: {value['username']}, logged in at {enterTime}, and logged out  at {leaveTime}\n"
      filename=key+".txt"
      with open(filename, "w") as file:
          file.write(message)
    else:
      print("Please enter a correct option from the menu")



# admin menu
def adminMenu(): #time complexity O(1), although we are intentially repeating a branch of the function( showing the menu of choices)
  print("Menu:")
  print("1. Display Statistics")
  print("2. Add an Employee")
  print("3. Display all Employees")
  print("4. Change Employee’s Salary")
  print("5. Remove Employee")
  print("6. Raise Employee’s Salary")
  print("7. Exit")
  while True:
    choice = input("Enter choice: ")	
    if choice == '1':	
      print(statistics(employees))	
    elif choice == '2':	
      addEmployee(employees)	
    elif choice == '3':	
      displayAll(employees)	
    elif choice == '4':	
      salaryChange(employees)	
    elif choice == '5':	
      removeEmployee(employees)	
    elif choice == '6':	
      raiseSalary(employees)	
    elif choice == '7':	
      exitNow(employees)	
      break	
    else:	
      print("Please enter a correct option from the menu")




#log in to check credentials for admin and employee
def logIn(employees): #time complexity: O(1), fixed number of attempts(5)
    attempts=5
    while attempts>0:
        if attempts==5:
            userName=input("Enter Username: ")
            password=input("Enter Password: ")
        else:
            userName=input(f"Enter Username: ({attempts} attempts remaining)")
            password=input(f"Enter Password: ({attempts} attempts remaining)")
        if userName=="admin" and password=="admin123123":
            adminMenu()
            break
        for key, value in employees.items():
            if value['username'] == userName:
                userMenu(key, value)
                return
    
        print("incorrect Username and/or Password")
        attempts-=1
    if attempts==0:
       print("Maximum ammount of attempts reached, please try again later")




readEmployees(employees)
logIn(employees)