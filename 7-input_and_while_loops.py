# Author: Sherzod Oltinboyev:
# Date: 23.12.2020:
# Theme: 7 Input and While loops:

# 7-1. Rental Car:
car=input("Enter the name of car which you want to rent? ")
print("Let me see if I can find you a "+car)

# 7-2. Restaurant Seating:
number=input("How many people are in your dinner group? ")
number=int(number)

if number >= 8:
    print("You will have to wait for a table!")
else:
    print("Your table is ready!")

# 7-3. Multiples of ten:
user=input("Please, enter the number? ")
user=int(user)
if user%10==0:
    print(str(user)+ " is a multiple of 10")
else:
    print(str(user)+" is not multiple of 10")

# 7-4. Pizza toppings:
prompt="\nPlease enter a series of pizza toppings"
prompt+="\nEnter 'quit' when you are finished "
message=""
while message!="quit":
    message=input(prompt)
    print(message)


# 7-5. Movie Tickets:
age=input("Please enter your age? ")
age=int(age)
if age < 3:
    print("The ticket price is free")
elif age > 3:
    print("Ticket price is $10")
elif age > 12:
    print("The ticket price is $15")

# 7-6. Three exits:
# 1.
prompt="\nPlease enter a series of pizza toppings"
prompt+="\nEnter 'quit' when you are finished "
active=True
while active:
    message=input(prompt)

    if message=="quit":
        active=False
    else:
        print(message)
# 2.
prompt="\nPlease enter a series of pizza toppings"
prompt+="\nEnter 'quit' when you are finished "
while True:
    message=input(prompt)
    if message=="quit":
        break
    else:
        print(message)




# 7-7. Infinity:hghg
a=10
while a < 34:
    a+=1
    print(a)

# Author: Sherzod Oltinboyev:
# Date: 26.12.2020:
# Theme: 7 Input and While loops:

# 7-8. Deli:
sandwich_orders=["pastrami",'pizza','pastrami','hot dog','donar','lavash','pastrami']
finished_sandwiches=[]
while sandwich_orders:
    finished=sandwich_orders.pop()
    print("I made your "+finished+" sandwich")
    finished_sandwiches.append(finished)
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-9.No Pastrami:
sandwich_orders=["pastrami",'pizza','pastrami','hot dog','donar','lavash','pastrami']
finished_sandwiches=[]
print("Pastrami is running out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)

# 7-10. Dream Vacation:
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name? ")
    response=input('If you could visit one place in the world,\nwhere would you go? ')
    responses[name]=response

    repeat=input("Would you like to let another person respond? (yes/no) ")
    if repeat=="no":
        polling_active=False
print("\n---Poll Results---")
for name,response in responses.items():
    print(name.title()+' would like to go to '+response.title())
