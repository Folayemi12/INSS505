#collecting input for user
number1=int(input("Enter number 1:"))
#using if statement to check if input is divisible by 3 and 5
for number1 in range(1,number1):
    if(number1%3==0) and (number1%5==0):
        print(number1,"Tic Tac")
#using the if statement to check if input is divisible by 3
    if(number1%3==0):
        print(number1,"Tic")
#using the if statement to check if input is divisible by 5
    if(number1%5==0):
        print(number1,"Tac")
#using while loop statement to print numbers from 1-20
a=1
while a<21:
    a+=1
    print(a)
input1=int(input("Enter input1:"))
input1=1
while input1<16:
    input1+=1
    if input1%3==0 and input1%5==0:
        print(input1, "Tic Tac")
#step 9
limit=5
while limit>0:
     user_value = int(input("Enter the value:"))
     if user_value>0:
         print(user_value," /n  Successful")
         break
     else:
         limit-=1
         print("invalid entry, please enter a valid value")
import random
user_value = int(input("Enter int value"))
main = random.randint(1, user_value)
limit = 0
while True:
    limit+= 1
    my_value = int(input("first value:"))
    if my_value== main:
        print("Perfect")
        break
    elif my_value!=main:
        print("both numbers don't match")
    else:
        print("invalid")


