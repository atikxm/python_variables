#name="alien"
#age=22
#height=1.75


#Print Variable & Type
'''''
name="alien"
age=22
print(name)
print(age)
print(type(name))
'''

#Variable declare korp

'''amy_name = "alien"
my_age = 22
my_height = 1.75
is_student = True

print(my_name)
print(my_age)
print(my_height)
print(is_student)
# Print Type    
print(type(my_name))
print(type(my_age))
print(type(my_height))
print(type(is_student)) 
'''
#input variable

'''name = input("Tumar naam ki? ")
print("Hello", name)
'''
'''
num1=input("Tumar prothom number ta ki: ")
num2=input("Tumar ditiyo number ta ki:")  

num1=int(num1)
num2=int(num2)

sum=num1+num2
print("tomar namer jogfol holo : ",sum)
'''
'''
name=input("Enter your name : ")
age=input("Enter your age : ")

print ("Your name is : ", name)
print("Your agfe is : ",age)
'''
'''
num1=input("Enter first number : ")
num2=input("Enter second number : ")
sum=int(num1)+int(num2)
print("The sum of the two numbers is : ", sum)

print(type(num1))
print(type(num2))
print(type(sum))

user_input = input("Are you student ? (yes/no): ")
is_student = user_input.lower() == 'yes'
print("Is the user a student?", is_student)


'''

# User er kache jiggesha kora holo
answer = input("Tumi ki Python shikho? (yes/no): ").strip().lower()

# Uttor onujayi response dewa holo
if answer == "yes":
    print("Darun!")
elif answer == "no":
    print("Suru koro aaj thekei!")
else:
    print("Please sudhu 'yes' ba 'no' likho.")

#avarage er jonno input
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

avarage = (num1 + num2) / 2
print("The average of the two numbers is:", avarage)