print('helloworld')
print('my first pull request') #Trying Github Pull request 1st time 
print('this is my second try') #Trying Github Pull request 2nd time
print('this is my third try')  #Trying Github Pull request 3rd time
#lets try input statement
i=int(input())
print(i)
#lets try list,tuple,set 
thilist=["Apple","Bannana","Cherry"]
print(thisList)
thistuple=("apple","banana","cherry")
print(thistuple)
thisset={"apple","banana","cherry"}
print(thisset)
#lets try Lambda
x=lambda a:a+10
print(x(5))
x=lambda a,b:a*b
print(x(5,6))

#lets try scope
def myfunc():
  x=300
  print(x)
 
my func() #Here we call our Scope
def myfunc1():
  x=300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()

#now we try some Built-in Math function
x=min(5,10,25)
y=max(5,10,25)
print(x)
print(y)

z=abs(-7.2)
print(z) #Try Yourself

a=pow(4,3)
print(a)#this is use for power

#lets try some file handling
f=open("filename.txt")
f=open("demofile.txt","rt")#here r stand for read only and t stand for text value


#Test MySql connector
import mysql.connector #After downloading Connector library we have to import that library in our program

mydb=mysql.connector.connect(host="localhost",user="yourusername"password="yourpassword")
print(mydb) 
#Creatin A Database
import mysql.connector #After downloading Connector library we have to import that library in our program

mydb=mysql.connector.connect(host="localhost",user="yourusername"password="yourpassword")
mycuursor=mydb.cursor()

mycursor.execute("Create Database mydatabase")

#Checking if database Exist
import mysql.connector #After downloading Connector library we have to import that library in our program

mydb=mysql.connector.connect(host="localhost",user="yourusername"password="yourpassword")
mycursor=mydb.cursor()
mycursor.execute("Show Database")

for x in mycursor:
  print(x)

#Creating A Table
import mysql.connector #After downloading Connector library we have to import that library in our program

mydb=mysql.connector.connect(host="localhost",user="yourusername"password="yourpassword")
mycursor=mydb.cursor()

mycursor.execute("Create Table Customers(name VARCHAR(255), address(VARCHAR(255))")
