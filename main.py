import datetime
employees={}

def readEmployees(employees):#time complexity=O(n) where n= number of lines in the users file
    with open("test2.txt", "r") as f: #https://www.w3schools.com/python/python_file_open.asp
      for x in f:
          line=x.split(",")
          employees[line[0].strip().lower()]={
          "username":line[1].strip().lower(),
          "timeStamp":int(line[2].strip()),
          "gender":line[3].strip().lower(),
          "salary":float(line[4].strip())
        }