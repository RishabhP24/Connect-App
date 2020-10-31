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
print(x)
