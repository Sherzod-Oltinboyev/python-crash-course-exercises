# Author: Sherzod Oltinboyev:
# Date: 18.12.2020:
# Theme: 5-If Statements:

# 5-1.Conditional Tests:
car='mercedes'
print("Is car=='mercedes'? I predict True")
print(car=='mercedes')

print("Is car=='bmw'? I predict False")
print(car=='bmw')

writer='Alisher Navoiy'
print("Is 'Alisher' Navoiy==writer? I predict True")
print(writer=="Alisher Navoiy")

print("Is writer=='Thomas Edision'? I predict False")
print(writer=='Thomas Edision')

winner="France"
print("Is winner=='France'? I predict True")
print(winner=='France')

print("Is winner=='Egypt'? I predict False")
print(winner=='Egypt')

famous='Bill Geyts'
print("Is famous=='Bill Geyts'? I predict True")
print(famous=="Bill Geyts")

print("Is famous=='Harry'? I predict False")
print(famous=="Harry")

inventer='Enstein'
print("Is inventer=='Enstein'? I predict True")
print(inventer=="Enstein")

print("Is inventer=='Messi'? I predict False")
print(inventer=='Messi')

# Author: Sherzod Oltinboyev:
# Date: 19.12.2020:
# Theme: 5-If Statements:

# 5-2. More Conditional Tests:
# 1.
languages=['uzbek','english','russia','arab']
for language in languages:
    if language=="uzbek":
        print("My native language is a "+language.title())
    else:
        print(language.title())
# 2.
name="Islom"
print(name.lower()=="islom")
# 3.
age=22
experience=3
if (age >= 18) and (experience >=5 ):
    print("You are suitable for our company")
else:
    print("Sorry  we couldn't hire you")
# 4.
number=17
if (number > 17) or (number <17 ):
    print("Your prediction is incorrect")
else:
    print("Your prediction is correct!")
    print("We congratulate you!")
# 5.
order_list=['Lavash','Kabob','Jiz','Tabaka']
if "Somsa" in order_list:
        print('Your order is ready')
else:
        print("We don't have this food.\n\tYou can order other foods")

# 5-3. Alien Colors #1:
alien_color="red"
if alien_color=="green":
    print("You earned 5 points")
elif alien_color=="red":
    print("You lost")

# 5-4. Alien Color #2:
alien_color="green"
if alien_color=="green":
    print("You earned 5 points for shooting thr alien")
elif alien_color!="green":
    print("You earned 10 points for shooting thr alien")

# 5-5. Alien Color #3:
# 1.
alien_color="green"
if alien_color=="green":
    print("You earned 5 points for shooting thr alien")
elif alien_color=="yellow":
    print("You earned 10 points for shooting thr alien")
elif alien_color=="red":
    print("You earned 15 points for shooting thr alien")

# 2.
alien_color="red"
if alien_color=="green":
    print("You earned 5 points for shooting thr alien")
elif alien_color=="yellow":
    print("You earned 10 points for shooting thr alien")
elif alien_color=="red":
    print("You earned 15 points for shooting thr alien")

# 3.
alien_color="yellow"
if alien_color=="green":
    print("You earned 5 points for shooting thr alien")
elif alien_color=="yellow":
    print("You earned 10 points for shooting thr alien")
elif alien_color=="red":
    print("You earned 15 points for shooting thr alien")

# 5-6. Stages of Life:
age=19
if (age<2):
    print("That person is a babby")
elif age<4:
    print("That person is a toddler")
elif age<13:
    print("That person is a kid")
elif age<20:
    print("That person is a teenager")
elif age<65:
    print("That person is an adult")
else:
    print("That person is an elder")

# 5-7. Favourite Fruit:
favorite_fruits=['apple','apelsin','banana']
if "apple" in favorite_fruits:
    print("I really like apples")
if 'persic' in favorite_fruits:
    print("I really like persic")
if "apelsin" in favorite_fruits:
    print("I really like apelsin")
if "banana" in favorite_fruits:
    print("I really like banana")
if "orange" in  favorite_fruits:
    print("I really like oranges")

# 5-8. Hello Admin.
usernames=['islom','ilhom','ixtiyor','admin','oybek']
for names in usernames:
    if names=="admin":
        print("Hello "+names.title()+",would you like to see a status report.")
    else:
        print("Hello "+names.title()+",thank you for logging again.")
# 5-9. No Users:
users=[]
if users:
    for user in users:
        print("Adding "+user+".")
    print("Finishing")
else:
    print("We need to find users")




# 5-10. Checking Usernames:
current_users=['Hamid','Nabi',"Ulug'bek",'sardor',"Abdulaziz"]
new_users=['Guli','Anvar','Nabi','Sardor','Diyor']
for users in new_users:
    if users in current_users:
        print("Sorry,This username is already exist.\n\tPlease, enter new username")
    else:
        print("This username is available")

# 5-11. Ordinal Numbers:
aiy='th'
list=[1,2,3,4,5,6,7,8,9]
for lists in list:
    if lists==1:
        print("1st")
    if lists==2:
        print('2nd')
    if lists==3:
        print("3rd")
    if lists > 3:
        print(lists,'th')

