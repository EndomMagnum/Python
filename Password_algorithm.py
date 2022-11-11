password = str(input("Enter base password word : "))

first_let = password[0]
last_let = password[-1]
middle_let = int(len(password)) *2
length = int(len(password)) 
num = int(middle_let / 2)
num2 = int(middle_let + length + num) **2


print(first_let)
print(last_let)
print(length)
print(middle_let)
print(num)
print(num2)

print(first_let,length,middle_let,num,last_let,num2)

