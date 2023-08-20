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
            countMale=+1
        elif emp['gender'] == 'female':
           countFemale+=1
    return f"there are {countFemale} female employees and {countMale} male employees"