# If a five-digit number is input through the keyboard, write a program to print a new number by adding one to each of its digits. 
# For example, if the number that is input is 12391, then the output should be displayed as 23502.



a=int(input("Enter the 5 digit number :- "))

num=(a//10000+1)%10
print(num)
num2=((a//1000)%10+1)%10
print(num2)
num3=((a//100)%10+1)%10
print(num3)
num4=((a//10)%10+1)%10
print(num4)
num5=(a%10+1)%10
print(num5)

number=num+num2+num3+num4+num5
print(number)