'''a = 5
b = 9
first_name = "vansh"
last_name =  "kumar"
print(first_name)
full_name = "vansh kumar"  print(full_name)
country = "india"
print(country)  city = ("dehradun")
print(city) print("my name is vansh")
print("i am from bafgpat up")
'''
'''
a = "a"
print(ord(a))'''

'''
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two+num_one
print(diff)
product = num_two*num_one
print(product)
division = num_one/ num_two
print(division)
reminder = num_one%num_two
print(reminder)
floor_division = num_one//num_two
print(floor_division)
print(3.14*30)
print(22/7*30)
py=3.14
radius=30
print(py*radius*radius)
circumference_of_circle=2*py*radius
print(circumference_of_circle)'''

'''
NUMBER_OF_MEMBER_A = (float(input("WRITE THE NUMBER OF MEMBER A: ")))
NUMBER_OF_MEMBER_B = (float(input("WRITE THE NUMBER OF MEMBER B: ")))
TOTAL = NUMBER_OF_MEMBER_A + NUMBER_OF_MEMBER_B
print("Total: ",TOTAL)'''

'''
a = float(input("enter a value"))
print(type(a))
num1 =float(input ('enter valu: '))
num2 = 20
total = (num1 + num2)
print("total",total)
'''
'''
a = 10
b = 15
print(a > b)'''

'''
name=  "chandu champion"
print(f"my name is {name}")'''
'''
name="chandu champion"
age=16

print("my name is %s and my age %d"%(name,age))
print("my name is {} and my age {}".  format(name,age))'''
'''
a = [1, 2]
b = a
c = [1, 2]
print(a is b, a is c, a == c)'''

'''
Clint = int(input("Type the numbers : "))
if Clint > 0 :
    print("The number is : positive")
if Clint < 0 :
    print("The number is : negative")
else :
    print("The number is : Zero")
'''
'''
num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
opration = int(input("1.sum,2.sub,3.mul1,4.div"))
if opration == 3 :
    print(num1 * num2 )
'''
'''
num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
sum = (num1 + num2)
if  (sum>=10 and sum<=20):
    print(15)
else:
    print(0) 
'''
'''
print("Temprature convertor farhemheit to celsius ")
farhenheit = float(input("Enter the ferhenheit degree : "))
Celsius = 5/9*(farhenheit-32)
print("The celsius degree is : ",Celsius,"C")
'''
'''
print("Temprature convertor celsius to farhemheit ")
celsius = float(input("Enter the celsius degree : "))
Farhenheit = 9/5*celsius+32
print("The farhenheit degree is : ",Farhenheit,"F")
'''
'''
A = float(input("Enter a number 1 : "))
B = float(input("Enter a number 2 : "))
if  A > B : 
    print(f"{A} is grater  than number 2. ")
elif B > A :
    print(f"{B} is grater than number 1. ")
else :
    print("both are value equel")
'''
'''

A = float(input("Enter the number 1 : "))        
B = float(input("Enter the number 2 : "))
C = float(input("Enter the number 3 : "))
if A > B and A > C :
    print("A is grater than B and C. ")
elif B > A and B > C : 
    print("B is grater than A and C. ")
elif C > A and C > B :
    print("C is grater than A and B. " )
else :
    print("All values are Equal. ")
'''
'''

A = int(input("Enter the number: " ))
if A % 2 == 0 and  A % 5 == 0 :
    print("Divisible by both 2 and 5. ")
elif A % 2 == 0 :
    print("Divisible by 2.")
elif A % 5 == 0 :
    print("Divisible by 5.")
else : 
    print("Not Divisible by either")
'''
'''
client = int(input("enter the number : "))
if client % 2 == 0 :
    print("Even")
elif client % 1 == 0 :
    print("odd")
'''
'''
for i in range(1,101,) :
    print(i)
'''
'''
for i in  range(1,101):
    if i % 2 != 0 :
        print(i)
'''
'''
for i in range (1,11):
    print("5 x",i,"=",5*i)
    print(f"5 x {i} = {5*i}")
'''
'''
name = input("Enter your name: ")
city = input("Enter your city: ")
print(f"{name} lives in {city}.")
'''
'''
n = int(input("Enter the positive number: "))
for i in range (1,n +1):
    print(f" The total of the numbers from 1 through {n} is: {i}.")
'''
'''
for  i in range (5):
    print ()
    for j in range(5):
        print(j, end=" ")
'''
'''
for i in range (1,6):
    print ()
    for j in range (i):
        print(i,end="")
'''
'''
for i in (range (1,10)):
    print()
    for j in range (i): 
        print(i , end=" ")
'''
'''
n = int(input("Enter the positive number here : "))
total = 0
for i in range (n+1):
    total += i
print(total)
'''
'''
n = int(input("Enter the positive number here : "))
total = 1
for i in range (1,11):
    total *= i
    print(total)
'''
'''
n = 1
while n < 10:
    n+=2
    print(n)
# '''
'''
n = 2
while True :
    n >1
    print(n)
'''
'''
n = 1
while True :
    print(n)
    n+=1                    
'''
'''
n = 0 
while n < 50 :
    if n % 2 == 0 :
        print(n)
    n += 1
'''
'''
n = 0
while n < 100 :
    if n % 2 != 0 :            
        print(n)                
    n += 1         
'''
'''
user = ''
while user.lower() !='quit': 
    user=input("Enter something: ")
    print(f"this is {user}") 
'''
'''
password = ""
count = 0
while password != "python123" and count < 3 :                       
    password = input("Enter password : ")
    count += 1
    if password == "python123" :
        print("Access granted ")
    else :
        print("Wrong password ")
if password != "python123":
    print("Account locked")
'''
'''
user = ''
count = 0
while user.lower() != "yes" and count < 5:
    user =  input("Enter  something : ")
    count += 1
    if user.lower() ==  "yes" :
        print("Right")
    else :
        print("Wrong")
if user.lower() != "yes" :
    print("Attempt over ")
'''
'''
for i in range(10):
    if i ==5:
        continue
    print(i)
'''
'''
student="bhunam"
students = ["nikhil","aaush","bhunam","anuj"]
for student in students:
     if student == 'bhunam':
         break
         print(student)
'''
'''
count=0  
while count < 30:
    count += 1
    if count % 3 == 0 :
        continue
    print(count)
'''
'''
count = 0 
while count < 15 :
    count += 1
    if count % 2 == 0 :
        continue 
    if count > 10 :
        break
    print(count ,end=" ")
'''
'''
count = 0
while count < 20 :
    count += 1
    if count > 10 and count % 4 == 0 :
        continue
    print(count)
 '''
'''
a = [1,2,3,4,5,6,7,8,9,10,]
a  [8]= 11                       # modifying list
print(a)
'''
'''
a = [1,2,3,4,5,6,7,8,9,10,]
a.append(16)                        # adding list
print(a)
'''
'''
a =  [1,2,3,4,5,6,7,8,9,10,]
a.remove(10)                           # remove list
print(a)
'''
'''
a = [1,2,3,4,5,6,7,8,9,10,]
a.pop(6)                                # list pop
print(a)
'''
'''
a = [1,2,3,4,5,6,7,8,9,10,]
print(len(a))                            # lenght of list
'''
# fruits = ['appple,','banana','mango']
# fruits[1]='kiwi'
# print(fruits)

# fruits = ['appple,','banana','mango']
# fruits.append('orange')
# print(fruits)

# fruits = ['appple,','banana','mango']
# fruits.insert(0,'graph')
# print(fruits)
'''
fruits = ['appple,','banana','mango']
fruits.insert(0,'graph')
print(fruits)
'''
'''
item = ['book','pencil','eraser']
if 'pen' in item :
    item.remove('pen')
else :
    print('not is item')
    print(item)
'''
'''
a = [1,2,3,4,]
a.pop()  
print(a)
'''
'''
a = 'hello'
a += "b"
print(a)
'''
'''
a = 'hello'
for i in (a):
    print(i, end='  ')
'''
'''
a = "hello"
n = len(a) -1
b = ""
while n >= 0 :
    b += a[n]
    n -= 1
print(b)
'''

'''
Ages = [19,22,19,24,20,25,26,24,25,24,]
min_age = min(Ages)
max_age = max(Ages)
print(f"min_age : {min_age}")
print(f"max_age : {max_age}")

Ages.append(min_age)
Ages.append(max_age)
print(f"Again add min and max : {Ages}")

age_average = sum(Ages) / len(Ages)
print(f"Average of ages : {age_average}")

Range_of_Ages = max_age - min_age 
print(f"Range of the ages : {Range_of_Ages}")
'''
'''
# fruits = ['apple','mango','kiwi']
# for i in range(len(fruits)) :
#      print(fruits[i].upper())
'''
'''
Ages = [19,22,19,24,20,25,26,24,25,24,]
print(Ages[::-1])                              #for reversed
'''
'''
Ages = [19,22,19,24,20,25,26,24,25,24,]
print(sorted(Ages))
'''
'''
ages = [19,22,19,24,20,25,26,24,25,24,]
total = 0
for i in ages :
    total += i
print(total)
print('Average : ' , total /len(ages))
'''
'''
name = {
'first_name' : 'vansh',
'last_name' : 'kumar',

'addres' :{
    'state' : 'up',
    },
    'adres' : {
    'village' : 'tikri',
        },
        'address' : {
            'town':'tikri',
            'chairman':'upendra pal'
        }

}
print(name['address']['chairman'])




for key , value in name.items():  # show both output key and values with for loop
    print(key,':',value)

for key in name:                  # show output only key use with loop
    print(key)

for value in name.values():        # show output only values use with loop
    print(value)

name['age'] = 24
name['skills'][1]= "overthinking"
name['skills'].append("sleeping")
print(name['skills'])
print(name)
print(name.values())
print(name.keys())
print(name.items())                 # convert dictionary to list

name.popitem()         # for delete variable and all values
print(name)

#  del name             # for delete variable and all values

name.pop('addres')         # partucular key remove  
print(name)
'''
'''

def even () :
    john =  int(input("Enter a number: "))
    if john %2 == 0 :
        return f" The {john} number is Even. "
    else:
        return f" The {john} number is Odd. "
    
print(even())

'''
'''
def check(list):
    first_type = type(list[3])
    for item in list :
        if first_type == type(item):
            return f" all value same."
        else:
            return f"all value not same."
print(check(['Vansh', 12,3,42,'hello']))
'''
'''
def geet () :
    name = "vansh"
    return(name)
'''

'''

class UPI :
    def pay(self, amount) :
        print(f"{amount} is paid via upi")
class Cash :
    def pay(self , amount) :
        print(f"{amount} is paid via cash")
def checkout(method,amount) :
     method.pay(amount)
checkout(UPI(), 50000)
checkout(Cash(), 300)
'''
